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

    def register_new_user(self, email, password):
        """
        принимает две строки и регистрирует пользователя
        :param email:
        :param password:
        :return:
        """
        registration_email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_LOCATOR)
        registration_password1_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1_LOCATOR)
        registration_password2_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2_LOCATOR)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON_LOCATOR)

        registration_email_field.send_keys(email)
        registration_password1_field.send_keys(password)
        registration_password2_field.send_keys(password)

        registration_button.click()
        self.wait_for_user_authorization()



