from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def test_login_valide(driver):
    page = LoginPage(driver)
    page.login("standard_user", "secret_sauce")
    url = driver.current_url
    WebDriverWait(driver, 10).until(
    EC.url_contains ("inventory.html"))
    assert "inventory.html" in url
    time.sleep(5)

def test_login_invalide(driver):
    page = LoginPage(driver)
    page.login("standard_user", "secraisuse")
    WebDriverWait(driver,10).until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR,"[data-test='error']")))
    error = page.get_error_message()
    assert "password" in error

def test_login_username_empty(driver):
    page = LoginPage(driver)
    page.login("", "secret_sauce")
    WebDriverWait(driver,10).until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR,"[data-test='error']")))
    error = page.get_error_message()
    assert "Username" in error

def test_login_password_empty(driver):
    page = LoginPage(driver)
    page.login("standard_user", "")
    WebDriverWait(driver,10).until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR,"[data-test='error']")))
    error = page.get_error_message()
    assert "Password" in error