from pytest_playwright.pytest_playwright import page
from playwright.async_api import expect


self.error = page.get_by_text("The username or password you entered is incorrect.")

def expect_error(self):
    expect(self.error).to_be_visible()