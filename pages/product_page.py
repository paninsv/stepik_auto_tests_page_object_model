from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_PRODUCT_TO_BASKET_BUTTON_LOCATOR), \
            "add_to_basket is not present"

    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_TO_BASKET_BUTTON_LOCATOR)
        add_to_basket_button.click()

    def should_be_name_in_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_IN_BASKET_LOCATOR), \
            "product name in basket message is not present"

    def should_be_price_in_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET_LOCATOR), \
            "product price in basket message is not present"

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_LOCATOR).text

    def get_product_name_in_basket_message(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET_LOCATOR).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_LOCATOR).text

    def get_product_price_in_basket_message(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET_LOCATOR).text

    def should_be_equal_product_name_and_name_in_basket(self):
        name_in_basket_message = self.get_product_name_in_basket_message()
        product_name = self.get_product_name()
        assert name_in_basket_message == product_name,  "product name and product name in basket message is not equal"

    def should_be_equal_product_price_and_price_in_basket(self):
        price_in_basket_message = self.get_product_price_in_basket_message()
        product_price = self.get_product_price()
        assert price_in_basket_message == product_price,  "product price and product price in basket" \
                                                          " message is not equal"
