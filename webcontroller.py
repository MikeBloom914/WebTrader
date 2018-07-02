#!/usr/bin/env python3

import time

from flask import Flask, redirect, render_template, request, url_for

import model


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        email = request.form['email']
        password = request.form['password']

        if email != 'mikebloom914@gmail.com' or password != 'swordfish':
            return render_template('login.html', message='BAD CREDENTIALS...Please try again')
        else:
            return redirect(url_for('homepage'))


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
        x = model.buy(ticker_symbol, trade_volume)
        return render_template('buy.html', message=x)


@app.route('/sell', methods=['GET', 'POST'])
def sell():
    if request.method == 'GET':
        return render_template('sell.html')
    else:
        ticker_symbol = request.form['sellone']
        trade_volume = request.form['selltwo']
        x = model.sell(ticker_symbol, trade_volume)
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
    x = model.portfolio()
    return render_template('portfolio.html', message=x)


@app.route('/pl', methods=['GET'])
def pl():
    x = model.pl()
    return render_template('pl.html', message=x)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5500, debug=True)
