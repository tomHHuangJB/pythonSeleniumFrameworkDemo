from selenium.webdriver.support.ui import WebDriverWait

from pages.debug_panel_page import DebugPanelPage


def test_debug_panel(driver, base_url):
    driver.get(f"{base_url}/")
    debug = DebugPanelPage(driver)

    debug.open_panel()
    WebDriverWait(driver, 5).until(lambda d: debug.is_open())

    debug.toggle_show_testids()
    assert debug.testid_visibility_attr() == "true"

    debug.toggle_offline()
    debug.select_network_profile("offline")
    debug.select_permission_override("granted")
    debug.set_time_skew("60000")

    assert "offline" in debug.state_viewer_text()
    assert "granted" in debug.state_viewer_text()
