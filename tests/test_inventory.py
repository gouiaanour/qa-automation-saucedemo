from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_inventory_title(driver):

    login = LoginPage(driver)

    login.login(
        "standard_user",
        "secret_sauce"
    )


    inventory = InventoryPage(driver)


    assert inventory.get_title() == "Products"