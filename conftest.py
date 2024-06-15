import pytest
from selenium import webdriver

import data


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get(data.MAIN_PAGE_URL)
    driver.maximize_window()
    yield driver
    driver.quit()
