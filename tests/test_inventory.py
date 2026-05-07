from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import os


class TestInventory:
    def test_inventory_page_loaded(self, logged_in_page):
        inventory_page = InventoryPage(logged_in_page)
        assert inventory_page.is_inventory_page()

    def test_product_count(self, logged_in_page):
        inventory_page = InventoryPage(logged_in_page)
        assert inventory_page.get_products_counts() > 0

    def test_add_first_product_to_cart(self, logged_in_page):
        inventory_page = InventoryPage(logged_in_page)
        inventory_page.add_first_product_to_cart()
        assert logged_in_page.locator(
            ".shopping_cart_badge").text_content() == "1"


class TestSorting:
    def test_sort_az(self, logged_in_page):
        inventory_page = InventoryPage(logged_in_page)
        inventory_page.select_sort_option("az")
        names = inventory_page.get_product_names()
        assert names == sorted(names), f"Expected A->Z, got: {names}"

    def test_sort_za(self, logged_in_page):
        inventory_page = InventoryPage(logged_in_page)
        inventory_page.select_sort_option("za")
        names = inventory_page.get_product_names()
        assert names == sorted(
            names, reverse=True), f"Expected Z->A, got: {names}"

    def test_sort_price_low_to_high(self, logged_in_page):
        inventory_page = InventoryPage(logged_in_page)
        inventory_page.select_sort_option("lohi")
        prices = inventory_page.get_product_prices()
        assert prices == sorted(
            prices, reverse=True), f"Expected price asc, got: {prices}"

    def test_sort_price_high_to_low(self, logged_in_page):
        inventory_page = InventoryPage(logged_in_page)
        inventory_page.select_sort_option("hilo")
        prices = inventory_page.get_product_prices()
        assert prices == sorted(
            prices, reverse=True), f"Expected price DESC, got: {prices}"
