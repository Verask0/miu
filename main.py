class Table:
  def __init__(self):
      self.data = []

  def add_row(self, row):
      self.data.append(row)

  def load_from_dicts(self, *dicts):
    for d in dicts:
        self.add_row(d)

  def load_from_file(self, filename):
      with open(filename, 'r') as file:
          lines = file.readlines()
          headers = lines[0].strip().split(',')
          for line in lines[1:]:
              row_values = line.strip().split(',')
              row = dict(zip(headers, row_values))
              self.add_row(row)

  def __str__(self):
      if not self.data:
          return "False"
      columns = list(self.data[0].keys())
      max_column_widths = {column: len(column) for column in columns}
      for row in self.data:
          for column, value in row.items():
              max_column_widths[column] = max(max_column_widths[column], len(str(value)))
      table_str = ""
      for column in columns:
          table_str += column.ljust(max_column_widths[column] + 2)
      table_str += "\n"
      for row in self.data:
          for column, width in max_column_widths.items():
              table_str += str(row.get(column, "")).ljust(width + 2)
          table_str += "\n"
      return table_str

# Пример использования:
fLine = {"a": 2, "b": 5}
sLine = {"a": 3, "b": 9}

table = Table()
table.add_row(fLine)
table.add_row(sLine)

print(table)

table_from_file=Table()
table_from_file.load_from_file("table.csv")
print(table_from_file)


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
# fLine = {"a" : 2, "b" : 4}
# sLine = {"a" : 3, "b" : 9}

# Результат при выводе таблицы
# а  b
# 2  4
# 3  9

#d = {"cat": "meow", "dog": "woof"}
#print (d["cat"])

#from tabulate import tabulate
#d = {"cat": "meow", "dog": "woof"}
#print(tabulate(d.items(), headers=['key', 'value'],tablefmt='grid'))
