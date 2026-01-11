from pages.base_page import BasePage


class SystemPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.alert_button = self.test_id("dialog-alert")
        self.confirm_button = self.test_id("dialog-confirm")
        self.prompt_button = self.test_id("dialog-prompt")
        self.window_open = self.test_id("window-open")
        self.storage_write = self.test_id("storage-write")
        self.storage_event = self.test_id("storage-event")
        self.role_select = self.test_id("role-access-select")

    def open_alert(self) -> None:
        self.click(self.alert_button)

    def open_confirm(self) -> None:
        self.click(self.confirm_button)

    def open_prompt(self) -> None:
        self.click(self.prompt_button)

    def open_new_window(self) -> None:
        self.click(self.window_open)

    def write_storage(self) -> None:
        self.click(self.storage_write)

    def wait_for_storage_event(self) -> None:
        self.waits.text_contains(self.storage_event, "Storage event")

    def storage_event_text(self) -> str:
        return self.get(self.storage_event).text

    def select_role(self, role: str) -> None:
        self.select_by_value(self.role_select, role)
