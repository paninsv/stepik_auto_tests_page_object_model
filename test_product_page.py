import time

from .pages.product_page import ProductPage


def open_page_and_get_code(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)  # инициализируем Page Object,
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    return page


def test_should_be_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)  # инициализируем Page Object,
    page.open()
    page.should_be_add_to_basket_button()


def test_should_be_name_in_basket_message(browser):
    page = open_page_and_get_code(browser)

    page.should_be_name_in_basket_message()


def test_should_be_price_in_basket_message(browser):
    page = open_page_and_get_code(browser)

    page.should_be_price_in_basket_message()


def test_guest_can_add_product_to_basket(browser):
    page = open_page_and_get_code(browser)

    # есть ли элементы с сообщениями о добавлении в продукта в корзину и его цене
    # странно что по заданию все в 1 тесте должно быть, а не раскидано по разным  .....
    page.should_be_name_in_basket_message()
    page.should_be_price_in_basket_message()

    # сравниваем имя продукта и имя в сообщении о добавлении в корзину
    page.should_be_equal_product_name_and_name_in_basket()

    # сравниваем цену продукта и цену в сообщении о добавлении в корзину
    page.should_be_equal_product_price_and_price_in_basket()

    # time.sleep(30)




