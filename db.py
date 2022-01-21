import sqlite3
 
conn = sqlite3.connect("book.db")
cursor = conn.cursor()
def search_tl(title):
    print("\n(№, Наименование, Имя автора, Отчество автора, Фамилия автора, Издательство):")
    for row in cursor.execute(f"SELECT rowid, * FROM books WHERE title='{title}'"):
        print(row)

def search_fn(first_name):
    print("\n(№, Наименование, Имя автора, Отчество автора, Фамилия автора, Издательство):")
    for row in cursor.execute(f"SELECT rowid, * FROM books WHERE author_first_name='{first_name}'"):
        print(row)

def search_mn(middle_name):
    print("\n(№, Наименование, Имя автора, Отчество автора, Фамилия автора, Издательство):")
    for row in cursor.execute(f"SELECT rowid, * FROM books WHERE author_middle_name='{middle_name}'"):
        print(row)

def search_ln(last_name):
    print("\n(№, Наименование, Имя автора, Отчество автора, Фамилия автора, Издательство):")
    for row in cursor.execute(f"SELECT rowid, * FROM books WHERE author_last_name='{last_name}'"):
        print(row)

def search_pb(publisher):
    print("\n(№, Наименование, Имя автора, Отчество автора, Фамилия автора, Издательство):")
    for row in cursor.execute(f"SELECT rowid, * FROM books WHERE publisher='{publisher}'"):
        print(row)

def delete(title):
    sql = f"DELETE FROM books WHERE title='{title}'"
    cursor.execute(sql)
    conn.commit()

#cursor.execute("""CREATE TABLE books
#                  (title text, author_first_name text, author_middle_name text,
#                   author_last_name text, publisher text)
#               """)

#cursor.execute("""INSERT INTO books
#                  VALUES ('Война и мир', 'Лев', 'Николаевич',
#                  'Толстой', 'АСТ')"""
#               )
#conn.commit()
#cursor.execute("""INSERT INTO books
#                  VALUES ('Капитанская дочка', 'Александр', 'Сергеевич',
#                  'Пушкин', 'АСТ')"""
#               )
#conn.commit()
#cursor.execute("""INSERT INTO books
#                  VALUES ('Евгений Онегин', 'Александр', 'Сергеевич',
#                  'Пушкин', 'АСТ')"""
#               )
#conn.commit()
i = 0
while (i != 5):
    print ("\nБД Книги")
    print ("Выберите действие:")
    print ("1) Поиск")
    print ("2) Добавление")
    print ("3) Вывод всех значений")
    print ("4) Удаление")
    print ("5) Выход")
    i = int(input())
    if i == 1:
        print ("\nВыберите данные поиска:")
        print ("1) Наименование")
        print ("2) Имя автора")
        print ("3) Отчество автора")
        print ("4) Фамилия автора")
        print ("5) Издательство")
        f = int(input())
        print ("\nВведите запрос.")
        sr = input()
        if f == 1:
            search_tl(sr)
        elif f == 2:
            search_fn(sr)
        elif f == 3:
            search_mn(sr)
        elif f == 4:
            search_ln(sr)
        elif f == 5:
            search_pb(sr)
    elif i == 2:
        print ("\nВведите наименование")
        nm = input()
        print ("Введите имя автора")
        fn = input()
        print ("Введите отчество автора")
        mn = input()
        print ("Введите фамилию автора")
        ln = input()
        print ("Введите издательство")
        pb = input()
        cursor.execute(f"""INSERT INTO books
                          VALUES ('{nm}', '{fn}', '{mn}', '{ln}', '{pb}')"""
                           )
        conn.commit()
        print ("\nКнига добавлена.")
    elif i == 3:
        print("\n(№, Наименование, Имя автора, Отчество автора, Фамилия автора, Издательство):")
        for row in cursor.execute(f"SELECT rowid, * FROM books"):
            print(row)
    elif i == 4:
        print ("\nВведите наименование книги для удаления.")
        nm = input()
        delete(nm)
        print ("\nКнига удалена.")