from pages.base_page import BasePage


class A11yPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.announce_btn = self.test_id("announce-btn")
        self.aria_live = self.test_id("aria-live")
        self.focus_modal = self.test_id("focus-modal")
        self.high_contrast = self.test_id("high-contrast")
        self.reduced_motion = self.test_id("reduced-motion")

    def announce_update(self) -> None:
        self.click(self.announce_btn)

    def aria_live_text(self) -> str:
        return self.get(self.aria_live).text

    def modal_visible(self) -> bool:
        return self.get(self.focus_modal).is_displayed()

    def toggle_high_contrast(self) -> None:
        self.click(self.high_contrast)

    def toggle_reduced_motion(self) -> None:
        self.click(self.reduced_motion)
