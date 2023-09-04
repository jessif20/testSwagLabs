from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginFailurePageLocators(BasePage):

    PRODUCT = (By.XPATH, "//*[@id='header_container']/div[2]/span")
    DROP_DOWN = (By.CSS_SELECTOR, "select.product_sort_container")
    FIRST_ITEM_TEXT = (By.CSS_SELECTOR, "div.inventory_item:nth-child(1) div.inventory_item_name")
    LOGIN_FAILURE_MESSAGE = (By.XPATH, "//h3")

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.ID, "login-button")