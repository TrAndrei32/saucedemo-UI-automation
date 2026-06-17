from pages.menu_page import MenuPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


class TestMenu:
    def test_menu_closed_by_default(self, logged_in_page):
        menu = MenuPage(logged_in_page)
        assert not menu.is_menu_open()

    def test_menu_opens(self, logged_in_page):
        menu = MenuPage(logged_in_page)
        menu.open_menu()
        assert menu.is_menu_open()

    def test_menu_closes(self, logged_in_page):
        menu = MenuPage(logged_in_page)
        menu.open_menu()
        assert menu.is_menu_open()

        menu.close_menu()
        assert not menu.is_menu_open()

    def test_logout_redirects_to_login_page(self, logged_in_page):
        menu = MenuPage(logged_in_page)
        menu.open_menu()
        menu.click_logout()

        assert logged_in_page.url == "https://www.saucedemo.com/"

    def test_reset_app_state_clears_cart(self, logged_in_page):
        inventory = InventoryPage(logged_in_page)
        cart = CartPage(logged_in_page)
        menu = MenuPage(logged_in_page)

        inventory.add_first_product_to_cart()
        assert cart.get_cart_badge_count() == "1"

        menu.open_menu()
        menu.click_reset_app_state()
        menu.close_menu()

        assert not logged_in_page.locator(
            "[data-test='shopping-cart-badge']").is_visible(), \
            "Badge should not be visible after reset app state"
