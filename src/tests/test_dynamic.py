from selenium.webdriver.support.ui import WebDriverWait

from pages.dynamic_page import DynamicPage


def test_dynamic_state(driver, base_url):
    driver.get(f"{base_url}/dynamic")
    dynamic = DynamicPage(driver)

    before = dynamic.count()
    dynamic.click_optimistic()
    WebDriverWait(driver, 5).until(lambda d: dynamic.status_text() != "saving")
    assert dynamic.count() >= before

    dynamic.trigger_race()
    dynamic.trigger_dedup()
    dynamic.trigger_partial()
    dynamic.toggle_cache()
    dynamic.simulate_disconnect()
    dynamic.register_service_worker()
    dynamic.unregister_service_worker()

    assert dynamic.skeleton_visible()
    assert dynamic.partial_failure_visible()
    assert len(dynamic.log_items()) > 0
