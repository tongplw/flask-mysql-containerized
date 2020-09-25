from flask import Flask
import sqlalchemy


app = Flask(__name__)

DB_URI = "mysql+pymysql://user:password@flask_mysql_containerized_sql_1:3306/database"
db = sqlalchemy.create_engine(DB_URI)

def add(text):
    cmd = f"INSERT INTO `database.text` (text) VALUES ('{text}');"
    with db.connect() as conn:
        conn.execute(cmd)

def fetch():
    cmd = f'SELECT text FROM `database.text`'
    with db.connect() as conn:
        result = conn.execute(cmd)
        return result.fetchall()
    
@app.route('/')
def hello_world():
    return fetch()


if __name__ == '__main__':
    app.run(debug=True)
