import sys, sqlite3

conn = sqlite3.connect('test.db')

class DB:
    
    def add(self, lists):
        for i in lists:
            conn.execute("""INSERT INTO test(`title`) VALUES(?)""", [(i)])
            conn.commit()
            print(f'Add row - {i}')

    def all(self):
        for i in conn.execute("""SELECT * FROM test"""):
            print(i)

    def oneById(self, id):
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM test WHERE id = ?""", [(id)])
        print(cursor.fetchone())



db = DB()

if len(sys.argv) > 1:
    a = sys.argv[1]
else:
    a = input("all - read data, add - added or get - find row by id: ")

if a == 'all':
    db.all()
elif a == 'get':
    if len(sys.argv) > 2:
        db.oneById(int(sys.argv[2]))
    else:
        db.oneById(int(input('Enter id: ')))
else:
    if len(sys.argv) > 2:
        lists = sys.argv[2]
    else:
        lists = input("List throught comma: ")
    db.add(lists.split(', '))
