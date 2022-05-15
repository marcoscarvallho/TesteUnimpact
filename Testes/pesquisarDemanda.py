from esperas import Esperas
import time

class PesquisarDemanda():
    def __init__(self, driver, demanda):
        self.driver = driver
        self.fazerPesquisa(demanda)
    
    def fazerPesquisa(self, demanda):
        barraPesquisa = Esperas.porId(self, "search")
        barraPesquisa.send_keys(demanda)
        time.sleep(1)
        self.driver.find_elements_by_tag_name("button")[1].click()