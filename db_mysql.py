#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
import pymysql
import pymysql.cursors
 
con = pymysql.connect('localhost', 'root', 
    '', 'book_test', charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)
 
with con:
    
    cur = con.cursor()
    cur.execute("SELECT * FROM autors;")
 
    autors = cur.fetchall()

    for autor in autors:
        print("ID: ", autor['id'], ", name: ", autor['fio'])
