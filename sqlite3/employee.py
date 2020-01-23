import sqlite3, sys, re

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

class Employee:
    def __init__(self):
        cursor.execute("CREATE TABLE IF NOT EXISTS employees(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name text, salary real, department text, position text, hireDate text)")
        conn.commit()

    def add(self, row):
        conn.execute('''INSERT INTO employees(name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?)''', row)
        conn.commit()

    def all(self):
        for i in conn.execute('''SELECT * FROM employees'''):
            print(i)

    def getById(self, id):
        for i in cursor.execute('''SELECT * FROM employees WHERE id = ?''', [(id)]):
            print(i)

    def update(self, data):
        sql = """UPDATE employees SET name = ?, salary = ?, department = ?, position = ?, hireDate = ? WHERE id = ?"""
        conn.execute(sql, data)
        conn.commit()
        print(data)


emp = Employee()

if len(sys.argv) > 1:
    key = sys.argv[1]
else:
    key = input('Please inter key from add, all: ')

if key=='all':
    emp.all()
elif key=='get':
    id = int(input('Enter id employee: '))
    emp.getById(id)
elif key=='update':
    name = input('Enter name: ')
    salary = input('Enter salary: ')
    departament = input('Enter departament: ')
    position = input('Enter position: ')
    hireDate = input('Enter hireDate: ')
    id = int(input('Enter id employee: '))
    emp.update((name, salary, departament, position, hireDate, id))
else:
    print('Add employee:')
    name = input('Enter name: ')
    salary = input('Enter salary: ')
    departament = input('Enter departament: ')
    position = input('Enter position: ')
    hireDate = input('Enter hireDate: ')
    emp.add((name, salary, departament, position, hireDate))



conn.close()    
