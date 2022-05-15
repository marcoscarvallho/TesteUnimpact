from acompanharDemandas import AcompanharDemandas
from esperas import Esperas
import time

class AdicionarMilestone():
    def __init__(self, driver, demanda, titulo, descricao):
        self.driver = driver
        self.adicionarMilestone(demanda, titulo, descricao)
    
    def adicionarMilestone(self, demanda, titulo, descricao):
        AcompanharDemandas(self.driver, demanda)
        time.sleep(1)    
        botaoProposta = Esperas.porXpath(self, '//span[contains(text(), "adicionar milestone")]')
        botaoProposta.click()
        inputTitulo = Esperas.porId(self, 'milestone')
        inputTitulo.send_keys(titulo)
        self.driver.find_element_by_id("description").send_keys(descricao)
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//span[contains(text(), "Salvar")]').click()
        time.sleep(0.5)