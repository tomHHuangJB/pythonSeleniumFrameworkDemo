from selenium.webdriver.support.ui import WebDriverWait

from pages.errors_page import ErrorsPage


def test_error_states_and_security_labs(driver, base_url):
    driver.get(f"{base_url}/errors")
    errors = ErrorsPage(driver)

    errors.trigger_network_fail()
    errors.trigger_timeouts()
    assert errors.partial_good_visible()
    assert errors.partial_fail_visible()

    errors.start_leak()
    WebDriverWait(driver, 5).until(lambda d: "Leak size" in d.page_source)

    # Demo-only: security lab triggers exercise Selenium flows.
    # In production, these behaviors must be blocked and validated by app controls.
    errors.run_security_labs()
    assert "Audit log" in errors.audit_log_text()
