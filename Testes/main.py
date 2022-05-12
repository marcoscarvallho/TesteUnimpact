from selenium import webdriver
import time
import sys

driver = webdriver.Chrome()
driver.get('https://unimpact2.herokuapp.com/lista-demandas')
time.sleep(1)
driver.find_element_by_xpath('//span[contains(text(), "Cadastro")]').click()
print("vai tentar agora")
time.sleep(1)
driver.find_element_by_xpath('//div[contains(text(), "Pessoa Jurídica")]').click()
time.sleep(2)
s = driver.find_elements_by_xpath("//input[@type='file']")
s[0].send_keys("C:\\Users\\moaci\\OneDrive\\Área de Trabalho\\tcc marcos\\TesteUnimpact\\Testes\\imgtest.jpg")