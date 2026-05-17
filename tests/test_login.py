from pages.login_page import LoginPage
import os
import pytest


class TestLogin:
    @pytest.mark.smoke
    def test_valid_login(self, logged_in_page):
        assert logged_in_page.url.endswith("/inventory.html")

    def test_invalid_login(self, navigated_page):
        login_page = LoginPage(navigated_page)
        login_page.login("wrong_user", "wrong_password")
        error = login_page.get_error_message()
        assert "Username and password do not match" in error

    def test_empty_credentials(self, navigated_page):
        login_page = LoginPage(navigated_page)
        login_page.login("", "")
        error = login_page.get_error_message()
        assert "Username is required" in error
