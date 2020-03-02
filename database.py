import sqlite3

conn = sqlite3.connect('attendance.db')

sql_query = """
CREATE TABLE IF NOT EXISTS attendance (
  name text,
  date_time text
);
"""

conn.execute(sql_query)
conn.close()