from selenium import webdriver
from selenium.webdriver.common.by import By

class MenuItems:
    logout_button = "logout_sidebar_link"

    def __init__(self, driver):
        self.driver = driver

    def clickLogoutButton(self):
        self.driver.find_element(By.ID, self.logout_button).click()
