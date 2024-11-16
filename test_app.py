import pytest
from app import app

# Фикстура для тестирования Flask-приложения
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Тест главной страницы (перенаправление на login)
def test_home_redirect(client):
    response = client.get('/')
    assert response.status_code == 302  # Проверяем, что происходит перенаправление
    assert response.location.endswith('/login')  # Проверяем правильность URL

# Тест страницы логина
def test_login_page(client):
    response = client.get('/login')
    assert response.status_code == 200  # Проверяем, что страница доступна
    assert b"Login" in response.data  # Проверяем, что на странице есть слово "Login"

# Тест логина с правильными данными
#def test_valid_login(client):
    # Отправляем POST-запрос с правильными данными
    #response = client.post('/login', data={'username': 'testuser', 'password': 'testpassword'})
    #assert response.status_code == 302  # Должно быть перенаправление
    #assert response.location.endswith('/success')  # Должен быть редирект на success

# Тест логина с неправильным паролем
#def test_invalid_login(client):
    #response = client.post('/login', data={'username': 'testuser', 'password': 'wrongpassword'})
    #assert response.status_code == 302  # Должно быть перенаправление
    #assert b"Invalid username or password" in response.data  # Проверка наличия ошибки на странице

# Тест регистрации с новым пользователем
#def test_register(client):
    #response = client.post('/register', data={'username': 'newuser', 'password': 'newpassword'})
    #assert response.status_code == 302  # Перенаправление после регистрации
    #assert response.location.endswith('/login')  # Должен быть редирект на страницу логина

# Тест, если пользователь пытается зарегистрироваться с уже существующим именем
#def test_register_existing_user(client):
    #response = client.post('/register', data={'username': 'testuser', 'password': 'newpassword'})
    #assert b"Username already exists" in response.data  # Проверка, что отображается сообщение о существующем пользователе
