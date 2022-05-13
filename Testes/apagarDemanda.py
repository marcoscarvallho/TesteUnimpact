
from esperas import Esperas
import time
from acompanharDemandas import AcompanharDemandas

class ApagarDemanda():
    def __init__(self, driver):
        self.driver = driver
        self.apagar()
    
    def apagar(self):
        AcompanharDemandas(self.driver, 'aa')
        time.sleep(1)
        botaoApagar = Esperas.porXpath(self, '//span[contains(text(), "Apagar")]')
        botaoApagar.click()
        botaoConfirmar = Esperas.porXpath(self, '//span[contains(text(), "Confirmar")]')
        botaoConfirmar.click()