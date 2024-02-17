import pytest
import sys
import os
from conftest import browser

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.search_page import SearchPage

# region Constants
IMAGE_URL = 'https://www.theglobeandmail.com/resizer/gew4suGzG44SaHLq5yXVIoEY3Qc=/arc-anglerfish-tgam-prod-tgam/public/2XCT3JN7ZRGMNAFSMZM2RSTH2I.jpeg'
SCREENSHOT_FOLDER_PATH = os.path.join(RESULTS_FOLDER_PATH, 'screenshots')
RESULTS_FOLDER_PATH = './results'
# endregion


# region test cases
def test_search_input(browser):
    search_page = SearchPage(browser)
    search_page.open()
    search_page.search_for('Python')
    browser.save_screenshot(os.path.join(SCREENSHOT_FOLDER_PATH, 'test_search_input.png'))

    assert "Python" in browser.page_source

def test_clear_input_button(browser):
    search_page = SearchPage(browser)
    search_page.open()
    search_page.clear_search_input()
    browser.save_screenshot(os.path.join(SCREENSHOT_FOLDER_PATH, 'test_clear_input_button.png'))

    assert search_page.get_search_input_value() == ''

def test_image_search(browser):
    search_page = SearchPage(browser)
    search_page.open()
    search_page.perform_image_search(IMAGE_URL)
    browser.save_screenshot(os.path.join(SCREENSHOT_FOLDER_PATH, 'test_image_search.png'))

    assert "honda" in browser.page_source
# endregion

if __name__ == "__main__":
    pytest.main(["-v", "--html=" + RESULTS_FOLDER_PATH + '/report.html'])
