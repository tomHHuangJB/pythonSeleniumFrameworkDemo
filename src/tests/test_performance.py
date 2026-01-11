from selenium.webdriver.support.ui import WebDriverWait

from pages.performance_page import PerformancePage


def test_performance_signals(driver, base_url):
    driver.get(f"{base_url}/performance")
    performance = PerformancePage(driver)

    assert performance.large_dom_count() > 100
    performance.block_main()

    WebDriverWait(driver, 5).until(lambda d: "Result:" in performance.worker_result_text())
    assert "CPU" in performance.cpu_indicator_text()
