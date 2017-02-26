from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)
# render the home.html file
@app.route('/')
def home():
	return render_template('home.html')
# /new-friend will accept POST and gather data from the form names
@app.route('/new-friend', methods = ['POST'])
def newFriend():
	connection = sqlite3.connect('database.db')
	cursor = connection.cursor()

	name = request.form['name']
	age = request.form['age']
# try except method to commit to the friends table
	try:
		cursor.execute('INSERT INTO friends(name, age) VALUES (?,?)',(name, age))
		connection.commit()
		message = 'Succesfull inserted into table'
	except:
		connection.rollback()
		message = 'there was an issue inserting data'
	finally:
		connection.close()
		return message

#spit back the friends from sqlite3
@app.route('/friends')
def friends():
	connection = sqlite3.connect('database.db')
	cursor = connection.cursor()
	cursor.execute('SELECT * FROM friends')
	friendsList = cursor.fetchall()
	connection.close()
	return jsonify(friendsList)
#app run so you don't need to restart server
app.run(debug = True)