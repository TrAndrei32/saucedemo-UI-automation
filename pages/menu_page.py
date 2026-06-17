from pages.base_page import BasePage


class MenuPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.open_menu_button = "#react-burger-menu-btn"
        self.close_menu_button = "#react-burger-cross-btn"
        self.logout_link = "[data-test='logout-sidebar-link']"
        self.about_link = "[data-test='about-sidebar-link']"
        self.reset_link = "[data-test='reset-sidebar-link']"
        self.menu_wrap = ".bm-menu-wrap"

    def open_menu(self):
        self.page.locator(self.open_menu_button).click()

    def close_menu(self):
        self.page.locator(self.close_menu_button).click()

    def click_logout(self):
        self.page.locator(self.logout_link).click()

    def click_about(self):
        self.page.locator(self.about_link).click()

    def click_reset_app_state(self):
        self.page.locator(self.reset_link).click()

    def is_menu_open(self) -> bool:
        self.page.wait_for_timeout(300)
        aria_hidden = self.page.locator(
            self.menu_wrap).get_attribute("aria-hidden")
        return aria_hidden == "false"
