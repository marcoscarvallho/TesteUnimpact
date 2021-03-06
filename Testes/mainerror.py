from selenium import webdriver
import time
from cadastroPessoaJuridica import CadastroPessoaJuridica
from cadastroPessoaFisica import CadastroPessoaFisica
from login import Login
from pesquisarDemanda import PesquisarDemanda
from fazerProposta import FazerProposta
from pesquisarEmpresa import PesquisarEmpresa
from editarPerfil import EditarPerfil
from aceitarProposta import AceitarProposta
from acompanharDemandas import AcompanharDemandas
from apagarDemanda import ApagarDemanda
from cadastrarDemanda import CadastrarDemanda
from editarDemanda import EditarDemanda

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)
driver.get('https://unimpact2.herokuapp.com/lista-demandas')

Login(driver)
# CadastroPessoaFisica(driver)
# CadastroPessoaJuridica(driver)
# PesquisarDemanda(driver)
# FazerProposta(driver)
# PesquisarEmpresa(driver)
# EditarPerfil(driver)
# AcompanharDemandas(driver ,'aa')
# AceitarProposta(driver)
# ApagarDemanda(driver)
# EditarDemanda(driver)
# CadastrarDemanda(driver, 'teste12', 'descricao', '04061997')

# driver.close()