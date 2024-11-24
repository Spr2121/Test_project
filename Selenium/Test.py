from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка драйвера
driver = webdriver.Chrome()
try:
    # Открываем браузер и переходим на страницу
    driver.get("http://127.0.0.1:5000/login")

    # Ждём появления поля username
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )

    # Вводим "1" в поле username
    username_field = driver.find_element(By.NAME, "username")
    username_field.clear()  # Очистка поля на случай, если в нём уже есть данные
    username_field.send_keys("1")

    # Вводим "1" в поле password
    password_field = driver.find_element(By.NAME, "password")
    password_field.clear()
    password_field.send_keys("1")

    # Нажимаем кнопку Login
    login_button = driver.find_element(By.XPATH, "//button[text()='Login']")
    login_button.click()

    # Ожидание перехода на следующую страницу или проверки результата
    WebDriverWait(driver, 10).until(
        EC.url_changes("http://127.0.0.1:5000/login")
    )
    print("Тест выполнен успешно")

finally:
    # Закрываем браузер
    driver.quit()
