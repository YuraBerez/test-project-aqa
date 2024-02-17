import pytest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# region Contants
IMAGE_URL = 'https://www.theglobeandmail.com/resizer/gew4suGzG44SaHLq5yXVIoEY3Qc=/arc-anglerfish-tgam-prod-tgam/public/2XCT3JN7ZRGMNAFSMZM2RSTH2I.jpeg'
RESULTS_FOLDER_PATH = './results'
SCREENSHOT_FOLDER_PATH = os.path.join(RESULTS_FOLDER_PATH, 'screenshots') 

SEARCH_INPUT_XPATH = '//*[@id="APjFqb"]'
CLEAR_SEARCH_INPUT_BUTTON_SELECTOR = 'div.BKRPef > div'
IMAGE_SEARCH_BUTTON_SELECTOR = 'div.nDcEnd > svg'
IMAGE_SEARCH_URL_INPUT_SELECTOR = 'div.PXT6cd > input'
# endregion

@pytest.fixture
def browser():
    if not os.path.exists(RESULTS_FOLDER_PATH):
        os.makedirs(RESULTS_FOLDER_PATH)

    if not os.path.exists(SCREENSHOT_FOLDER_PATH):
        os.makedirs(SCREENSHOT_FOLDER_PATH)

    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_search_input(browser):
    browser.get("https://www.google.com/")
    search_input = browser.find_element(By.XPATH, SEARCH_INPUT_XPATH)
    search_input.send_keys('Python')
    search_input.send_keys(Keys.ENTER)
    time.sleep(1)
    browser.save_screenshot(os.path.join(SCREENSHOT_FOLDER_PATH, 'test_search_input.png'))

    assert "Python" in browser.page_source

def test_clear_input_button(browser):
    browser.get("https://www.google.com/")
    search_input = browser.find_element(By.XPATH, SEARCH_INPUT_XPATH)
    clear_button = browser.find_element(By.CSS_SELECTOR, CLEAR_SEARCH_INPUT_BUTTON_SELECTOR)
    search_input.send_keys('Python')
    clear_button.click()
    browser.save_screenshot(os.path.join(SCREENSHOT_FOLDER_PATH, 'test_clear_input_button.png'))

    assert search_input.text == ''

def test_image_search(browser):
    browser.get("https://www.google.com/")
    image_search_button = browser.find_element(By.CSS_SELECTOR, IMAGE_SEARCH_BUTTON_SELECTOR) 
    image_search_button.click()
    time.sleep(0.5)
    browser.save_screenshot(os.path.join(SCREENSHOT_FOLDER_PATH, 'test_image_search_1.png'))
    image_link_input = browser.find_element(By.CSS_SELECTOR, IMAGE_SEARCH_URL_INPUT_SELECTOR)
    image_link_input.send_keys(IMAGE_URL)
    image_link_input.send_keys(Keys.ENTER)
    browser.save_screenshot(os.path.join(SCREENSHOT_FOLDER_PATH, 'test_image_search_2.png'))

    print(os.path.join(SCREENSHOT_FOLDER_PATH, 'test_image_search_2.png'))

    assert "honda" in browser.page_source

if __name__ == "__main__":
    pytest.main(["-v", "--html=" + RESULTS_FOLDER_PATH + '/report.html'])

