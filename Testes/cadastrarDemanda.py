from esperas import Esperas
import time

class CadastrarDemanda():
    def __init__(self, driver, nome, descricao, data = None):
        self.driver = driver
        self.cadastrarDemanda(nome, descricao, data)
    
    def cadastrarDemanda(self, nome, descricao, data):
        botaoDemandas = Esperas.porXpath(self, '//p[contains(text(), "Dashboard")]')
        time.sleep(0.5)
        Esperas.porId(self, "search")
        self.driver.find_element_by_css_selector("[aria-label=add]").click()
        # self.driver.find_elements_by_tag_name("button")[2].click()
        inputTitulo = Esperas.porId(self, 'titulo')
        inputTitulo.send_keys(nome)
        self.driver.find_element_by_id("descricao").send_keys(descricao)
        if data != None:
            self.driver.find_element_by_id("dataLimite").send_keys(data)
        self.driver.find_element_by_id("ofereceInvestimento").click()
        self.driver.find_element_by_xpath("//span[contains(text(),'Salvar')]").click()
        time.sleep(0.5)