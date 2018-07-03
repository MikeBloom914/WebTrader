#!/usr/bin/env python3

import time

from flask import Flask, redirect, render_template, request, session, url_for

import model


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        submitted_username = request.form['username']
        submitted_password = request.form['password']
        if submitted_username and submitted_password:
            import sqlite3
            connection = sqlite3.connect('master.db', check_same_thread=False)
            cursor = connection.cursor()
            cursor.execute('SELECT username FROM users WHERE username=?;', (submitted_username,))
            objectified_username = cursor.fetchall()
            if len(objectified_username) == 0:
                return render_template('login.html', message='BAD CREDENTIALS...Please try again')

            else:
                objectified_username = objectified_username[0][0]
                cursor.execute('SELECT password FROM users WHERE username=?;', (submitted_username,))
                objectified_password = cursor.fetchall()[0][0]
                if submitted_password == objectified_password:
                    import sqlite3
                    connection = sqlite3.connect('master.db', check_same_thread=False)
                    cursor = connection.cursor()
                    cursor.execute('SELECT pk FROM users WHERE username=?;', (submitted_username,))
                    session['guid'] = cursor.fetchall()[0][0]
                    return redirect(url_for('homepage'))
                else:
                    return render_template('login.html', message='BAD CREDENTIALS...Please try again')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'GET':
        return render_template('registration.html')
    else:
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        username = request.form['username']
        password = request.form['password']
        balance = float(100000)
        x = model.registration(firstname, lastname, username, password, balance)
        return render_template('login.html')


@app.route('/homepage', methods=['GET', 'POST'])
def homepage():
    if request.method == 'GET':
        return render_template('homepage.html')
    else:
        return render_template('homepage.html')


@app.route('/buy', methods=['GET', 'POST'])
def buy():
    if request.method == 'GET':
        return render_template('buy.html')
    else:
        ticker_symbol = request.form['thingone']
        trade_volume = request.form['thingtwo']
        x = model.buy(ticker_symbol, trade_volume, session['guid'])
        return render_template('buy.html', message=x)


@app.route('/sell', methods=['GET', 'POST'])
def sell():
    if request.method == 'GET':
        return render_template('sell.html')
    else:
        ticker_symbol = request.form['sellone']
        trade_volume = request.form['selltwo']
        x = model.sell(ticker_symbol, trade_volume, session['guid'])
        return render_template('sell.html', message=x)


@app.route('/lookup', methods=['GET', 'POST'])
def lookup():
    if request.method == 'GET':
        return render_template('lookup.html')
    else:
        company_name = request.form['coname']
        x = model.lookup(company_name)
        return render_template('lookup.html', message=x)


@app.route('/quote', methods=['GET', 'POST'])
def quote():
    if request.method == 'GET':
        return render_template('quote.html')
    else:
        ticker_symbol = request.form['copsymb']
        x = model.quote(ticker_symbol)
        return render_template('quote.html', message=x)


@app.route('/portfolio', methods=['GET'])
def portfolio():
    x = model.portfolio(session['guid'])
    return render_template('portfolio.html', message=x)


@app.route('/pl', methods=['GET'])
def pl():
    x = model.pl(session['guid'])
    return render_template('pl.html', message=x)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5500, debug=True)
