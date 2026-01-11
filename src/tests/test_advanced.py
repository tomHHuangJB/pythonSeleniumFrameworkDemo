from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

from pages.components_page import ComponentsPage


def test_advanced_selenium_features(driver, base_url):
    driver.get(f"{base_url}/components")
    components = ComponentsPage(driver)

    components.open_context_menu()
    driver.switch_to.alert.accept()

    toast_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='toast-btn']")
    driver.execute_script("arguments[0].scrollIntoView(true);", toast_button)
    components.trigger_toast()
    assert components.has_toasts()

    driver.get(f"{base_url}/auth")
    username_label = driver.find_element(By.XPATH, "//label[contains(.,'Username')]")
    username_input = driver.find_element(locate_with(By.TAG_NAME, "input").below(username_label))
    username_input.send_keys("relative-locator")
