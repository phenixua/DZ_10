from collections import UserDict

# Оголошуємо базовий клас для полів
class Field:
    def __init__(self, value):
        self.value = value

# Клас для зберігання телефонних номерів, успадкований від Field
class Phone(Field):
    pass

# Клас для зберігання імен, успадкований від Field
class Name(Field):
    pass

# Клас для представлення запису в адресній книзі
class Record:
    def __init__(self, name: Name, phones: list, emails: list=None):
        self.name = name
        self.phones = phones if phones else []  # Список телефонних номерів
        self.emails = emails if emails else []  # Список електронних адрес

    # Метод для додавання телефонного номеру до запису
    def add_phone(self, phone):
        phone_number = Phone(phone)
        if phone_number not in self.phones:
            self.phones.append(phone_number)

    # Метод для видалення телефонного номеру з запису
    def delete_phone(self, phone):
        new_phones = []
        for p in self.phones:
            if p.value != phone:
                new_phones.append(p)
        self.phones = new_phones


    # Метод для редагування телефонного номеру
    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                break

# Клас для представлення адресної книги, успадкований від UserDict
class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find_record(self, value):
        return self.data.get(value)

# Тестування класів
if __name__ == "__main__":
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, [phone])  
    ab = AddressBook()
    ab.add_record(rec)  

    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'

    print('All Ok)')

