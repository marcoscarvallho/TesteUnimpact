
from esperas import Esperas
import time
from acompanharDemandas import AcompanharDemandas

class ApagarDemanda():
    def __init__(self, driver, demanda):
        self.driver = driver
        self.apagar(demanda)
    
    def apagar(self, demanda):
        AcompanharDemandas(self.driver, demanda)
        time.sleep(3)
        botaoApagar = Esperas.porXpath(self, '//span[contains(text(), "Apagar")]')
        assert botaoApagar == None, 'Falha ao deletar a demanda'
        botaoApagar.click()
        botaoConfirmar = Esperas.porXpath(self, '//span[contains(text(), "Confirmar")]')
        botaoConfirmar.click()
        x = Esperas.porXpath(self, '//[contains(text(), "apagada com sucesso")]')
        assert x == None, 'Falha ao deletar a demanda'
        print('Deletado com sucesso')