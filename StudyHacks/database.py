import sqlite3

def add_data(data):
    print(data)
    with sqlite3.connect('data.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_data (
                username TEXT,
                quiz_name TEXT,
                order_num TEXT,
                question TEXT,
                answer TEXT
            )
        ''')
        print("ADDING DATA TO TABLE" + data['username'])
        cursor.execute('''
            INSERT INTO user_data (username, quiz_name, order_num, question, answer)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            data['username'],
            data['quiz_name'],
            data['order_num'],
            data['question'],
            data['answer']
        ))
        conn.commit()
        cursor.execute('SELECT * FROM user_data')
        rows = cursor.fetchall()
        for row in rows:
            print(row)

def get_data(username, quiz_name):
    with sqlite3.connect('data.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT order_num, question, answer FROM user_data
            WHERE username = ? AND quiz_name = ?
        ''', (username, quiz_name))
        rows = cursor.fetchall()
        print(rows)
        if rows:
            return [list(row) for row in rows]
        else:
            return None