from esperas import Esperas
from selenium import webdriver

import time

class FazerProposta():

    def __init__(self, driver, titulo, descricao, data, investimento=None):
        self.driver = driver
        self.fazerProposta(titulo, descricao, data, investimento)

    def fazerProposta(self, titulo, descricao, data, investimento=None):
        botaoProposta = Esperas.porXpath(self, '//span[contains(text(), "Fazer Proposta")]')
        botaoProposta.click()
        modalContainerAux = self.driver.find_element_by_class_name('MuiDialog-root');
        tituloInput = modalContainerAux.find_element_by_id('titulo')
        tituloInput.send_keys(titulo)
        descricaoPropostaInput = modalContainerAux.find_element_by_id('descricao')
        descricaoPropostaInput.clear
        descricaoPropostaInput.send_keys(descricao)
        dataPropostaInput = modalContainerAux.find_element_by_id('dataPrevista')
        dataPropostaInput.send_keys(data)
        if investimento != None:
            togle = modalContainerAux.find_element_by_id('precisaInvestimento')
            togle.click()
        criar = modalContainerAux.find_element_by_xpath('//span[contains(text(), "Criar")]')
        criar.click()
        x = Esperas.porXpath(self, '//[contains(text(), "Proposta criada com sucesso! Aguarde retorno do demandante.")]')
        assert x == None, 'Falha ao fazer proposta'
