from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """
        подсказка вместо докстринги ;)
        current_url
        Gets the URL of the current page.
        Usage:
        driver.current_url
       """
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "'login' is not url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_LOCATOR), "Login form is not present"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_LOCATOR), "Register form is not present"
