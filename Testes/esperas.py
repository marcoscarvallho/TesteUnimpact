from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Esperas():
    
    def __init__(self, driver):
        self.driver = driver

    def porXpath(self, xpath):
        try:
            resposta = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
        except:
            print("Erro, busca nao encontrada")
            # self.driver.close()
            resposta = None
        finally:
            return resposta

    def porId(self, id):
        try:
            resposta = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, id))
            )
        except:
            print("Erro, busca nao encontrada")
            # self.driver.close()
            resposta = None
        finally:
            return resposta