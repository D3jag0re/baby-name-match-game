import sqlite3

def initialize_db():
    conn = sqlite3.connect('baby_names.db')
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS names
                 (id INTEGER PRIMARY KEY, name TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS responses
                 (id INTEGER PRIMARY KEY, user_id INTEGER, name_id INTEGER, response TEXT)''')
    
    names = ['Emma', 'Liam', 'Noah', 'Olivia', 'Ava']
    c.executemany('INSERT INTO names (name) VALUES (?)', [(name,) for name in names])
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_db()
