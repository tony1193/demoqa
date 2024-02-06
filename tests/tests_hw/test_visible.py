from pages.elements import Elements
import time
from conftest import browser


def test_visible_btn_sidebar(browser):
    elements = Elements(browser)
    elements.visit()
    elements.btn_sidebar_first.click()
    time.sleep(3)
    assert elements.btn_sidebar_first_textbox.exist()
    assert elements.btn_sidebar_first_textbox.visible()
