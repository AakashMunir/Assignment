from selenium import webdriver
from selenium.webdriver.common.by import By

class Login:
    text_username_id = "user-name"
    text_password_id = "password"
    button_login_id = "login-button"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.text_username_id).clear()
        self.driver.find_element(By.ID, self.text_username_id).send_keys(username)
        # self.driver.find_element_by_id(self.text_username_id).clear()
        # self.driver.find_element_by_id(self.text_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.text_password_id).clear()
        self.driver.find_element(By.ID, self.text_password_id).send_keys(password)


    def clickLogin(self):
        self.driver.find_element(By.ID, self.button_login_id).click()