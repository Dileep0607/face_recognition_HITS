import sqlite3

conn = sqlite3.connect('students.db')

sql_query = """
CREATE TABLE IF NOT EXISTS students (
  name text
);
"""

conn.execute(sql_query)
conn.close()