from selenium.webdriver.common.by import By

class ModalDialogsPage:
    def __init__(self, browser):
        self.browser = browser

    def go_to_page(self):
        self.browser.get("https://demoqa.com/modal-dialogs")

    def get_submenu_buttons_count(self):
        buttons = self.browser.find_elements(By.CSS_SELECTOR, ".nav-link[data-toggle='dropdown']")
        return len(buttons)

    def refresh_page(self):
        self.browser.refresh()

    def go_to_home_page(self):
        home_icon = self.browser.find_elements(By.CSS_SELECTOR, ".brand")
        home_icon.click()

    def go_back(self):
        self.browser.back()

    def set_window_size(self, width, height):
        self.browser.set_window_size(width, height)

    def go_forward(self):
        self.browser.forward()

    def get_current_url(self):
        return self.browser.current_url

    def get_title(self):
        return self.browser.title

