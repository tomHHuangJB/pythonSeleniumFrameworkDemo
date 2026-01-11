from pages.base_page import BasePage


class DynamicPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.optimistic_count = self.test_id("optimistic-count")
        self.optimistic_btn = self.test_id("optimistic-btn")
        self.optimistic_status = self.test_id("optimistic-status")
        self.race_trigger = self.test_id("race-trigger")
        self.dedup_trigger = self.test_id("dedup-trigger")
        self.partial_trigger = self.test_id("partial-trigger")
        self.cache_toggle = self.test_id("cache-toggle")
        self.ws_disconnect = self.test_id("ws-disconnect")
        self.sw_register = self.test_id("sw-register")
        self.sw_unregister = self.test_id("sw-unregister")
        self.skeleton_card = self.test_id("skeleton-card")
        self.partial_failure = self.test_id("partial-failure")
        self.dynamic_log = self.test_id("dynamic-log")

    def count(self) -> int:
        return int(self.get(self.optimistic_count).text)

    def click_optimistic(self) -> None:
        self.click(self.optimistic_btn)

    def status_text(self) -> str:
        return self.get(self.optimistic_status).text

    def trigger_race(self) -> None:
        self.click(self.race_trigger)

    def trigger_dedup(self) -> None:
        self.click(self.dedup_trigger)

    def trigger_partial(self) -> None:
        self.click(self.partial_trigger)

    def toggle_cache(self) -> None:
        self.click(self.cache_toggle)

    def simulate_disconnect(self) -> None:
        self.click(self.ws_disconnect)

    def register_service_worker(self) -> None:
        self.click(self.sw_register)

    def unregister_service_worker(self) -> None:
        self.click(self.sw_unregister)

    def skeleton_visible(self) -> bool:
        return self.get(self.skeleton_card).is_displayed()

    def partial_failure_visible(self) -> bool:
        return self.get(self.partial_failure).is_displayed()

    def log_items(self):
        return self.get(self.dynamic_log).find_elements("tag name", "li")
