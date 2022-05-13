from selenium import webdriver
import time
from cadastroPessoaJuridica import CadastroPessoaJuridica
from cadastroPessoaFisica import CadastroPessoaFisica
from login import Login
from pesquisarDemanda import PesquisarDemanda
from fazerProposta import FazerProposta
from pesquisarEmpresa import PesquisarDemanda

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)
driver.get('https://unimpact2.herokuapp.com/lista-demandas')

Login(driver)
# CadastroPessoaFisica(driver)
# CadastroPessoaJuridica(driver)
# PesquisarDemanda(driver)
# FazerProposta(driver)
# PesquisarDemanda(driver)