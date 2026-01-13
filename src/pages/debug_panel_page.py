from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class DebugPanelPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.close_btn = self.test_id("debug-close")
        self.show_testids = self.test_id("debug-testids")
        self.simulate_offline = self.test_id("debug-offline")
        self.network_profile = self.test_id("debug-network")
        self.permission_override = self.test_id("debug-permission")
        self.time_skew = self.test_id("debug-time-skew")
        self.state_viewer = self.test_id("state-viewer")

    def open_panel(self) -> None:
        self.actions.key_down(Keys.ALT).key_down(Keys.SHIFT).send_keys("d").key_up(Keys.SHIFT).key_up(Keys.ALT).perform()

    def is_open(self) -> bool:
        return len(self.driver.find_elements(*self.close_btn)) > 0

    def toggle_show_testids(self) -> None:
        # CI runs can have overlay timing issues; JS click avoids intercepted clicks.
        self.js_click(self.show_testids)

    def toggle_offline(self) -> None:
        # CI runs can have overlay timing issues; JS click avoids intercepted clicks.
        self.js_click(self.simulate_offline)

    def select_network_profile(self, value: str) -> None:
        self.select_by_value(self.network_profile, value)

    def select_permission_override(self, value: str) -> None:
        self.select_by_value(self.permission_override, value)

    def set_time_skew(self, value: str) -> None:
        element = self.get(self.time_skew)
        element.clear()
        element.send_keys(value)

    def state_viewer_text(self) -> str:
        return self.get(self.state_viewer).text

    def testid_visibility_attr(self) -> str:
        return self.driver.execute_script("return document.documentElement.getAttribute('data-testid-visible');")
