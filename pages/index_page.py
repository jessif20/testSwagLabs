from pages.base_page import BasePage
from pages.index_page_locators import IndexPageLocators
from resources.constants import MAX_WAIT_INTERVAL


class IndexPage(BasePage):

    def wait_and_type_user_name(self, usr_and_pw):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.USERNAME).send_keys(
            usr_and_pw[0])

    def type_password(self, usr_and_pw):
        self.find_element(IndexPageLocators.PASSWORD).send_keys(
            usr_and_pw[1])

    def click_submit_btn(self):
        self.find_element(IndexPageLocators.SUBMIT).click()


