from pages.base_page import BasePage


class PerformancePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.large_dom = self.test_id("large-dom")
        self.block_main_thread = self.test_id("block-main-thread")
        self.worker_result = self.test_id("worker-result")
        self.cpu_indicator = self.test_id("cpu-indicator")

    def large_dom_count(self) -> int:
        container = self.get(self.large_dom)
        return len(container.find_elements("tag name", "span"))

    def block_main(self) -> None:
        self.click(self.block_main_thread)

    def worker_result_text(self) -> str:
        return self.get(self.worker_result).text

    def cpu_indicator_text(self) -> str:
        return self.get(self.cpu_indicator).text
