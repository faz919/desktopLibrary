import sqlite3 

def connect():
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute(
        "Create Table If NOT EXISTS books (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("insert into books values (Null,?,?,?,?)", (title, author, year, isbn))
    conn.commit()
    conn.close()

def search(title = "", author = "", year = "", isbn = ""):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("Select * from books where title=? or author=? or year=? or isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("delete from books where id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("update books set title=?,author=?,year=?,isbn=? where id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("Select * from books")
    rows = cur.fetchall()
    conn.close()
    return rows 

# connect()
# insert("the best book ever", "faz", "2020", "12387483274")
# insert("book number two","putin","1831","23982398") 
  
# i=0
# while i < len(view()): wrong
#     print(view()[i]) 
#     i = i + 1

# i=0
# for i in range(len(view())): close but still wrong
#     print(view()[i]) 

# for x in view()[-2:]: correct, also specifies last two books in series
#     print(x)

# for i in range(1,5):
#     print('*' * i)

# for i in range(1,5):
#     for j in range(i):
#         print('*', end="")
#     print("\n")

# update(1, "yo","danesh","1950","198498324")
# delete(6)