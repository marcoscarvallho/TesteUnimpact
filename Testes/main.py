from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get('https://unimpact2.herokuapp.com/lista-demandas')
time.sleep(5)
driver.find_element_by_xpath('//span[contains(text(), "Cadastro")]').click()