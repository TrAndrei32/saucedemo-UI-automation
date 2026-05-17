from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.cart_items = "[data-test='inventory-item']"
        self.remove_button = "[data-test^='remove-']"
        self.cart_badge = "[data-test='shopping-cart-badge']"

    def get_cart_items_count(self) -> int:
        return self.page.locator(self.cart_items).count()

    def remove_first_item(self):
        self.page.locator(self.remove_button).first.click()

    def get_cart_badge_count(self) -> str:
        return self.page.locator(self.cart_badge).text_content()

    def is_cart_empty(self) -> bool:
        return self.page.locator(self.cart_items).count() == 0
