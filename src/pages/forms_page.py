from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class FormsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.toggle_extra = self.test_id("toggle-extra")
        self.conditional_input = self.test_id("conditional-input")
        self.wizard_prev = self.test_id("wizard-prev")
        self.wizard_next = self.test_id("wizard-next")
        self.wizard_step = self.test_id("wizard-step")
        self.array_add = self.test_id("array-add")
        self.rich_text_iframe = self.test_id("rich-text-iframe")
        self.drag_drop_zone = self.test_id("drag-drop-zone")
        self.color_picker = self.test_id("color-picker")
        self.range_min = self.test_id("range-min")
        self.range_max = self.test_id("range-max")
        self.datetime_picker = self.test_id("datetime-picker")
        self.shadow_host = self.test_id("shadow-host")

    def toggle_extra_field(self) -> None:
        self.click(self.toggle_extra)

    def conditional_visible(self) -> bool:
        try:
            return self.get(self.conditional_input).is_displayed()
        except Exception:
            return False

    def wizard_next_step(self) -> None:
        self.click(self.wizard_next)

    def wizard_step_text(self) -> str:
        return self.get(self.wizard_step).text

    def add_array_item(self) -> None:
        self.click(self.array_add)

    def remove_array_item(self, index: int) -> None:
        self.click(self.test_id(f"array-remove-{index}"))

    def enter_rich_text(self, text: str) -> None:
        iframe = self.get(self.rich_text_iframe)
        self.driver.switch_to.frame(iframe)
        body = self.driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.CONTROL, "a")
        body.send_keys(text)
        self.driver.switch_to.default_content()

    def drag_drop_zone_visible(self) -> bool:
        return self.get(self.drag_drop_zone).is_displayed()

    def pick_color(self, value: str) -> None:
        self.type(self.color_picker, value)

    def set_range(self, min_val: int, max_val: int) -> None:
        self.type(self.range_min, str(min_val))
        self.type(self.range_max, str(max_val))

    def set_datetime(self, value: str) -> None:
        self.type(self.datetime_picker, value)

    def fill_shadow_input(self, text: str) -> None:
        element = self.shadow_input(self.shadow_host, "shadow-input")
        element.clear()
        element.send_keys(text)
