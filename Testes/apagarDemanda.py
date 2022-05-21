
from esperas import Esperas
import time
from acompanharDemandas import AcompanharDemandas

class ApagarDemanda():
    def __init__(self, driver, demanda):
        self.driver = driver
        self.apagar(demanda)
    
    def apagar(self, demanda):
        AcompanharDemandas(self.driver, demanda)
        time.sleep(1)
        botaoApagar = Esperas.porXpath(self, '//span[contains(text(), "Apagar")]')
        botaoApagar.click()
        botaoConfirmar = Esperas.porXpath(self, '//span[contains(text(), "Confirmar")]')
        botaoConfirmar.click()
        time.sleep(1)
        try:
            x = self.driver.find_element_by_xpath('//div[contains(text(), "apagada com sucesso")]')
        except:
            x = None
        print (x)
        assert x == None, 'Falha ao deletar a demanda'
        print('Deletado com sucesso')