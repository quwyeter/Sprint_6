from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_url(self, geturl):
        self.driver.get(geturl)

    def find_element_by_locator_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_to_element(self, locator):
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def add_text_to_element(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.driver.find_element(*locator).text

    def current_url(self):
        return self.driver.current_url

    def wait_for_visibility(self, locator):
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(locator))

    def wait_url(self, url):
        WebDriverWait(self.driver, 5).until(ec.url_to_be(url))

    def switch_window(self):
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
