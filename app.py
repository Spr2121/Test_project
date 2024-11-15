import logging
from logging import FileHandler
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from db import get_db_connection

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Настроим логирование в файл
if not app.debug:
    file_handler = FileHandler('app.log')
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        app.logger.info(f'Login attempt with username: {username}')  # Логируем попытку логина

        # Получаем соединение с БД
        db = get_db_connection()
        cursor = db.cursor()

        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()

        if user and check_password_hash(user[2], password):
            app.logger.info(f'Login successful for user: {username}')
            db.close()
            return redirect(url_for('success'))
        else:
            app.logger.warning(f'Invalid login attempt for user: {username}')
            db.close()
            flash("Invalid username or password", 'error')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Получаем соединение с БД
        db = get_db_connection()
        cursor = db.cursor()

        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        if cursor.fetchone():
            app.logger.warning(f'Username already exists: {username}')
            flash("Username already exists", 'error')
            db.close()
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password)
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
        db.commit()

        app.logger.info(f'User {username} registered successfully')
        db.close()
        flash("Registration successful, please login", 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
