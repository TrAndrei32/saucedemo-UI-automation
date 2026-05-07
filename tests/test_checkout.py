import os
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage


class TestCheckout:
    def test_checkout_happy_path(self, logged_in_page):
        inventory = InventoryPage(logged_in_page)
        checkout = CheckoutPage(logged_in_page)

        inventory.add_first_product_to_cart()
        logged_in_page.locator(".shopping_cart_link").click()
        checkout.go_to_checkout()
        checkout.fill_checkout_info(
            os.getenv("FIRST_NAME"),
            os.getenv("LAST_NAME"),
            os.getenv("POSTAL_CODE")
        )
        checkout.continue_to_overview()
        checkout.finish_order()

        message = checkout.get_confirmation_message()
        assert message == "Thank you for your order!"

    def test_checkout_missing_firstname(self, logged_in_page):
        inventory = InventoryPage(logged_in_page)
        checkout = CheckoutPage(logged_in_page)

        inventory.add_first_product_to_cart()
        logged_in_page.locator(".shopping_cart_link").click()
        checkout.go_to_checkout()
        checkout.fill_checkout_info("",
                                    os.getenv("LAST_NAME"),
                                    os.getenv("POSTAL_CODE")
                                    )
        checkout.continue_to_overview()

        error = checkout.get_error_message()
        assert "First Name is required" in error
