from esperas import Esperas
import time

class FazerProposta():

    def __init__(self, driver):
        self.driver = driver
        self.fazerProposta()

    def fazerProposta(self):
        botaoProposta = Esperas.porXpath(self, '//span[contains(text(), "Fazer Proposta")]')
        botaoProposta.click()
        tituloPropostaInput = Esperas.porId(self, 'titulo-label')
        time.sleep(2)
        self.driver.switch_to().alert()
        tituloPropostaInput.clear()
        tituloPropostaInput.send_keys('Teste título')
        descricaoPropostaInput = self.find_element_by_id('descricao-label')
        descricaoPropostaInput.clear()
        descricaoPropostaInput.send_keys('Teste descricao')
        dataPropostaInput = self.find_element_by_id('dataPrevista')
        dataPropostaInput.clear()
        dataPropostaInput.send_keys('08/07/2010')