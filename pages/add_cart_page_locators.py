from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AddCartPageLocators(BasePage):
    ADD_CART = (By.CSS_SELECTOR, "a.shopping_cart_link")
    ITEM_NAME = (By.XPATH, "//*[@id='item_2_title_link']")
    CHECKOUT = (By.ID, "checkout")
    VERIFY_TITLE = (By.XPATH, "//span[@class='title']")
    # REMOVE_BTN = (By.XPATH, "//button[text()='REMOVE']")
    REMOVE_BTN = (By.ID, "remove-sauce-labs-onesie")
    # REMOVE_BTN = (By.ID, "remove-sauce-labs-bike-light")
    # REMOVE_ITEM_CART = (By.CLASS_NAME, "shopping_cart_link")

    REMOVE_ITEM_CART = (By.XPATH, "//div[@class='cart_item']")
    CONTINUE_LINK = (By.XPATH, "//a[text()='Continue Shopping']")
    CART_COUNT = (By.XPATH, "//span[@class='shopping_cart_badge']")