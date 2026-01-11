from pages.integrations_page import IntegrationsPage


def test_iframe_post_message(driver, base_url):
    driver.get(f"{base_url}/integrations")
    integrations = IntegrationsPage(driver)
    integrations.approve_payment()
    assert "payment-approved" in integrations.message_text()
