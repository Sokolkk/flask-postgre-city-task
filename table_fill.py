import random
import psycopg2
from faker import Faker

# Параметры подключения к базе данных
db_params = {
    'dbname': 'medieval_city_db',
    'user': 'admin',
    'password': '123456',
    'host': 'localhost',
    'port': '5432'
}

# Создайте экземпляр Faker для генерации фиктивных данных
fake = Faker()

# Список возможных социальных статусов
social_statuses = ['King', 'baron', 'knight', 'peasant']

def generate_random_citizen():
    first_name = fake.first_name()
    last_name = fake.last_name()
    age = random.randint(18, 80)
    social_status = random.choice(social_statuses)
    monthly_income = random.randint(100, 5000)
    return (first_name, last_name, age, social_status, monthly_income)

def fill_database():
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    # Заполнение таблицы "citizens"
    for _ in range(500):
        citizen_data = generate_random_citizen()
        query = "INSERT INTO citizens (first_name, last_name, age, social_status, monthly_income) VALUES (%s, %s, %s, %s, %s);"
        cursor.execute(query, citizen_data)

    # Заполнение таблицы "hierarchy"
    for i in range(2, 500+1):
        superior_id = random.randint(1, i-1)
        subordinate_id = i
        query = "INSERT INTO hierarchy (superior_id, subordinate_id) VALUES (%s, %s);"
        cursor.execute(query, (superior_id, subordinate_id))

    connection.commit()
    connection.close()

if __name__ == "__main__":
    fill_database()
    print("База данных успешно заполнена.")
