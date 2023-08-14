from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

db_params = {
    'dbname': 'medieval_city_db',
    'user': 'admin',
    'password': '123456',
    'host': 'localhost',
    'port': '5432'
}

def connect_db():
    return psycopg2.connect(**db_params)

@app.route('/')
def index():
    connection = connect_db()
    cursor = connection.cursor()

    # SQL-запрос с использованием LEFT JOIN для получения данных с информацией о начальнике
    query = """
    SELECT c1.*, c2.first_name AS superior_first_name, c2.last_name AS superior_last_name
    FROM citizens AS c1
    LEFT JOIN citizens AS c2 ON c1.superior_id = c2.id;
    """
    cursor.execute(query)
    citizens_with_superiors = cursor.fetchall()

    connection.close()

    return render_template('index.html', citizens_with_superiors=citizens_with_superiors)

if __name__ == "__main__":
    app.run()
