import pytest
import re
from playwright.sync_api import expect


def test_valid_login(login_page, page):
    login_page.login("admin", "admin")
    expect(page).not_to_have_url(re.compile(r"/login"))
    expect(page.get_by_role("heading", name="Dartachalani Dashboard")).to_be_visible()

@pytest.mark.parametrize("user,pwd", [
    ("wrong", "admin"),
    ("admin", "wrong"),
    ("wrong", "wrong"),
])
def test_invalid_login(login_page, page, user, pwd):
    login_page.login(user, pwd)
    expect(page.get_by_text("The username or password you entered is incorrect.")).to_be_visible()
    expect(page).to_have_url(re.compile(r"/login"))

 