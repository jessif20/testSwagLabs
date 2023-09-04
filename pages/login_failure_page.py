from pages.base_page import BasePage
from pages.login_failure_page_locators import LoginFailurePageLocators
from resources.constants import MAX_WAIT_INTERVAL


class LoginFailurePage(BasePage):

    def wait_and_type_user_name(self, usr_and_pw):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, LoginFailurePageLocators.USERNAME).send_keys(
            usr_and_pw[0])

    def type_password(self, usr_and_pw):
        self.find_element(LoginFailurePageLocators.PASSWORD).send_keys(
            usr_and_pw[1])

    def click_submit_btn(self):
        self.find_element(LoginFailurePageLocators.SUBMIT).click()

    def get_login_failure_label(self):
        lbl_login_failure_text = self.explicitly_wait_and_find_element(
            MAX_WAIT_INTERVAL, LoginFailurePageLocators.LOGIN_FAILURE_MESSAGE).text
        return lbl_login_failure_text


