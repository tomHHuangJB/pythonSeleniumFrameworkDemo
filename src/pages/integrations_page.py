from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class IntegrationsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.payment_iframe = self.test_id("payment-iframe")
        self.iframe_message = self.test_id("iframe-message")

    def approve_payment(self) -> None:
        iframe = self.get(self.payment_iframe)
        self.driver.switch_to.frame(iframe)
        self.driver.find_element(By.TAG_NAME, "button").click()
        self.driver.switch_to.default_content()

    def message_text(self) -> str:
        return self.get(self.iframe_message).text
