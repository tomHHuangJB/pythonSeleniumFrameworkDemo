from pages.auth_page import AuthPage


def test_login_and_mfa(driver, base_url):
    driver.get(f"{base_url}/auth")
    auth = AuthPage(driver)
    auth.login("principal.engineer", "demo", remember=True)
    auth.submit_mfa("123456")
