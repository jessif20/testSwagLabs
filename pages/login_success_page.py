import time

import self
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from pages.login_success_page_locators import LoginSuccessPageLocators
from resources.constants import MAX_WAIT_INTERVAL
from selenium.common.exceptions import StaleElementReferenceException


class LoginSuccessPage(BasePage):

    def get_login_success_label(self):
        lbl_login_success_txt = self.explicitly_wait_and_find_element(
            MAX_WAIT_INTERVAL, LoginSuccessPageLocators.BACKPACK).text
        return lbl_login_success_txt

    def display_item_page(self):
        lbl_product_display_txt = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                                        LoginSuccessPageLocators.DISPLAY_FIRST_ITEM)
        # ITEM_NAME
        lbl_product_name = lbl_product_display_txt.text
        return lbl_product_name

    def get_product_lbl(self):
        product_lbl = self.explicitly_wait_and_find_element(
            MAX_WAIT_INTERVAL, LoginSuccessPageLocators.PRODUCTS).click
        return product_lbl

    def add_cart(self):
        add_to_cart_btn = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                                LoginSuccessPageLocators.BUTTON_ID)

    def wait_and_type_user_name(self, usr_and_pw):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, LoginSuccessPageLocators.USERNAME).send_keys(
            usr_and_pw[0])

    def type_password(self, usr_and_pw):
        self.find_element(LoginSuccessPageLocators.PASSWORD).send_keys(
            usr_and_pw[1])

    def click_submit_btn(self):
        self.find_element(LoginSuccessPageLocators.SUBMIT).click()

    def filter_option(self):

        dropdown = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, LoginSuccessPageLocators.DROP_DOWN)
        dropdown.click()
        time.sleep(5)
        '''dropdown = Select(
            self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, LoginSuccessPageLocators.DROP_DOWN))
        dropdown.select_by_visible_text("Price (low to high)")'''

        time.sleep(2)

        try:

            dropdown = Select(
                self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, LoginSuccessPageLocators.DROP_DOWN))
            dropdown.select_by_visible_text("Price (low to high)")

            time.sleep(2)

            first_item = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                               LoginSuccessPageLocators.FIRST_ITEM_TEXT)
            first_item_text = first_item.text

            return first_item_text

        except StaleElementReferenceException as e:
            # Refresh the page and search for the element again
            print("Error occurred: ", e)
            return None

    def add_cart(self):
        try:
            add_to_cart_btn = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                                    LoginSuccessPageLocators.BUTTON_ID)

            add_to_cart_btn.click()
            time.sleep(2)
            '''add_to_cart_btn1 = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                                     LoginSuccessPageLocators.ITEM_NAME_ONE)

            add_to_cart_btn1.click()'''

            cart_button = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, LoginSuccessPageLocators.CART_ICON)
            add_cart_button = int(cart_button.text)
            return add_cart_button

        except StaleElementReferenceException as e:
            print("Error occurred: ", e)

    def add_cart_link_click(self):
        add_cart_link = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, LoginSuccessPageLocators.ADD_CART)
        add_cart_link.click()

    def get_item_price(self):
        item_price = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, LoginSuccessPageLocators.ITEM_PRICE)
        return item_price.text
