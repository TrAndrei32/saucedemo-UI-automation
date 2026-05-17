from pages.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.product_list = ".inventory_list"
        self.product_items = ".inventory_item"
        self.cart_icon = ".shopping_cart_link"
        self.sort_dropdown = ".product_sort_container"
        self.open_cart = ".shopping_cart_link"

    def get_products_counts(self):
        return self.page.locator(self.product_items).count()

    def is_inventory_page(self):
        # return self.page.url.endswith("inventory.html")
        return self.get_url().endswith("inventory.html")

    def add_first_product_to_cart(self):
        self.page.locator(".btn_inventory").first.click()

    def navigate_to_cart(self):
        self.page.locator(self.open_cart).click()

    def select_sort_option(self, option_value: str):
        """option_value: 'az', 'za', 'lohi',  'hilo'"""
        self.page.locator(self.sort_dropdown).select_option(option_value)

    def get_product_names(self) -> list[str]:
        items = self.page.locator(".inventory_item_name")
        return [items.nth(i).text_content() for i in range(items.count())]

    def get_product_prices(self) -> list[float]:
        items = self.page.locator("inventory_item_price")
        return [float(items.nth(i).text.content().replace("$", "")) for i in range(items.count())]
