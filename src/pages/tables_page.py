from pages.base_page import BasePage


class TablesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.data_grid = self.test_id("data-grid")
        self.cursor_next = self.test_id("cursor-next")
        self.offset_next = self.test_id("offset-next")
        self.bulk_export = self.test_id("bulk-export")
        self.sort_asc = self.test_id("sort-asc")
        self.filter_active = self.test_id("filter-active")

    def grid_visible(self) -> bool:
        return self.get(self.data_grid).is_displayed()

    def select_row(self, row_id: int) -> None:
        self.click(self.test_id(f"row-select-{row_id}"))

    def update_row_name(self, row_id: int, name: str) -> None:
        self.type(self.test_id(f"row-name-{row_id}"), name)

    def update_row_status(self, row_id: int, status: str) -> None:
        self.select_by_visible_text(self.test_id(f"row-status-{row_id}"), status)

    def next_cursor_page(self) -> None:
        self.click(self.cursor_next)

    def next_offset_page(self) -> None:
        self.click(self.offset_next)

    def export_csv(self) -> None:
        self.click(self.bulk_export)

    def sort_ascending(self) -> None:
        self.click(self.sort_asc)

    def filter_active_rows(self) -> None:
        self.click(self.filter_active)
