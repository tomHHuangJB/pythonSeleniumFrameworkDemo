from pages.base_page import BasePage


class AuthPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username = self.test_id("login-username")
        self.password = self.test_id("login-password")
        self.remember = self.test_id("login-remember")
        self.submit = self.test_id("login-submit")
        self.mfa_code = self.test_id("mfa-code")
        self.mfa_verify = self.test_id("mfa-verify")

    def login(self, user: str, password: str, remember: bool = False) -> None:
        self.type(self.username, user)
        self.type(self.password, password)
        if remember:
            self.click(self.remember)
        self.click(self.submit)

    def submit_mfa(self, code: str) -> None:
        self.type(self.mfa_code, code)
        self.click(self.mfa_verify)
