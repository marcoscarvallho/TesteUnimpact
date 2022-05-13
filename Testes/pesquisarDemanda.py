from esperas import Esperas
import time

class PesquisarDemanda():
    def __init__(self, driver):
        self.driver = driver
        self.fazerPesquisa()
    
    def fazerPesquisa(self):
        barraPesquisa = Esperas.porId(self, "search")
        barraPesquisa.send_keys("Construção")
        time.sleep(1)
        self.driver.find_elements_by_tag_name("button")[1].click()