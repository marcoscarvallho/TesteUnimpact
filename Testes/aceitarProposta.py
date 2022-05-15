from acompanharDemandas import AcompanharDemandas
from esperas import Esperas
from selenium.webdriver.common.alert import Alert
import time

class AceitarProposta():
    def __init__(self, driver, demanda):
        self.driver = driver
        self.aceitar(demanda)
    
    def aceitar(self, demanda):
        AcompanharDemandas(self.driver, demanda)
        time.sleep(1)
        botaoPropostas = Esperas.porXpath(self, '//p[contains(text(), "Propostas:")]/..')
        time.sleep(1)
        botaoPropostas.click()
        botaoAceitar = Esperas.porXpath(self, '//span[contains(text(), "Aceitar Proposta")]')
        botaoAceitar.click()
        botaoConfirmar = Esperas.porXpath(self, '//span[contains(text(), "Confirmar")]')
        botaoConfirmar.click()