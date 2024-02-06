from conftest import browser
from pages.modal_dialogs import ModalDialogsPage

def test_modal_elements(browser):
    page = ModalDialogsPage(browser)
    page.go_to_page()
    assert page.get_submenu_buttons_count() == 5
def test_navigation_modal(browser):
    page = ModalDialogsPage(browser)
    page.go_to_page()
    page.refresh_page()
    page.go_to_home_page()
    page.go_back()
    page.set_window_size(900, 400)
    page.go_forward()
    assert page.get_current_url() == 'https://demoqa.com/'
    assert page.get_title() == 'ToolsQA'
    page.set_window_size(1000, 1000)