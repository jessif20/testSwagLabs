from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginSuccessPageLocators(BasePage):
    LOGIN_SUCCESS_TEXT = (By.XPATH, "//*[@id='header_container']/div[1]/div[2]/div")
    FIRST_ITEM_TEXT = (By.CSS_SELECTOR, "div.inventory_item:nth-child(1) div.inventory_item_name")

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.ID, "login-button")
    ERROR_MSG = (By.XPATH, "//*[@id='login_button_container']/div/form/div[3]")
    ERROR_BUTTON = (By.CLASS_NAME, "error-button")

    BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    BACKPACK = (By.XPATH, "//*[@id='item_4_title_link']/div")
    DISPLAY_FIRST_ITEM = (By.CSS_SELECTOR, "div.inventory_item:nth-child(1) div.inventory_item_name")

    LOGIN_SUCCESS_TEXT = (By.XPATH, "//*[@id='header_container']/div[1]/div[2]/div")
    PRODUCTS = (By.XPATH, "//*[@id='header_container']/div[2]/span")
    DROP_DOWN = (By.CSS_SELECTOR, "select.product_sort_container")
    BUTTON_ID = (By.ID, "add-to-cart-sauce-labs-onesie")
    REMOVE_BTN_ID = (By.ID, "remove-sauce-labs-onesie")
    ITEM_NAME_ONE = (By.ID, "add-to-cart-sauce-labs-bike-light")
    ADD_CART = (By.CSS_SELECTOR, "a.shopping_cart_link")
    ITEM_NAME = (By.CSS_SELECTOR, "#item_2_title_link:nth-child(1) div.inventory_item_name")
    DISPLAY_FIRST_ITEM = (By.CSS_SELECTOR, "div.inventory_item:nth-child(1) div.inventory_item_name")
    ITEM_PRICE = (By.XPATH, "//div[@class='inventory_item_price']")
    REMOVE_BTN_TEXT = (By.XPATH, "//button[text()='Remove']")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON = (By.XPATH, "//a[@class='shopping_cart_link']")
    INVENTORY_CONTAINER = (By.ID, "inventory_container")