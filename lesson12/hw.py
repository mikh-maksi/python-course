import pickle
import random
import string
import sys
from collections import UserString
from abc import ABC, abstractmethod
import re
from datetime import date, datetime
from pathlib import Path
from typing import Optional, List
import cmd


class IncorrectInput(Exception):
    pass


def validate_input_decorator(func):
    def inner(*args):
        try:
            result = func(*args)
        except IncorrectInput as e:
            print(e)
            return
        return result

    return inner


class DataField(ABC, UserString):
    preferred_order: int = 0

    def __init__(self, *args, **kwargs):
        super(DataField, self).__init__(*args, **kwargs)
        self.value = self.data

    @property
    def value(self) -> str:
        return self.data

    @value.setter
    @abstractmethod
    def value(self, value: str):
        """Field value validation code should be set here"""
        pass


class FirstNameField(DataField):
    preferred_order = 0

    @DataField.value.setter
    def value(self, value: str):
        self.data = value


class LastNameField(DataField):
    preferred_order = 1

    @DataField.value.setter
    def value(self, value: str):
        self.data = value


class PhoneField(DataField):
    preferred_order = 2
    PHONE_REGEX = re.compile(r"^\+?(\d{2})?\(?(0\d{2})\)?(\d{7}$)")

    def __init__(self, value: str, name: str = "Home"):
        """
        :param value: Phone number value
        :param name: Phone name ex.: Home, Mobile, iPhone, etc.
        """
        super().__init__(value)
        self.name = name
        self.country_code: str = ""
        self.operator_code: str = ""
        self.phone_number: str = ""

    @DataField.value.setter
    def value(self, value: str):
        value = value.replace(" ", "")
        search = re.search(self.PHONE_REGEX, value)
        try:
            country, operator, phone = search.group(1, 2, 3)
        except AttributeError:
            raise IncorrectInput(f"No phone number found in {value}")

        if operator is None:
            raise IncorrectInput(f"Operator code not found in {value}")

        self.country_code = country if country is not None else "38"
        self.operator_code = operator
        self.phone_number = phone
        self.data = f"+{self.country_code}({self.operator_code}){self.phone_number}"


class OrganizationField(DataField):
    preferred_order = 3

    @DataField.value.setter
    def value(self, value: str):
        self.data = value


class AddressField(DataField):
    preferred_order = 4

    @DataField.value.setter
    def value(self, value: str):
        self.data = value


class BirthdayField(DataField):
    preferred_order = 5
    date_format = "%d.%m.%Y"

    def __init__(self, *args):
        self._date: Optional[date] = None
        super().__init__(*args)

    @DataField.value.setter
    def value(self, value: str):
        try:
            self._date = datetime.strptime(value, self.date_format).date()
        except ValueError:
            raise IncorrectInput(
                f"Birthday should be given in format: 'zero_padded_day.month.year'. Given: {value}"
            )
        self.data = value

    @property
    def is_birthday_today(self) -> bool:
        today = date.today()
        return self._date.replace(year=today.year) == today

    @property
    def days_to_birthday(self) -> int:
        today = date.today()
        this_year_birthday = self._date.replace(year=today.year)
        if today > this_year_birthday:
            next_birthday = self._date.replace(year=today.year + 1)
            return (next_birthday - today).days
        else:
            return (this_year_birthday - today).days


class EmailField(DataField):
    preferred_order = 6
    EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

    @DataField.value.setter
    def value(self, value: str):
        if not self.EMAIL_REGEX.match(value):
            raise IncorrectInput(f"{value} is not an email.")
        self.data = value


class Record:
    def __init__(self, *fields: DataField):
        self.id: Optional[int] = None
        self.data: List[DataField] = list(fields)
        self.sort()

    def sort(self):
        self.data.sort(key=lambda x: x.preferred_order)

    def append(self, value: DataField):
        self.data.append(value)
        self.sort()

    def remove(self, idx: int):
        self.data.pop(idx)

    def update(self, idx: int, value: str):
        field: DataField = self.data[idx]
        field.data = value

    def __contains__(self, item: str):
        for field in self.data:
            if item in field:
                return True
        return False

    def __str__(self) -> str:
        result_str = f"{self.id:=^30}\n"
        for idx, field in enumerate(self.data):
            result_str += f"{idx}. {field.__class__.__name__}: {field}\n"
        return result_str


class AddressBook:
    def __init__(self, filename: str = ""):
        self.records = {}
        self.last_record_id = 0
        if not filename:
            filename = self.random_string()
        self.file = Path(filename)
        self.load()

    @staticmethod
    def random_string(string_length=8):
        name = "".join(
            random.choice(string.ascii_lowercase) for _ in range(string_length)
        )
        name += ".bin"
        return name

    def add(self, record: Record):
        self.records[self.last_record_id] = record
        record.id = self.last_record_id
        self.last_record_id += 1

    def delete(self, record_id: int):
        try:
            self.records.pop(record_id)
        except KeyError:
            raise IncorrectInput(f"Record {record_id} not found")

    def search(self, search_str: str) -> List[int]:
        result = []
        for record_id, record in self.records.items():
            if search_str in record:
                result.append(record_id)
        return result

    def update_record(self, id_: int, record: Record):
        self.records[id_] = record

    def show_record(self, record_id: int) -> str:
        result_str = f"{self.records[record_id]}\n"
        return result_str

    def show_records(self, chunk_size: int = 10) -> str:
        counter, result_str = 0, ""
        for record in self.records.values():
            result_str += str(record)
            counter += 1
            if counter == chunk_size:
                yield result_str
                counter, result_str = 0, ""
        yield result_str

    def dump(self):
        with open(self.file, "wb") as file:
            pickle.dump((self.last_record_id, self.records), file)

    def load(self):
        if not self.file.exists():
            return
        with open(self.file, "rb") as file:
            self.last_record_id, self.records = pickle.load(file)


PARENT = Path().parent
BIN_FILES: List[Path] = list(
    filter(lambda x: x.suffix == ".bin", (file for file in PARENT.iterdir()))
)


class MainShell(cmd.Cmd):
    intro = "Welcome to the Address Book shell. Type help or ? to list commands.\n"
    prompt = "(ab) "

    def __init__(self, *args):
        super().__init__(*args)
        self.book: Optional[AddressBook] = None
        # TODO: Remove this check in production. Only for development
        if BIN_FILES:
            self.book = AddressBook(str(BIN_FILES[0]))

    def do_open(self, file_name=None):
        """Open Address Book:  OPEN my_book.bin"""
        if self.book:
            self.book.dump()
        self.book = AddressBook(file_name)
        print(f"New Address Book created. Saved to {self.book.file}")

    def do_new(self, _):
        """Create new record NEW"""
        record = Record()
        RecordShell(record=record).cmdloop()
        if record is not None:
            self.book.add(record)
            print(f"New record saved:\n{record}")
        else:
            print("All changes discarded.")

    def do_list(self, args=10):
        """Print Saved records. LIST [RECORDS NUMBER]"""
        if args:
            try:
                records_number = int(args)
            except ValueError:
                print(f"Chunk size is not int: {args}")
                return
            except TypeError:
                records_number = 10
        else:
            records_number = 10
        IterationShell(book=self.book, chunk_size=records_number).cmdloop()

    def do_search(self, args):
        """Search in Address Book for given key. SEARCH NAME"""
        ids = self.book.search(args)
        result = f"Search result for '{args}':\n"
        for id in ids:
            result += self.book.show_record(id)
        print(result)

    def do_update(self, args):
        """Update given record. UPDATE 1"""
        try:
            id_ = int(args)
        except (TypeError, ValueError):
            print(f"ID {args} is invalid.")
            return

        try:
            record = self.book.records[id_]
        except KeyError:
            print(f"Given id {id_} not found in Address Book")
            return
        RecordShell(record=record).cmdloop()
        self.book.update_record(id_, record)

    def do_exit(self, _):
        """Exit Address Book app: EXIT"""
        self.book.dump()
        return True

    do_EOF = do_exit


class RecordShell(cmd.Cmd):
    intro = "Record prompt. Enter ? or help to list commands.\n"
    prompt = "(record) "

    def __init__(self, *args, record: Record):
        super().__init__(*args)
        self.record = record

    def do_show(self, _):
        """Show current record state"""
        print(self.record)

    def do_remove(self, args):
        """Remove field by its index. REMOVE 2"""
        try:
            self.record.remove(int(args))
            print("Removal done")
        except ValueError:
            print(f"Index should be integer. {args} given.")
            return
        except IndexError:
            print(f"Field with index {args} does not exist in this record")
            return

    def do_update(self, args):
        """Update field by its index. UPDATE 0 Jhon"""
        try:
            idx, value = args.split()
        except ValueError:
            print("Two arguments are needed, field index and new value")
            return

        try:
            idx = int(idx)
        except ValueError:
            print(f"Index ID {args[0]} is invalid")
            return
        self.record.update(idx, value)

    def do_name(self, args):
        """Add First name. NAME Taras"""
        if not args:
            print("Name should not be empty")
            return
        field = FirstNameField(args)
        self.record.append(field)

    @validate_input_decorator
    def do_phone(self, args):
        """Add phone. PHONE +38095 123 45 67"""
        field = PhoneField(args)
        self.record.append(field)

    @validate_input_decorator
    def do_birthday(self, args):
        """Add birthday. BIRTHDAY 30.10.1970"""
        field = BirthdayField(args)
        self.record.append(field)

    @validate_input_decorator
    def do_last_name(self, args):
        """Add last name. LAST_NAME Shevchenko"""
        field = LastNameField(args)
        self.record.append(field)

    @validate_input_decorator
    def do_organization(self, args):
        """Add last name. ORGANIZATION Google Inc."""
        field = OrganizationField(args)
        self.record.append(field)

    @validate_input_decorator
    def do_address(self, args):
        """Add address. ADDRESS Baker st. 121b"""
        field = AddressField(args)
        self.record.append(field)

    @validate_input_decorator
    def do_email(self, args):
        """Add email. EMAIL valid@email.com"""
        field = EmailField(args)
        self.record.append(field)

    @staticmethod
    def do_q(_):
        """Save record and exit."""
        return True

    do_EOF = do_q


class IterationShell(cmd.Cmd):
    intro = "Iterate over all records. Press ENTER to continue\n"
    prompt = "(list) "

    def __init__(self, *args, book: AddressBook, chunk_size: int):
        super().__init__(*args)
        self.book = book
        self.chunk_size = chunk_size
        self.chunk_number = 0
        self.generator = self.book.show_records(chunk_size=self.chunk_size)

    def emptyline(self):
        try:
            print(next(self.generator))
            self.chunk_number += 1
            chunks_left = len(self.book.records) // self.chunk_size
            if len(self.book.records) % self.chunk_size:
                chunks_left += 1
            print(f"{self.chunk_number}/{chunks_left}")
        except StopIteration:
            return True

    @staticmethod
    def do_q(_):
        """EXIT"""
        print("FINISHED")
        return True

    do_EOF = do_q


if __name__ == "__main__":
    MainShell().cmdloop()
    sys.exit(0)
