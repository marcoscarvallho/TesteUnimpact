from esperas import Esperas
import time

class CadastrarDemanda():
    def __init__(self, driver, nome = None, descricao = None, data = None):
        self.driver = driver
        if nome == None:
            nome = 'aa'
        if descricao == None:
            descricao = 'aaaaaaa'
        self.cadastrarDemanda(nome, descricao, data)
    
    def cadastrarDemanda(self, nome, descricao, data = None):
        Esperas.porId(self, "search")
        self.driver.find_elements_by_tag_name("button")[2].click()
        inputTitulo = Esperas.porId(self, 'titulo')
        inputTitulo.send_keys(nome)
        self.driver.find_element_by_id("descricao").send_keys(descricao)
        if data != None:
            self.driver.find_element_by_id("dataLimite").send_keys(data)
        self.driver.find_element_by_id("ofereceInvestimento").click()
        self.driver.find_element_by_xpath("//span[contains(text(),'Salvar')]").click()