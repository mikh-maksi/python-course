import re
from collections import UserDict
from datetime import datetime


class IncorrectInput(Exception):
    pass


class AddressBook(UserDict):
    def __str__(self):
        result = ""
        for id_, record in self.data.items():
            result += f"{id_}:\n{20*'='}\n{str(record)}\n"
        return result

    def add(self, record):
        self.data[record.name.value] = record

    def iterator(self, item_number):
        counter = 0
        result = ""
        for id_, record in self.data.items():
            result += f"{id_}:\n{20 * '='}\n{str(record)}\n"
            counter += 1
            if counter >= item_number:
                yield result
                counter = 0
                result = ""


class Record:
    def __init__(self, name, *phones, birthday=None):
        self.name = name
        self.birthday: Birthday = birthday
        self.key = None
        self.phones = []
        for phone in phones:
            self.phones.append(phone)

    def __str__(self):
        result = str(self.name)
        for idx, phone in enumerate(self.phones):
            result += f"\n{idx}{phone}"
        return result

    def days_to_birthday(self):
        if not self.birthday:
            return
        now = datetime.today()
        if (self.birthday.value.replace(year=now.year) - now).days > 0:
            return (self.birthday.value.replace(year=now.year) - now).days
        return (self.birthday.value.replace(year=now.year+1) - now).days


class Field:
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def __str__(self):
        return f"{self.__class__.__name__}: {self.value}"


class Name(Field):
    pass


class Phone(Field):
    PHONE_REGEX = re.compile(r"^\+?(\d{2})?\(?(0\d{2})\)?(\d{7}$)")

    def __init__(self, value):
        super().__init__(value)
        self.country_code: str = ""
        self.operator_code: str = ""
        self.phone_number: str = ""

    @Field.value.setter
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
        self.__value = f"+{self.country_code}({self.operator_code}){self.phone_number}"


class Birthday(Field):
    @Field.value.setter
    def value(self, value: str):
        self.__value = datetime.strptime(value, '%d%m%Y').date()
