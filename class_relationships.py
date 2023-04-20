# practice for understanding inheritance in classes

class Person:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


class Student(Person):
    def __init__(self, name, phone, email, address, s_number, av_mark):
        super().__init__(name, phone, email, address)
        self.s_number = s_number
        self.av_mark = av_mark


class Professor(Person):
    def __init__(self, name, phone, email, address, salary, s_number, yos, class_count):
        super().__init__(name, phone, email, address)
        self.salary = salary
        self.s_number = s_number
        self.yos = yos
        self.class_count = class_count


class Address:
    def __init__(self, street, city, state, postal, country):
        self.street = street
        self.city = city
        self.state = state
        self.postal = postal
        self.country = country


Person.address = Address("Taranaki", "Wellington", "Te Aro", "6011", "New Zealand")
p1 = Person("Leonard", "0276866141", "Leno@hotmail.co.nz", Address)
