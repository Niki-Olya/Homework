# Создаём суперкласс.
class SuperClass(object):

    # Конструктор суперкласса.
    def __init__(self, num):
        self.num = num

    # Метод суперкласса.
    def get_num(self):
        print(self.num)


# Создаем подкласс.
class SubClass(SuperClass):

    # Конструктор подкласса.
    def __init__(self, num):
        # Вызываем конструктор суперкласса.
        super().__init__(num)
        print('Экземпляр создан!')


# Создаем 1-й экземпляр подкласса.
obj_1 = SubClass(4)

# Выводим значение атрибута.
print(obj_1.num)

# Создаем 2-й экземпляр подкласса.
obj_2 = SubClass(5)

# Выводим значение атрибута.
obj_1.get_num()
