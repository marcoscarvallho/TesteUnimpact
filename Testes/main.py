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
from logout import Logout




class Main():

    options = webdriver.ChromeOptions() 
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get('https://unimpact2.herokuapp.com/lista-demandas')
    # CadastroPessoaFisica(driver, 'testeMain2', 'teste', 't@ll', 'testandinho', '11237666666', '81995688622')
    # CadastroPessoaJuridica(driver, 'testecnpj', 'senhacnpj', 'email@cnpj', 'nomecnpj', 'razaocnpj', '81994588543', 'institutoo', '12312312312312', 'razaoempresa', 'vagabundo')
    Login(driver, 'testeLogin', 'testeSenha')
    PesquisarDemanda(driver, 'data invalida')
    # FazerProposta(driver)
    # PesquisarEmpresa(driver)
    # EditarPerfil(driver)
    # AcompanharDemandas(driver ,'adsdasdasdadsa')
    # AceitarProposta(driver)
    # ApagarDemanda(driver)
    # EditarDemanda(driver)
    # CadastrarDemanda(driver, 'teste12', 'descricao', '04061997')
    Logout(driver)
    # driver.close()

