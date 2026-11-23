import pytest

BASE_URL = "https://devtuth.dolphin.com.np/dartachalani"

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture
def login_page(page, base_url):
    from pages.login_page import LoginPage
    lp = LoginPage(page, base_url)
    lp.open()
    return lp