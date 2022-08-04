import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import Login
from pageObjects.DashBoard import DashBoard
from pageObjects.MenuItems import MenuItems
import time

class Test_01_login:
    baseURL = "https://www.saucedemo.com/"
    username = "performance_glitch_user"
    password = "secret_sauce"
    wrongusername = "locked_out_user"

    def test_loginPageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Swag Labs":
            assert True
        else:
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.db = DashBoard(self.driver)
        self.db.clickMenueButton()
        time.sleep(3)
        self.mi = MenuItems(self.driver)
        self.mi.clickLogoutButton()
        self.driver.close()


    def test_lockuser(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.wrongusername)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        element = self.driver.find_element(By.TAG_NAME, 'h3')
        if element.text == 'Epic sadface: Sorry, this user has been locked out.':
            assert True
        else:
            assert False

        self.driver.close()

