from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Waits:
    def __init__(self, driver: WebDriver, timeout: int = 15) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def visible(self, locator: tuple[str, str]):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def present(self, locator: tuple[str, str]):
        return self.wait.until(EC.presence_of_element_located(locator))

    def clickable(self, locator: tuple[str, str]):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def text_contains(self, locator: tuple[str, str], text: str) -> None:
        self.wait.until(EC.text_to_be_present_in_element(locator, text))

    def page_ready(self) -> None:
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
