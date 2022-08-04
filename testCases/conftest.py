import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup():
    # driver = webdriver.Chrome(executable_path=r"C:/Users/malik/OneDrive/Desktop/Webdriver/chromedriver.exe")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    return driver

