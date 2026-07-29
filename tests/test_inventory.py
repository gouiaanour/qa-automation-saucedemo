from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_inventory_title(driver):

    login = LoginPage(driver)

    login.login(
        "standard_user",
        "secret_sauce"
    )

    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory.html")
    )

    inventory = InventoryPage(driver)

    assert inventory.get_title() == "Products"

    time.sleep(5)


def test_products_count(driver):

    login = LoginPage(driver)

    login.login(
        "standard_user",
        "secret_sauce"
    )

    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory.html")
    )

    inventory = InventoryPage(driver)

    print("\nNombre de produits :", inventory.get_products_count())

    print("\nListe des produits :")

    for product in inventory.get_product_names():
        print("-", product)

    assert inventory.get_products_count() == 6

    time.sleep(5)