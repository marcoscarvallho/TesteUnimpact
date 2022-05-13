from esperas import Esperas
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

class EditarDemanda():

    def __init__(self, driver):
        self.driver = driver
        self.editarDemanda()

    def editarDemanda(self):
        botaoProposta = Esperas.porXpath(self, '//span[contains(text(), "Editar")]')
        botaoProposta.click()
        modalContainerAux = self.driver.find_element_by_class_name('MuiDialog-root');
        tituloInput = modalContainerAux.find_element_by_id('titulo')
        tituloInput.send_keys(Keys.CONTROL,"a")
        tituloInput.send_keys(Keys.DELETE)
        tituloInput.send_keys('Teste título')
        descricaoPropostaInput = modalContainerAux.find_element_by_id('descricao')
        descricaoPropostaInput.send_keys(Keys.CONTROL,"a")
        descricaoPropostaInput.send_keys(Keys.DELETE)
        descricaoPropostaInput.send_keys('Teste descricao')
        dataPropostaInput = modalContainerAux.find_element_by_id('dataLimite')
        dataPropostaInput.send_keys('08071998')
        togle = modalContainerAux.find_element_by_id('ofereceInvestimento')
        togle.click()
        criar = modalContainerAux.find_element_by_xpath('//span[contains(text(), "Salvar")]')
        criar.click()