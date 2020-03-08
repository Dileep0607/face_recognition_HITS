import sqlite3

def execute_query(sql_query):
    """
    function to execute sql commands
    :return: returns values if select command used
    """
    # print(sql_query)
    with sqlite3.connect("attendance.db") as con:
        cur = con.cursor()
        result = cur.execute(sql_query)
        con.commit()
    return result

def add_item(text):

    sql_query = """insert into attendance(name,date_time) VALUES ( '%s',datetime('now','localtime') )""" % (text)
    execute_query(sql_query)

def get_item():

    sql_query = """select * from attendance"""
    return execute_query(sql_query).fetchall()

