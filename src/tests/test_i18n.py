from pages.i18n_page import I18nPage


def test_locale_and_timezone(driver, base_url):
    driver.get(f"{base_url}/i18n")
    i18n = I18nPage(driver)

    i18n.select_locale("ar")
    assert i18n.page_dir_attribute() == "rtl"

    i18n.select_timezone("Asia/Tokyo")
    assert "Asia/Tokyo" in i18n.timezone_text()
