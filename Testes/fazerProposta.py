from esperas import Esperas
from selenium import webdriver

import time

class FazerProposta():

    def __init__(self, driver):
        time.sleep(20)
        self.driver = driver
        self.fazerProposta()

    def fazerProposta(self):
        botaoProposta = Esperas.porXpath(self, '//span[contains(text(), "Fazer Proposta")]')
        botaoProposta.click()
        modalContainerAux = self.driver.find_element_by_class_name('MuiDialog-root');
        tituloInput = modalContainerAux.find_element_by_id('titulo')
        tituloInput.send_keys('Teste título')
        time.sleep(2)
        descricaoPropostaInput = modalContainerAux.find_element_by_id('descricao')
        descricaoPropostaInput.clear
        descricaoPropostaInput.send_keys('Teste descricao')
        dataPropostaInput = modalContainerAux.find_element_by_id('dataPrevista')
        dataPropostaInput.send_keys('08071998')
        togle = modalContainerAux.find_element_by_id('precisaInvestimento')
        togle.click()
        criar = modalContainerAux.find_element_by_xpath('//span[contains(text(), "Criar")]')
        criar.click()