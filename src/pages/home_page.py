from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.ws_status = self.test_id("ws-status")
        self.notification_log = self.test_id("notification-log")
        self.session_state = self.test_id("session-state")

    def websocket_status(self) -> str:
        return self.get(self.ws_status).text

    def notification_log_visible(self) -> bool:
        return self.get(self.notification_log).is_displayed()

    def session_state_visible(self) -> bool:
        return self.get(self.session_state).is_displayed()
