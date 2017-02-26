import sqlite3

connection = sqlite3.connect('database.db')
print 'We\'re connected!'

connection.execute('CREATE TABLE friends (name TEXT, age INTEGER)')
print 'table created!'

connection.close()