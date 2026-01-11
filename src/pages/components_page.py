from pages.base_page import BasePage


class ComponentsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.virtual_list = self.test_id("virtual-list")
        self.infinite_scroll = self.test_id("infinite-scroll")
        self.load_more = self.test_id("load-more")
        self.svg_chart = self.test_id("svg-chart")
        self.canvas = self.test_id("canvas")
        self.context_zone = self.test_id("context-zone")
        self.toast_button = self.test_id("toast-btn")
        self.toast_item = self.test_id("toast-item")

    def virtual_list_visible(self) -> bool:
        return self.get(self.virtual_list).is_displayed()

    def infinite_items_count(self) -> int:
        container = self.get(self.infinite_scroll)
        return len(container.find_elements("css selector", "div.rounded"))

    def load_more_items(self) -> None:
        self.click(self.load_more)

    def svg_visible(self) -> bool:
        return self.get(self.svg_chart).is_displayed()

    def canvas_visible(self) -> bool:
        return self.get(self.canvas).is_displayed()

    def open_context_menu(self) -> None:
        zone = self.get(self.context_zone)
        self.actions.context_click(zone).perform()

    def trigger_toast(self) -> None:
        self.click(self.toast_button)

    def has_toasts(self) -> bool:
        return len(self.driver.find_elements(*self.toast_item)) > 0
