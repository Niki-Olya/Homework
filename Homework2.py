# Задача 1. Напишите программу с классом Student, в котором есть три атрибута: name,
# groupNumber и age. По умолчанию name = Ivan, age = 18, groupNumber = 10A.
# Необходимо создать пять методов: getName, getAge, getGroupNumber, setNameAge,
# setGroupNumber. Метод getName нужен для получения данных об имени конкретного
# студента, метод getAge нужен для получения данных о возрасте конкретного студента,
# vетод setGroupNumberнужен для получения данных о номере группы конкретного
# студента. Метод SetNameAge позволяет изменить данные атрибутов установленных
# по умолчанию, метод setGroupNumber позволяет изменить номер группы
# установленный по умолчанию. В программе необходимо создать пять экземпляров
# класса Student, установить им разные имена, возраст и номер группы
print("\nЗадание 1:")


class Student:
    def __init__(self, name="Ivan", groupNumber=18, age="10A"):
        self.name = name
        self.groupNumber = groupNumber
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGroupNumber(self):
        return self.groupNumber

    def setNameAge(self, name, age):
        self.name = name
        self.age = age

    def setGroupNumber(self, groupNumber):
        self.groupNumber = groupNumber


stud1 = Student("Alex", 17, "9A")

stud2 = Student("Billy", 18)
stud2.setGroupNumber("10B")

stud3 = Student()
stud3.setNameAge("Charlie", 19)
stud3.setGroupNumber("11C")

stud4 = Student("Daniel", 20, "12D")
stud5 = Student("Emily", 21, "13E")

print(str(stud1.getName()) + ", " + str(stud1.getAge()) + ", " + str(stud1.getGroupNumber()))
print(str(stud2.getName()) + ", " + str(stud2.getAge()) + ", " + str(stud2.getGroupNumber()))
print(str(stud3.getName()) + ", " + str(stud3.getAge()) + ", " + str(stud3.getGroupNumber()))
print(str(stud4.getName()) + ", " + str(stud4.getAge()) + ", " + str(stud4.getGroupNumber()))
print(str(stud5.getName()) + ", " + str(stud5.getAge()) + ", " + str(stud5.getGroupNumber()))

# Задача 2. Напишите программу с классом Math. Создайте два атрибута — a и b.
# Напишите методы addition — сложение, multiplication — умножение, division —
# деление, subtraction — вычитание. При передаче в методы параметров a и b с ними
# нужно производить соответствующие действия и печатать ответ.
print("\nЗадание 2:")


class Math:
    @staticmethod
    def addition(a, b):
        print(a + b)

    @staticmethod
    def substraction(a, b):
        print(a - b)

    @staticmethod
    def multiplication(a, b):
        print(a * b)

    @staticmethod
    def division(a, b):
        print(a / b)


Math.addition(4, 33)

# Задача 3. Напишите программу с классом Car. Создайте конструктор класса Car.
# Создайте атрибуты класса Car — color (цвет), type (тип), year (год). Напишите пять
# методов. Первый — запуск автомобиля, при его вызове выводится сообщение
# «Автомобиль заведен». Второй — отключение автомобиля — выводит сообщение
# «Автомобиль заглушен». Третий — присвоение автомобилю года выпуска. Четвертый
# метод — присвоение автомобилю типа. Пятый — присвоение автомобилю цвета
print("\nЗадание 3:")


class Car:
    def __init__(self, color="white", type="sedan", year=2000):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print("Автомобиль заведен")

    def stop(self):
        print("Автомобиль заглушен")

    def setYear(self, year):
        self.year = year

    def setType(self, type):
        self.type = type

    def setColor(self, color):
        self.color = color

car1 = Car()
car1.setYear(1999)
car1.setColor("green")
car1.setType("roadster")

car1.start()
car1.stop()