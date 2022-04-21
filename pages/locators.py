from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM_LOCATOR = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM_LOCATOR = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_PRODUCT_TO_BASKET_BUTTON_LOCATOR = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME_LOCATOR = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")
    PRODUCT_PRICE_LOCATOR = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_NAME_IN_BASKET_LOCATOR = (By.CSS_SELECTOR, "div#messages strong")
    PRODUCT_PRICE_IN_BASKET_LOCATOR = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-info.fade.in strong")
