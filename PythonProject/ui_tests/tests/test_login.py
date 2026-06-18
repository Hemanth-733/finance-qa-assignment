from pages.login_page import LoginPage

def test_valid_login(page):
    login = LoginPage(page)
    login.navigate()
    login.login("Admin", "admin123")

    page.wait_for_url("**/dashboard/**")
    assert "dashboard" in page.url.lower()


def test_invalid_login(page):
    login = LoginPage(page)
    login.navigate()
    login.login("Admin", "wrongpassword")

    page.wait_for_selector(".oxd-alert-content-text")
    assert "Invalid credentials" in page.locator(".oxd-alert-content-text").text_content()