from esperas import Esperas
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from acompanharDemandas import AcompanharDemandas

import time

class EditarDemanda():

    def __init__(self, driver, demanda, titulo, descricao, data, investimento=None):
        self.driver = driver
        self.editarDemanda(demanda, titulo, descricao, data, investimento)

    def editarDemanda(self, demanda, titulo, descricao, data, investimento):
        AcompanharDemandas(self.driver, demanda)
        time.sleep(1)
        botaoProposta = Esperas.porXpath(self, '//span[contains(text(), "Editar")]')
        botaoProposta.click()
        modalContainerAux = self.driver.find_element_by_class_name('MuiDialog-root');
        tituloInput = modalContainerAux.find_element_by_id('titulo')
        tituloInput.send_keys(Keys.CONTROL,"a")
        tituloInput.send_keys(Keys.DELETE)
        tituloInput.send_keys(titulo)
        descricaoPropostaInput = modalContainerAux.find_element_by_id('descricao')
        descricaoPropostaInput.send_keys(Keys.CONTROL,"a")
        descricaoPropostaInput.send_keys(Keys.DELETE)
        descricaoPropostaInput.send_keys(descricao)
        dataPropostaInput = modalContainerAux.find_element_by_id('dataLimite')
        dataPropostaInput.send_keys(data)
        if investimento != None:
            togle = modalContainerAux.find_element_by_id('ofereceInvestimento')
            togle.click()
        criar = modalContainerAux.find_element_by_xpath('//span[contains(text(), "Salvar")]')
        criar.click()
        time.sleep(2)
        AcompanharDemandas(self.driver, titulo)
        time.sleep(2)
        try:
            x = self.driver.find_element_by_xpath('//p[contains(text(), "'+titulo+'")]')
        except:
            x = None
        print (x)
        assert x != None, 'Falha na edição da demanda'
        print('Editado com sucesso')