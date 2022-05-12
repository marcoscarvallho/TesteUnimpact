from selenium import webdriver
import time
import sys
from cadastroPessoaJuridica import CadastroPessoaJuridica

class main():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.get('https://unimpact2.herokuapp.com/lista-demandas')
    time.sleep(1)
    CadastroPessoaJuridica(driver)