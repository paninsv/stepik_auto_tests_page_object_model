from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from .locators import MainPageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    # def should_be_login_link(self):
    #     self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")


