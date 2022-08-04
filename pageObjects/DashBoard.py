from selenium import webdriver
from selenium.webdriver.common.by import By

class DashBoard:
    button_menu = "react-burger-menu-btn"

    def __init__(self, driver):
        self.driver = driver

    def clickMenueButton(self):
        self.driver.find_element(By.ID, self.button_menu).click()