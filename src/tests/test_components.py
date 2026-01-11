from selenium.webdriver.support.ui import WebDriverWait

from pages.components_page import ComponentsPage


def test_components_coverage(driver, base_url):
    driver.get(f"{base_url}/components")
    components = ComponentsPage(driver)

    assert components.virtual_list_visible()
    before = components.infinite_items_count()
    components.load_more_items()
    WebDriverWait(driver, 5).until(lambda d: components.infinite_items_count() > before)

    assert components.svg_visible()
    assert components.canvas_visible()

    components.open_context_menu()
    driver.switch_to.alert.accept()

    components.trigger_toast()
    WebDriverWait(driver, 5).until(lambda d: components.has_toasts())
    assert components.has_toasts()
