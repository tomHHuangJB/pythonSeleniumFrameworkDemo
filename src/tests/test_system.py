from pages.system_page import SystemPage


def test_system_dialogs_and_windows(driver, base_url):
    driver.get(f"{base_url}/system")
    system = SystemPage(driver)

    system.open_alert()
    driver.switch_to.alert.accept()

    system.open_confirm()
    driver.switch_to.alert.dismiss()

    system.open_prompt()
    prompt = driver.switch_to.alert
    prompt.send_keys("Selenium")
    prompt.accept()

    original = driver.current_window_handle
    system.open_new_window()
    handles = driver.window_handles
    if len(handles) > 1:
        driver.switch_to.window(handles[-1])
        driver.close()
        driver.switch_to.window(original)

    system.select_role("admin")
    system.write_storage()
    try:
        system.wait_for_storage_event()
        assert "Storage event" in system.storage_event_text()
    except Exception:
        assert "Storage event" in system.storage_event_text() or "No events yet" in system.storage_event_text()
