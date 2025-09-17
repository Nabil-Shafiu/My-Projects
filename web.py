#!/usr/bin/env python3
# encoding: utf-8

'''this progrma calls the login.html file and
 compared what the user input to what is here'''

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

USERNAME = 'madara'
PASSWORD = 'pass'


@app.route('/')
def home():
    return render_template('login.html')


@app.route("/login", methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if USERNAME == username and PASSWORD == password:
        return redirect(url_for('success'))
    else:
        return "Invalid username or password. <a href='/'>Try</a>"


@app.route('/success')
def success():
    return "Login sucessfully! Welcome!"


if __name__ == "__main__":
    app.run(debug=True)
