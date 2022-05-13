from selenium import webdriver
import time
import sys

class Login():
    def __init__(self, driver):
        self.driver = driver
        self.inicioLogin()
    
    def inicioLogin(self):
        self.driver.find_element_by_id("login").send_keys("testeLogin")
        self.driver.find_element_by_id("password").send_keys("testeSenha")
        self.driver.find_element_by_xpath('//span[contains(text(), "Entrar")]').click()