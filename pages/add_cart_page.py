from pages.base_page import BasePage
from pages.add_cart_page_locators import AddCartPageLocators
from resources.constants import MAX_WAIT_INTERVAL


class AddCartSuccessPage(BasePage):
    def verify_page_title(self):
        page_title = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, AddCartPageLocators.VERIFY_TITLE)
        page_title_text = page_title.text
        return page_title_text

    def item_display(self):
        cart_item = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, AddCartPageLocators.ITEM_NAME)
        check_cart = cart_item.text
        return check_cart

    def item_remove(self):
        remove_btn = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, AddCartPageLocators.REMOVE_BTN)
        remove_btn.click()
        cart_items = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                           AddCartPageLocators.REMOVE_ITEM_CART)
        cart_count = len(cart_items)
        return cart_count

    def continue_shop_link(self):
        clink = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, AddCartPageLocators.CONTINUE_LINK)

        clink.click()

    def click_checkout(self):
        check_btn = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, AddCartPageLocators.CHECKOUT)
        check_btn.click()
