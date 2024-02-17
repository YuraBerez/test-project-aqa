import os
import pytest
from selenium import webdriver

RESULTS_FOLDER_PATH = './results'
SCREENSHOT_FOLDER_PATH = os.path.join(RESULTS_FOLDER_PATH, 'screenshots')

@pytest.fixture
def browser():
    if not os.path.exists(RESULTS_FOLDER_PATH):
        os.makedirs(RESULTS_FOLDER_PATH)

    if not os.path.exists(SCREENSHOT_FOLDER_PATH):
        os.makedirs(SCREENSHOT_FOLDER_PATH)

    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# command for executions test
# pytest --html=results/test-results.html;