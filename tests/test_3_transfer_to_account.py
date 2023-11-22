import pytest

def test_transfer_to_account():
    # Проверь переход по клику на «Личный кабинет».
    from selenium.webdriver.common.by import By
    from selenium import webdriver

    driver = webdriver.Chrome()

    # Переход с главной в ЛК
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()

    # Проверка нахождения на странице перехода по клику на «Личный кабинет».
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    driver.quit()
