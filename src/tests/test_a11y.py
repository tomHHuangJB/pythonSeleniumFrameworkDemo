from selenium.webdriver.support.ui import WebDriverWait

from pages.a11y_page import A11yPage


def test_a11y_features(driver, base_url):
    driver.get(f"{base_url}/a11y")
    a11y = A11yPage(driver)

    a11y.announce_update()
    WebDriverWait(driver, 5).until(lambda d: a11y.aria_live_text() != "Ready")

    driver.find_element("xpath", "//button[contains(.,'Open modal')]").click()
    assert a11y.modal_visible()

    a11y.toggle_high_contrast()
    a11y.toggle_reduced_motion()
