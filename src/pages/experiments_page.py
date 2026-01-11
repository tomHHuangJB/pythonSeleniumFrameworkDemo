from pages.base_page import BasePage


class ExperimentsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.variant_a = self.test_id("variant-a")
        self.variant_b = self.test_id("variant-b")
        self.flag_override = self.test_id("flag-override")
        self.role_select = self.test_id("role-select")

    def choose_variant_a(self) -> None:
        self.click(self.variant_a)

    def choose_variant_b(self) -> None:
        self.click(self.variant_b)

    def active_variant_text(self) -> str:
        return self.driver.find_element("xpath", "//*[contains(text(),'Active variant:')]").text

    def apply_flag_override(self) -> None:
        self.click(self.flag_override)

    def select_role(self, role: str) -> None:
        self.select_by_value(self.role_select, role)

    def flag_enabled_text(self) -> str:
        return self.driver.find_element("xpath", "//*[contains(text(),'Flag enabled:')]").text
