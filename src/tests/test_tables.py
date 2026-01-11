from pages.tables_page import TablesPage


def test_table_operations(driver, base_url):
    driver.get(f"{base_url}/tables")
    tables = TablesPage(driver)
    assert tables.grid_visible()
    tables.select_row(1)
    tables.update_row_name(2, "Row 2 Updated")
    tables.update_row_status(3, "Archived")
    tables.sort_ascending()
    tables.filter_active_rows()
    tables.next_cursor_page()
    tables.next_offset_page()
    tables.export_csv()
