from pages.forms_page import FormsPage


def test_complex_forms(driver, base_url):
    driver.get(f"{base_url}/forms")
    forms = FormsPage(driver)
    forms.toggle_extra_field()
    assert forms.conditional_visible()

    forms.wizard_next_step()
    assert "Step 2" in forms.wizard_step_text()

    forms.add_array_item()
    forms.remove_array_item(0)

    forms.enter_rich_text("Senior automation input")
    forms.fill_shadow_input("Shadow DOM value")
    forms.pick_color("#ff0000")
    forms.set_range(20, 80)
    forms.set_datetime("2024-01-10T10:30")
    assert forms.drag_drop_zone_visible()
