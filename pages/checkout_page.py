from pages.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.checkout_button = "[data-test='checkout']"
        self.firstname_input = "[data-test='firstName']"
        self.lastname_input = "[data-test='lastName']"
        self.postal_code_input = "[data-test='postalCode']"
        self.error_message = "[data-test='error']"
        self.continue_button = ".submit-button"
        self.finish_button = "#finish"
        self.complete_order_message = ".complete-header"

    def go_to_checkout(self):
        self.page.locator(self.checkout_button).click()
        self.wait_for_url("checkout-step-one.html")

    def fill_checkout_info(self, firstname: str, lastname: str, postal: str):
        self.page.locator(self.firstname_input).fill(firstname)
        self.page.locator(self.lastname_input).fill(lastname)
        self.page.locator(self.postal_code_input).fill(postal)

    def continue_to_overview(self):
        self.page.locator(self.continue_button).click()

    def finish_order(self):
        self.page.locator(self.finish_button).click()

    def get_confirmation_message(self) -> str:
        return self.page.locator(self.complete_order_message).text_content()

    def get_error_message(self) -> str:
        return self.page.locator(self.error_message).text_content()
