from .base_page import BasePage


class MainPage(BasePage):
    # перенесли методы в BasePage
    # def go_to_login_page(self):
    #     # login_link = self.browser.find_element(by=By.CSS_SELECTOR, value="#registration_link")
    #     login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    #     login_link.click()
    #
    # def should_be_login_link(self):
    #     assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


