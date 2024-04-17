class Table:
    # метод-конструктор
    def __init__(self):
        self.field = []
        self.col_names = []

    # метод, который добавляет строки в наш объект
    def create_row(self, d):
        self.col_names.append(d.keys())
        self.field.append(d)


# как создать экземпляр по классу?
table1 = Table()
print(table1.field)
d = {"cat": "meow", "dog": "woof"}
table1.create_row(d)
print(table1.field, table1.col_names)

# Вариант 2
# Формат csv - универсальный формат таблицы.
# В Python c помощью DictWritter мы можем записывать в таблицу строки как словари.
# Необходимо создать аналогичный класс таблицы.

# Требования к классу:
# 1. каждый экземпляр должен быть самостоятельным объектом,
# 2. при выводе экземпляра в консоль будет выведена вся таблица,
# 3. пустые таблицы – это False,
# 4. таблицу можно создать из файла или из словарей,
# 5. колонки таблицы можно складывать

#  Пример
# Даны словари в качестве строк
fLine = {"a" : 2, "b" : 4}
sLine = {"a" : 3, "b" : 9}

# Результат при выводе таблицы
# а  b
# 2  4
# 3  9

#d = {"cat": "meow", "dog": "woof"}
#print (d["cat"])

#from tabulate import tabulate
#d = {"cat": "meow", "dog": "woof"}
#print(tabulate(d.items(), headers=['key', 'value'],tablefmt='grid'))
