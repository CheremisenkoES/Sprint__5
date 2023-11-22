import pytest

def test_logout_of_account(email,password):
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    driver = webdriver.Chrome()
    # Проверь выход по кнопке «Выйти» в личном кабинете.
    # Вход на сайт
    driver.get("https://stellarburgers.nomoreparties.site/login")
    # Авторизация

    driver.find_element(By.NAME, "Пароль").click()
    driver.find_element(By.NAME, "Пароль").send_keys(password)

    driver.find_element(By.NAME, "name").click()
    driver.find_element(By.NAME, "name").send_keys(email)

    driver.find_element(By.CSS_SELECTOR, ".button_button__33qZ0").click()
    # Вход в ЛК
    driver.find_element(By.CSS_SELECTOR,
                        ".AppHeader_header__link__3D_hX:nth-child(3) > .AppHeader_header__linkText__3q_va").click()
    # Выход из аккаунта
    driver.implicitly_wait(10)

    driver.find_element(By.CSS_SELECTOR, ".Account_button__14Yp3")

    # Проверка что мы на нужной странице после выхода
    assert '/stellarburgers.nomoreparties.site' in driver.current_url

    driver.quit()