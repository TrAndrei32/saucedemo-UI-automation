from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class TestInventory:
    def test_inventory_page_loaded(self, page):
        login_page = LoginPage(page)
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(page)
        assert inventory_page.is_inventory_page()

    def test_product_count(self, page):
        login_page = LoginPage(page)
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(page)
        assert inventory_page.get_products_counts() > 0

    def test_add_first_product_to_cart(self, page):
        login_page = LoginPage(page)
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(page)
        inventory_page.add_first_product_to_cart()
        assert page.locator(".shopping_cart_badge").text_content() == "1"
