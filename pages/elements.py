from pages.base_page import BasePage
from components.components import WebElement

class Elements(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)

        self.text_center = WebElement(driver, '#app > div > div > div.row > div.col-12.nt-4.col-md-6')
        self.text_elements = WebElement(driver, 'div.playground-header > div')
        self.icon = WebElement(driver, 'header > a > ing')
        self.btn_sidebar_first = WebElement(driver, 'div:ntn-child(1) > span > div')
        self.btn_sidebar_first_textbox = WebElement(driver, 'div:ntn-child(1) > div> ul > #item-0 > span')