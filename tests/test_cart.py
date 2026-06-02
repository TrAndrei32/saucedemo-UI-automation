from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


class TestCart:
    def test_remove_item_from_cart(self, logged_in_page):
        inventory = InventoryPage(logged_in_page)
        cart = CartPage(logged_in_page)
        inventory.add_first_product_to_cart()
        inventory.navigate_to_cart()
        assert cart.get_cart_items_count() == 1
        cart.remove_first_item()
        assert cart.is_cart_empty(), "Cart should be empty after removing item"

    def test_cart_badge_updates_after_remove(self, logged_in_page):
        inventory = InventoryPage(logged_in_page)
        cart = CartPage(logged_in_page)
        inventory.add_first_product_to_cart()
        inventory.navigate_to_cart()
        assert cart.get_cart_items_count() == 1
        cart.remove_first_item()
        assert not logged_in_page.locator(
            "[data-test='shopping-cart-badge']").is_visible()


class TestMultipleProducts:
    def test_add_three_products_badge(self, logged_in_page):
        inventory = InventoryPage(logged_in_page)
        cart = CartPage(logged_in_page)
        inventory.add_product_by_index(0)
        inventory.add_product_by_index(1)
        inventory.add_product_by_index(2)
        assert cart.get_cart_badge_count() == "3"

    def test_add_three_products_cart_count(self, logged_in_page):
        inventory = InventoryPage(logged_in_page)
        cart = CartPage(logged_in_page)
        inventory.add_product_by_index(0)
        inventory.add_product_by_index(1)
        inventory.add_product_by_index(2)
        logged_in_page.locator(".shopping_cart_link").click()
        assert cart.get_cart_items_count() == 3
