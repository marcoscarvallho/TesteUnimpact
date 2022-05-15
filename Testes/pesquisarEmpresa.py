from esperas import Esperas
import time

class PesquisarEmpresa():
    def __init__(self, driver, empresa):
        self.driver = driver
        self.fazerPesquisa(empresa)
    
    def fazerPesquisa(self, empresa):
        botaoInstituicao = Esperas.porXpath(self, '//p[contains(text(), "Instituições")]')
        botaoInstituicao.click()
        barraPesquisa = Esperas.porId(self, "search")
        barraPesquisa.send_keys(empresa)
        time.sleep(1)
        self.driver.find_elements_by_tag_name("button")[1].click()