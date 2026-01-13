from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from utils.waits import Waits


class BasePage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.waits = Waits(driver)
        self.actions = ActionChains(driver)

    @staticmethod
    def test_id(value: str) -> tuple[str, str]:
        return By.CSS_SELECTOR, f"[data-testid='{value}']"

    def get(self, locator: tuple[str, str]):
        return self.waits.visible(locator)

    def click(self, locator: tuple[str, str]) -> None:
        self.waits.clickable(locator).click()

    def js_click(self, locator: tuple[str, str]) -> None:
        element = self.waits.visible(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', inline: 'center'});",
            element,
        )
        self.driver.execute_script("arguments[0].click();", element)

    def type(self, locator: tuple[str, str], text: str) -> None:
        element = self.waits.visible(locator)
        element.clear()
        element.send_keys(text)

    def select_by_value(self, locator: tuple[str, str], value: str) -> None:
        Select(self.waits.visible(locator)).select_by_value(value)

    def select_by_visible_text(self, locator: tuple[str, str], text: str) -> None:
        Select(self.waits.visible(locator)).select_by_visible_text(text)

    def shadow_input(self, host_locator: tuple[str, str], shadow_testid: str):
        host = self.waits.visible(host_locator)
        root = host.shadow_root
        return root.find_element(By.CSS_SELECTOR, f"[data-testid='{shadow_testid}']")
