import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# region Constants
SEARCH_INPUT_XPATH = '//*[@id="APjFqb"]'
CLEAR_SEARCH_INPUT_BUTTON_SELECTOR = 'div.BKRPef > div'
IMAGE_SEARCH_BUTTON_SELECTOR = 'div.nDcEnd > svg'
IMAGE_SEARCH_URL_INPUT_SELECTOR = 'div.PXT6cd > input'
# endregion

class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.google.com/")

    def search_for(self, keyword):
        search_input = self.driver.find_element(By.XPATH, SEARCH_INPUT_XPATH)
        search_input.send_keys(keyword)
        search_input.send_keys(Keys.ENTER)
        time.sleep(1)

    def clear_search_input(self):
        search_input = self.driver.find_element(By.XPATH, SEARCH_INPUT_XPATH)
        clear_button = self.driver.find_element(By.CSS_SELECTOR, CLEAR_SEARCH_INPUT_BUTTON_SELECTOR)
        search_input.send_keys('Python')
        clear_button.click()

    def get_search_input_value(self):
        search_input = self.driver.find_element(By.XPATH, SEARCH_INPUT_XPATH)
        return search_input.text


    def click_image_search(self):
        image_search_button = self.driver.find_element(By.CSS_SELECTOR, IMAGE_SEARCH_BUTTON_SELECTOR)
        image_search_button.click()
        time.sleep(0.5)

    def perform_image_search(self, image_url):
        self.click_image_search()
        image_link_input = self.driver.find_element(By.CSS_SELECTOR, IMAGE_SEARCH_URL_INPUT_SELECTOR)
        image_link_input.send_keys(image_url)
        image_link_input.send_keys(Keys.ENTER)