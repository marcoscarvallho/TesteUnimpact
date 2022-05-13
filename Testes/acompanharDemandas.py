from inspect import _void
from esperas import Esperas
import time

class AcompanharDemandas():

    def __init__(self, driver, str = None):
        self.driver = driver
        if str == None:
            str == 'cc'
        self.demandas(str)
    
    def demandas(self, str):
        botaoDemandas = Esperas.porXpath(self, '//p[contains(text(), "Minhas Demandas")]')
        time.sleep(1)
        botaoDemandas.click()
        barraPesquisa = Esperas.porId(self, "search")
        barraPesquisa.send_keys(str)
        time.sleep(1)
        self.driver.find_elements_by_tag_name("button")[1].click()