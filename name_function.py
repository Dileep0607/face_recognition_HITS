import sqlite3

def execute_query(sql_query):
    """
    function to execute sql commands
    :return: returns values if select command used
    """
    # print(sql_query)
    with sqlite3.connect("students.db") as con:
        cur = con.cursor()
        result = cur.execute(sql_query)
        con.commit()
    return result

def add_student(text):

    sql_query = """insert into students(name) VALUES ( '%s')""" % (text)
    execute_query(sql_query)

def get_student():

    sql_query = """select * from students"""
    return execute_query(sql_query).fetchall()