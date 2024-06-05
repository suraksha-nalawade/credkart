import pytest
from selenium import webdriver


@pytest.fixture()
def setup(): # broswer invoke
    driver = webdriver.Chrome()
    driver.get("https://automation.credence.in")
    return driver

    #
    # yield
    # driver.quit()