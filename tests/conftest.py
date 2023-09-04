import pytest as pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def username_password():
    user_name = "standard_user"
    password = "secret_sauce"
    return [user_name, password]


@pytest.fixture(scope="module")
def driver():
    _driver = webdriver.Chrome()
    yield _driver
    _driver.quit()


@pytest.fixture(scope="function")
def incorrect_username_password():
    user_name = "standard_person"
    password = "secret_recipe"
    return [user_name, password]


@pytest.fixture(scope="function")
def incorrect_username_correct_password():
    wrong_user_name = "Standard"
    correct_password = "secret"
    return [wrong_user_name, correct_password]