from pages.base_page import BasePage


class Accordion(BasePage):

    def __init__(self, driver):
        self.browser = None
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver)

    def go_to_page(self):
        self.browser.get(self.base_url)

    def is_element_visible(self, param):
        pass

    def click_element(self, param):
        pass
