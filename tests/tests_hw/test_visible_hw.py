from pages.accordion import Accordion
import time
from conftest import browser


def test_visible_accordion(browser):
    accordion_page: Accordion = Accordion(browser)
    accordion_page.visit()
    assert accordion_page.is_element_visible('#section1Content > p')

    accordion_page.click_element('#section1Heading')
    time.sleep(2)
    assert not accordion_page.is_element_visible('#section1Content > p')


def test_visible_accordion_default(browser):
    accordion_page_default = Accordion(browser)
    accordion_page_default.visit()
    assert not accordion_page_default.is_element_visible('#section2Content > p:nth-child(1)')
    assert not accordion_page_default.is_element_visible('#section2Content > p:nth-child(2)')
    assert not accordion_page_default.is_element_visible('#section3Content > p')
