from selenium.webdriver.common.by import By

from pages.home_page import HomePage


def test_home_dashboard(driver, base_url):
    driver.get(f"{base_url}/")
    home = HomePage(driver)

    assert home.session_state_visible()
    assert home.notification_log_visible()
    assert home.websocket_status().strip() != ""

    assert len(driver.find_elements(By.CSS_SELECTOR, "[role='navigation']")) > 0
    assert len(driver.find_elements(By.CSS_SELECTOR, "[role='complementary']")) > 0
