# Contains functions to interact with db
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('baby_names.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_names():
    conn = get_db_connection()
    names = conn.execute('SELECT * FROM names').fetchall()
    conn.close()
    return names

def record_response(user_id, name_id, response):
    conn = get_db_connection()
    conn.execute('INSERT INTO responses (user_id, name_id, response) VALUES (?, ?, ?)', 
                 (user_id, name_id, response))
    conn.commit()
    conn.close()

def get_common_names():
    conn = get_db_connection()
    query = '''
        SELECT n.name 
        FROM responses r1
        JOIN responses r2 ON r1.name_id = r2.name_id
        JOIN names n ON n.id = r1.name_id
        WHERE r1.user_id = 1 AND r2.user_id = 2 
          AND ((r1.response = 'yes' OR r1.response = 'maybe') 
          AND (r2.response = 'yes' OR r2.response = 'maybe'))
    '''
    common_names = conn.execute(query).fetchall()
    conn.close()
    return common_names

def reset_db():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('DROP TABLE IF EXISTS names')
    c.execute('DROP TABLE IF EXISTS responses')
    c.execute('''CREATE TABLE names (id INTEGER PRIMARY KEY, name TEXT)''')
    c.execute('''CREATE TABLE responses (id INTEGER PRIMARY KEY, user_id INTEGER, name_id INTEGER, response TEXT)''')
    
    # Insert initial data
    names = ['Emma', 'Liam', 'Noah', 'Olivia', 'Ava']
    c.executemany('INSERT INTO names (name) VALUES (?)', [(name,) for name in names])
    
    conn.commit()
    conn.close()

