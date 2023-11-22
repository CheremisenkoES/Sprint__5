import pytest

def test_registration(user,password):
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    # Проверка успешной регистрации
    driver = webdriver.Chrome()

    # вход на сайт
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # заполнить форму валидными данными
    driver.find_element(By.NAME, "name").click()
    driver.find_element(By.NAME, "name").send_keys(user)

    driver.find_element(By.CSS_SELECTOR, ".Auth_fieldset__1QzWN:nth-child(2) .input").click()
    driver.find_element(By.CSS_SELECTOR, ".input_status_active > .input__textfield").send_keys(
        "evgeniy_cheremisenko_3_006@test.ru")

    driver.find_element(By.NAME, "Пароль").click()
    driver.find_element(By.NAME, "Пароль").send_keys(password)

    # отправить форму
    driver.find_element(By.CSS_SELECTOR, ".button_button__33qZ0").click()

    # переход на нужную страницу после успешной регистрации
    assert '/stellarburgers.nomoreparties.site' in driver.current_url

    # Закрой браузер
    driver.quit()

def test_name_not_empty(user):
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    # Проверка что поле Имя не пустое

    driver = webdriver.Chrome()

    # вход на сайт
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # заполнить поле Имя  данными
    driver.find_element(By.NAME, "name").click()
    driver.find_element(By.NAME, "name").send_keys(user)

    name = driver.find_element(By.NAME, "name").get_attribute("value")

    # проверка что поле не пустое
    assert name != ""

    driver.quit()

def test_email_format(email):
    import re
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    # Проверка что в поле Email введён email в формате логин@домен: например, 123@ya.ru

    driver = webdriver.Chrome()

    # вход на сайт
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # заполнить форму валидными данными
    driver.find_element(By.CSS_SELECTOR, ".Auth_fieldset__1QzWN:nth-child(2) .input").click()
    driver.find_element(By.CSS_SELECTOR, ".input_status_active > .input__textfield").send_keys("user100@asdasd.ru")

    mail = driver.find_element(By.CSS_SELECTOR, ".input_status_active > .input__textfield").get_attribute("value")

    # проверка структуры емайла
    assert re.match(r'^\S+@\S+\.\S+$', mail)


def test_min_password(email,password):
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    # Проверка что минимальный пароль — шесть символов

    driver = webdriver.Chrome()

    # вход на сайт
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # заполнить форму валидными данными

    driver.find_element(By.NAME, "Пароль").click()
    driver.find_element(By.NAME, "Пароль").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, ".input__icon path").click()

    password = driver.find_element(By.NAME, "Пароль").get_attribute("value")

    # проверка длины пароля
    assert len(password) >= 6

    driver.quit()

def test_password_error(email, user):
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    # проверить ошибку для некорректного пароля.
    driver = webdriver.Chrome()

    # вход на сайт
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # регистрация
    driver.find_element(By.NAME, "name").click()
    driver.find_element(By.NAME, "name").send_keys(user)

    driver.find_element(By.CSS_SELECTOR, ".Auth_fieldset__1QzWN:nth-child(2) .input").click()
    driver.find_element(By.CSS_SELECTOR, ".input_status_active > .input__textfield").send_keys(email)

    # ввести не пароль менее 6 символов
    driver.find_element(By.NAME, "Пароль").click()
    driver.find_element(By.NAME, "Пароль").send_keys("111")

    # отправить форму
    driver.find_element(By.CSS_SELECTOR, ".button_button__33qZ0").click()

    # получить сообщение об ошибке на длину пароля
    assert driver.find_element(By.CSS_SELECTOR, ".input__error").text == 'Некорректный пароль'

    driver.quit()