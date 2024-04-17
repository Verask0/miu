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