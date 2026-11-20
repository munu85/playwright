from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.url = f"{base_url}/login"
        self.username = page.locator("#username")
        self.password = page.locator("#password")
        self.submit = page.get_by_role("button", name="Login")
        self.flash = page.locator("#flash")

    def open(self):
        self.page.goto(self.url)

    def login(self, user: str, pwd: str):
        self.username.fill(user)
        self.password.fill(pwd)
        self.submit.click()

    def expect_message(self, text: str):
        expect(self.flash).to_contain_text(text)