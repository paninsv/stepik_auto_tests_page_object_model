from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

    VIEW_BASKET_LINK = (By.CSS_SELECTOR, 'span.btn-group > a.btn.btn-default')

    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    # перенесли в BasePageLocators
    # LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    pass


class LoginPageLocators:
    LOGIN_FORM_LOCATOR = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM_LOCATOR = (By.CSS_SELECTOR, "#register_form")

    REGISTRATION_EMAIL_LOCATOR = (By.CSS_SELECTOR, 'input#id_registration-email')
    REGISTRATION_PASSWORD1_LOCATOR = (By.CSS_SELECTOR, 'input#id_registration-password1')
    REGISTRATION_PASSWORD2_LOCATOR = (By.CSS_SELECTOR, 'input#id_registration-password2')

    REGISTRATION_BUTTON_LOCATOR = (By.NAME, 'registration_submit')


class ProductPageLocators:
    ADD_PRODUCT_TO_BASKET_BUTTON_LOCATOR = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME_LOCATOR = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")
    PRODUCT_PRICE_LOCATOR = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_NAME_IN_BASKET_LOCATOR = (By.CSS_SELECTOR, "div#messages strong")
    PRODUCT_PRICE_IN_BASKET_LOCATOR = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-info.fade.in strong")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div#messages strong")


class BasketPageLocators:
    EMPTY_BASKET_MESSAGE_LOCATOR = (By.CSS_SELECTOR, '#content_inner > p')
    PRODUCTS_IN_BASKET_LOCATOR = (By.CSS_SELECTOR, 'div.basket-items')
