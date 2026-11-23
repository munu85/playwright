from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.url = f"{base_url}/login"
        self.username = page.locator("input[type='text']")
        self.password = page.locator("input[type='password']")
        self.signin = page.get_by_role("button", name="Sign In")

    def open(self):
        self.page.goto(self.url)
        expect(self.username).to_be_visible()

    def login(self, user: str, pwd: str):
        self.username.fill(user)
        self.password.fill(pwd)
        self.signin.click()