from selenium.webdriver.common.by import By


class InventoryPage:

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.find_element(
            By.CLASS_NAME,
            "title"
        ).text


    def get_products(self):
        return self.driver.find_elements(
            By.CLASS_NAME,
            "inventory_item"
        )


    def get_products_count(self):
        return len(self.get_products())


    def get_product_names(self):

        products = self.get_products()

        names = []

        for product in products:
            name = product.find_element(
                By.CLASS_NAME,
                "inventory_item_name"
            ).text

            names.append(name)

        return names