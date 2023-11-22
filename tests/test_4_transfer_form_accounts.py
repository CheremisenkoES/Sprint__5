import pytest

def test_transfer_from_construct(email_pretty,password_pretty):
    # Переход из ЛК в Конструктор
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    driver = webdriver.Chrome()
    # Вход на сайт
    driver.get("https://stellarburgers.nomoreparties.site/login")

    # Авторизация
    driver.find_element(By.NAME, "name").click()
    driver.find_element(By.NAME, "name").send_keys(email_pretty)

    driver.find_element(By.NAME, "Пароль").click()
    driver.find_element(By.NAME, "Пароль").send_keys(email_pretty)

    driver.find_element(By.CSS_SELECTOR, ".button_button__33qZ0").click()

    # Переход в ЛК
    driver.find_element(By.CSS_SELECTOR,
                        ".AppHeader_header__link__3D_hX:nth-child(3) > .AppHeader_header__linkText__3q_va").click()

    # Переход из ЛК в Конструктор
    driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) .AppHeader_header__linkText__3q_va").click()

    # Проверка нахождения на странице после перехода в конструктор
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    driver.quit()

def test_transfer_from_logo(email_pretty, password_pretty):
    # Переход из ЛК  по логотипу Stellar Burgers.
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    driver = webdriver.Chrome()
    # Вход на сайт

    driver.get("https://stellarburgers.nomoreparties.site/login")

    # Авторизация
    driver.find_element(By.NAME, "name").click()
    driver.find_element(By.NAME, "name").send_keys(email_pretty)

    driver.find_element(By.NAME, "Пароль").click()
    driver.find_element(By.NAME, "Пароль").send_keys(password_pretty)

    driver.find_element(By.CSS_SELECTOR, ".button_button__33qZ0").click()

    # Переход в ЛК
    driver.find_element(By.CSS_SELECTOR,
                        ".AppHeader_header__link__3D_hX:nth-child(3) > .AppHeader_header__linkText__3q_va").click()

    # Переход из ЛК по ЛОГО
    driver.find_element(By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2 svg").click()
    # Проверка нахождения на странице после перехода по логотипу
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    driver.quit()
