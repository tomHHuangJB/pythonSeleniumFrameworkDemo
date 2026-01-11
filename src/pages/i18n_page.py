from pages.base_page import BasePage


class I18nPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locale_select = self.test_id("locale-select")
        self.timezone_select = self.test_id("timezone-select")

    def select_locale(self, locale: str) -> None:
        self.select_by_value(self.locale_select, locale)

    def select_timezone(self, timezone: str) -> None:
        self.select_by_value(self.timezone_select, timezone)

    def page_dir_attribute(self) -> str:
        select = self.get(self.locale_select)
        return self.driver.execute_script(
            "return arguments[0].closest('div[dir]').getAttribute('dir');", select
        )

    def timezone_text(self) -> str:
        return self.driver.find_element("xpath", "//*[contains(text(),'Selected TZ:')]").text
