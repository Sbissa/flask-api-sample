import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

user = (1, 'jose', 'asdf')

insert_query = "INSERT INTO users VALUES (?, ? , ?)"
cursor.execute(insert_query,user)


users =[
(4, '2jose', '2asdf'),
(2, '3jose', '3asdf'),
(3, '4jose', '4asdf'),
]

cursor.executemany(insert_query, users)

select_query = 'SELECT * FROM users'
for row in cursor.execute(select_query):
    print(row)

connection.commit()

connection.close()
