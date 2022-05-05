from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_basket_message(self):

        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE_LOCATOR), \
            "'empty basket' message is not present"

    # в корзине нет товаров
    def should_not_be_products_in_basket(self):

        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET_LOCATOR), \
            "Where are products in basket, but should not be"
