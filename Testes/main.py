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
from adicionarMilestone import AdicionarMilestone
from logout import Logout




class Main():

    options = webdriver.ChromeOptions() 
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get('https://unimpact2.herokuapp.com/lista-demandas')
    # CadastroPessoaFisica(driver, '人testeMain2', '人teste', '人t@ll', '人testandinho', '人11237666666', '人81995688622')
    # CadastroPessoaJuridica(driver, 'testecnpj', 'senhacnpj', 'email@cnpj', 'nomecnpj', 'razaocnpj', '81994588543', 'institutoo', '12312312312312', 'razaoempresa', 'vagabundo')
    Login(driver, 'testeLogin', 'testeSenha')
    # PesquisarDemanda(driver, 'data invalida')
    # FazerProposta(driver, 'eita', 'eu tenho interesse nessa vaga', '04061997', True)
    # PesquisarEmpresa(driver, 'amazon')
    # EditarPerfil(driver, 'Email@a', 'nome', '40028922', 'som do japones')
    # AcompanharDemandas(driver ,'adsdasdasdadsa')
    # AceitarProposta(driver, 'data invalida')
    # ApagarDemanda(driver, 'Teste título')
    # EditarDemanda(driver, 'invalida data', 'data invalida', 'erro', '04061997')
    # CadastrarDemanda(driver, 'teste12', 'descricao', '04061997')
    # AdicionarMilestone(driver, 'Teste título', 'vamos adicionar', 'descricao vem bem aqui')
    # ApagarDemanda(driver, 'Teste título')
    # time.sleep(5)
    # Logout(driver)
    # time.sleep(3)
    # driver.close()

