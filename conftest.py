import pytest
from pages.login_page import LoginPage
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://www.saucedemo.com"


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture
def page(page, base_url):
    page.goto(base_url)
    return page


@pytest.fixture(scope="function")
def logged_in_page(page):
    login_page = LoginPage(page)
    login_page.login(os.getenv("NAME"), os.getenv("PASSWORD"))
    return page
