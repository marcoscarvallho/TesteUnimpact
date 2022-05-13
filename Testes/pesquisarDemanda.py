import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from esperas import Esperas

class PesquisarDemanda():
    def __init__(self, driver):
        self.driver = driver
        self.fazerPesquisa()
    
    def fazerPesquisa(self):
        barraPesquisa = Esperas.porXpath(self, "search")
        barraPesquisa.send_keys("Construção")
        time.sleep(1)
        self.driver.find_elements_by_tag_name("button")[1].click()