import time

import pytest

from .pages.product_page import ProductPage
from .pages.login_page import LoginPage


def open_page_and_get_code(browser,
                           link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
                                "?promo=newYear2019"):
    page = ProductPage(browser, link)  # инициализируем Page Object,
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    return page

#
# def test_should_be_add_to_basket_button(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#     page = ProductPage(browser, link)  # инициализируем Page Object,
#     page.open()
#     page.should_be_add_to_basket_button()


def test_should_be_name_in_basket_message(browser):
    page = open_page_and_get_code(browser)

    page.should_be_name_in_basket_message()

    time.sleep(200)


def test_should_be_price_in_basket_message(browser):
    page = open_page_and_get_code(browser)

    page.should_be_price_in_basket_message()


@pytest.mark.skip
@pytest.mark.parametrize('offer_number', [*range(7),
                                          pytest.param(7, marks=pytest.mark.skip(reason="some bug")),
                                          *range(8, 10)])
def test_guest_can_add_product_to_basket(browser, offer_number):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_number}'
    page = open_page_and_get_code(browser, link)

    # есть ли элементы с сообщениями о добавлении в продукта в корзину и его цене
    # странно что по заданию все в 1 тесте должно быть, а не раскидано по разным  .....
    page.should_be_name_in_basket_message()
    page.should_be_price_in_basket_message()

    # сравниваем имя продукта и имя в сообщении о добавлении в корзину
    page.should_be_equal_product_name_and_name_in_basket()

    # сравниваем цену продукта и цену в сообщении о добавлении в корзину
    page.should_be_equal_product_price_and_price_in_basket()

    # time.sleep(30)


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # Открываем страницу товара
    # Добавляем товар в корзину
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)  # инициализируем Page Object,
    page.open()
    page.add_product_to_basket()

    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    # Открываем страницу товара
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)  # инициализируем Page Object,
    page.open()

    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    # Открываем страницу товара
    # Добавляем товар в корзину
    # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)  # инициализируем Page Object,
    page.open()
    page.add_product_to_basket()

    page.should_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()





