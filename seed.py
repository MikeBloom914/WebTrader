#!/usr/bin/env python3

import sqlite3


connection = sqlite3.connect('master.db', check_same_thread=False)
cursor = connection.cursor()

cursor.execute(
    """INSERT INTO users(
        firstname,
        lastname,
        email,
        password,
        balance
    ) VALUES(
        'firstname',
        'lastname',
        'Shecky914',
        'swordfish',
        100000.00
    );"""
)


connection.commit()
cursor.close()
connection.close()
