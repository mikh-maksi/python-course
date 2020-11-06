from collections import UserDict


class AddressBook(UserDict):
    def __str__(self):
        result = ""
        for id_, record in self.data.items():
            result += f"{id_}:\n{20*'='}\n{str(record)}\n"
        return result

    def add(self, record):
        self.data[record.name.value] = record


class Record:
    def __init__(self, name, *phones):
        self.name = name
        self.key = None
        self.phones = []
        for phone in phones:
            self.phones.append(phone)

    def __str__(self):
        result = str(self.name)
        for idx, phone in enumerate(self.phones):
            result += f"\n{idx}{phone}"
        return result


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{self.__class__.__name__}: {self.value}"


class Name(Field):
    pass


class Phone(Field):
    pass
