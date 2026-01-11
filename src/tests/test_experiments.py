from pages.experiments_page import ExperimentsPage


def test_experiments_flags(driver, base_url):
    driver.get(f"{base_url}/experiments")
    experiments = ExperimentsPage(driver)

    experiments.choose_variant_b()
    assert "B" in experiments.active_variant_text()

    experiments.apply_flag_override()
    experiments.select_role("admin")
    assert "true" in experiments.flag_enabled_text()
