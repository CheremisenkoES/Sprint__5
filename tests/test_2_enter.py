import pytest

def test_enter_button(email_pretty,password_pretty):
    # Проверь вход по кнопке «Войти в аккаунт» на главной
    from selenium.webdriver.common.by import By
    from selenium import webdriver

    driver = webdriver.Chrome()

    # Открыть сайт и войти
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.CSS_SELECTOR, ".button_button__33qZ0").click()

    # Заполнить форму
    driver.find_element(By.NAME, "name").click()
    driver.find_element(By.NAME, "name").send_keys(email_pretty)

    driver.find_element(By.NAME, "Пароль").click()
    driver.find_element(By.NAME, "Пароль").send_keys(password_pretty)

    # Войти
    driver.find_element(By.CSS_SELECTOR, ".button_button__33qZ0").click()

    # Проверка страницы после успешного входа
    assert '/stellarburgers.nomoreparties.site' in driver.current_url

    driver.quit()

def test_enter_lk(email_pretty, password_pretty):
    # Проверь вход через кнопку «Личный кабинет»
    from selenium.webdriver.common.by import By
    from selenium import webdriver

    driver = webdriver.Chrome()

    # Открыть сайт и зайти в ЛК
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()

    # Заполнить форму
    driver.find_element(By.NAME, "name").click()
    driver.find_element(By.NAME, "name").send_keys(email_pretty)

    driver.find_element(By.NAME, "Пароль").click()
    driver.find_element(By.NAME, "Пароль").send_keys(password_pretty)
    # Войти
    driver.find_element(By.CSS_SELECTOR, ".button_button__33qZ0").click()

    # Проверка страницы после успешного входа
    assert '/stellarburgers.nomoreparties.site' in driver.current_url

    driver.quit()

def test_enter_in_reg_form(email_pretty, password_pretty):
    # Проверь вход через кнопку Вход в форме регистрации
    from selenium.webdriver.common.by import By
    from selenium import webdriver

    driver = webdriver.Chrome()

    # Открыть сайт и зайти в ЛК
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(By.LINK_TEXT, "Войти").click()

    # Заполнить форму
    driver.find_element(By.NAME, "name").click()
    driver.find_element(By.NAME, "name").send_keys(email_pretty)

    driver.find_element(By.NAME, "Пароль").click()
    driver.find_element(By.NAME, "Пароль").send_keys(password_pretty)
    # Войти
    driver.find_element(By.CSS_SELECTOR, ".button_button__33qZ0").click()

    # Проверка страницы после успешного входа
    assert '/stellarburgers.nomoreparties.site' in driver.current_url

    driver.quit()

def test_enter_recover(email_pretty, password_pretty):
    # Проверь вход через кнопку в форме восстановления пароля.
    from selenium.webdriver.common.by import By
    from selenium import webdriver
    driver = webdriver.Chrome()

    # Открыть сайт и зайти в ЛК
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
    driver.find_element(By.LINK_TEXT, "Войти").click()

    # Заполнить форму
    driver.find_element(By.NAME, "name").click()
    driver.find_element(By.NAME, "name").send_keys(email_pretty)

    driver.find_element(By.NAME, "Пароль").click()
    driver.find_element(By.NAME, "Пароль").send_keys(password_pretty)
    # Войти
    driver.find_element(By.CSS_SELECTOR, ".button_button__33qZ0").click()

    # Проверка страницы после успешного входа
    assert '/stellarburgers.nomoreparties.site' in driver.current_url

    driver.quit()