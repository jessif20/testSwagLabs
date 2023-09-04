from selenium.webdriver.common.by import By


class IndexPageLocators:
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.ID, "login-button")
    ERROR_MSG = (By.XPATH, "//*[@id='login_button_container']/div/form/div[3]")
    ERROR_BUTTON = (By.CLASS_NAME, "error-button")




