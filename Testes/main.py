from selenium import webdriver
import time
from cadastroPessoaJuridica import CadastroPessoaJuridica
from cadastroPessoaFisica import CadastroPessoaFisica
from login import Login

driver = webdriver.Chrome()
driver.get('https://unimpact2.herokuapp.com/lista-demandas')
time.sleep(5)

# CadastroPessoaFisica(driver)
# CadastroPessoaJuridica(driver)
Login(driver)