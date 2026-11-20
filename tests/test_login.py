import pytest

def test_valid_login(login_page, page):
    login_page.login("tomsmith", "SuperSecretPassword!")
    login_page.expect_message("You logged into a secure area!")
    assert "/secure" in page.url

@pytest.mark.parametrize("user,pwd,msg", [
    ("wrong", "SuperSecretPassword!", "Your username is invalid!"),
    ("tomsmith", "wrong", "Your password is invalid!"),
])
def test_invalid_login(login_page, user, pwd, msg):
    login_page.login(user, pwd)
    login_page.expect_message(msg)