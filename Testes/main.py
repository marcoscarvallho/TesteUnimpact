from selenium import webdriver
import time
from cadastroPessoaJuridica import CadastroPessoaJuridica
from cadastroPessoaFisica import CadastroPessoaFisica
from login import Login
from esperas import Esperas
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
    # driver = webdriver.Firefox()
    driver.get('https://unimpact2.herokuapp.com/login')
    resp = Esperas.porId(driver, "login")
    if resp == None:
        driver.get('https://unimpact2.herokuapp.com/login')
        resp = Esperas.porId(driver, "login")
    # CadastroPessoaFisica(driver, 'aaaa', 'teste1', '人t123@ll', '人testandinho', '人11237666666', '人81995688622')
    # CadastroPessoaJuridica(driver, 'testecnpj', 'senhacnpj', 'email@cnpj', 'nomecnpj', 'razaocnpj', '81994588543', 'institutoo', '12312312312312', 'razaoempresa', 'vagabundo')
    Login(driver, 'testeLogin', 'testeSenha')
    # PesquisarDemanda(driver, 'Desenvolver software de biblioteca')
    # FazerProposta(driver, 'eita', 'eu tenho interesse nessa vaga', '04061997', True)
    # PesquisarEmpresa(driver, 'amazon')
    # EditarPerfil(driver, 'Email@ab', 'nome123', '40028922', 'som do japones')
    # AcompanharDemandas(driver ,'adsdasdasdadsa')
    # AceitarProposta(driver, 'data invalida')
    # CadastrarDemanda(driver, 'Criado pelo git', 'git actions', '04061997')
    ApagarDemanda(driver, 'Criado pelo git')
    # EditarDemanda(driver, 'demandada', 'deu certo', 'erro', '04061997')
    # AdicionarMilestone(driver, 'demandada', 'vamos adicionar', 'descricao vem bem aqui')
    # ApagarDemanda(driver, 'Teste título')
    Logout(driver)
    driver.close()

