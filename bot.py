from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __str__(self):
        return f"Name: {self.value}"


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        if not self.validate():
            raise ValueError("Phone number must be 10 digits long.")

    def validate(self):
        return len(str(self.value)) == 10

    def __str__(self):
        return f"Phone: {self.value}"


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)

    def edit_phone(self, old_number_phone, new_number_phone):
        try:
            Phone(new_number_phone)
        except ValueError as e:
            raise ValueError(f'New number is incorrect: {e}')

        for phone in self.phones:
            if phone.value == old_number_phone:
                phone.value = new_number_phone
                return 'Number is successfully updated'
        raise ValueError("Old number is not defined")


    def find_phone(self, phone):
        for phone in self.phones:
            if phone.value == phone:
                return phone

    def __str__(self):
        phones_info = "; ".join(str(phone) for phone in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_info}"

class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]




# Створення нової адресної книги
book = AddressBook()

    # Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
book.add_record(john_record)

    # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

    # Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

    # Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

john.edit_phone("1234567890", "1112223")


print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

    # Видалення запису Jane
book.delete("Jane")

