class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.product_list = ".inventory_list"
        self.product_items = ".inventory_item"
        self.cart_icon = ".shopping_cart_link"

    def get_products_counts(self):
        return self.page.locator(self.product_items).count()

    def is_inventory_page(self):
        return self.page.url.endswith("inventory.html")

    def add_first_product_to_cart(self):
        self.page.locator(".btn_inventory").first.click()
