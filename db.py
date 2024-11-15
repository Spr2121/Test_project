import mysql.connector

def get_db_connection():
    db = mysql.connector.connect(
        host="localhost",
        user="root",  # Ваш пользователь
        password="123456789",  # Ваш пароль
        database="test_db"
    )
    return db
