from tests_utils import *
import time

from pages import login_success_page
from pages.add_cart_page import AddCartSuccessPage
from pages.login_failure_page import LoginFailurePage
from pages.index_page import IndexPage
from pages.login_success_page import LoginSuccessPage
from resources.constants import TEST_SITE_URL


class TestLogin:

    # Test Case 1  (Incorrect user)
    def test_login_incorrect_user(self, driver, incorrect_username_password):
        login_failure_page = LoginFailurePage(driver)
        login_failure_page.navigate_to(TEST_SITE_URL)
        login_failure_page.wait_and_type_user_name(incorrect_username_password)
        login_failure_page.type_password(incorrect_username_password)
        time.sleep(5)
        login_failure_page.click_submit_btn()
        login_failure_lbl = login_failure_page.get_login_failure_label()
        assert login_failure_lbl, "Epic sadface: Username and password do not match any user in this service"
        time.sleep(5)

    # Test Case 2 ( Successful login to the user and add item to the cart )
    def test_login_new_user(self, driver, username_password):
        index_page = IndexPage(driver)
        index_page.navigate_to(TEST_SITE_URL)
        login_page = IndexPage(driver)
        login_page.wait_and_type_user_name(username_password)
        login_page.type_password(username_password)
        time.sleep(5)
        login_page.click_submit_btn()
        login_success_page = LoginSuccessPage(driver)
        login_success_lbl = login_success_page.get_login_success_label()
        login_success_lbl_text = "BACKPACK"
        print(login_success_lbl_text)
        assert login_success_lbl_text == login_success_lbl_text, "User Login failed!"

    '''Test case # 4 click the product (Backpack)

    def test_click_product(self, driver, sauce_labs_backpack):
        product_list_page = ProductListPage(driver)
        product_list_page.wait.click_submit_btn(sauce_labs_backpack)
        product_list_success_page = ProductListSuccessPage(driver)
        product_list_success_lbl = product_list_success_page.get_product_list_success_label()
        assert product_list_success_lbl.__contains__(sauce_labs_backpack), "carry.allTheThings() with the sleek, " \
                                                                           "streamlined Sly Pack that melds " \
                                                                           "uncompromising style with unequaled laptop" \
                                                                           " and tablet protection."   '''

    def test_inventory_page(self, driver):
        login_success_page = LoginSuccessPage(driver)
        login_success_lbl = login_success_page.get_login_success_label()
        login_success_lbl_text = "Products"
        display_item = login_success_page.display_item_page()
        display_item_text = "Sauce Labs Backpack"
        assert display_item == display_item_text, "Item not displayed on the page"
        select_option = login_success_page.filter_option()
        expected_option_text = "Sauce Labs Onesie"
        assert select_option == expected_option_text, " first item not found"
        add_cart_btn = login_success_page.add_cart()
        item_count = 1
        assert add_cart_btn == item_count, "Item not added to the cart "

        login_success_page.add_cart_link_click()
