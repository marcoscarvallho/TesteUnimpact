from esperas import Esperas
import time

class Login():

    def __init__(self, driver, login, senha):
        self.driver = driver
        self.inicioLogin(login, senha)
    
    def inicioLogin(self, login, senha):
        inputLogin = Esperas.porId(self, "login")
        inputLogin.send_keys(login)
        self.driver.find_element_by_id("password").send_keys(senha)
        self.driver.find_element_by_xpath('//span[contains(text(), "Entrar")]').click()
        x = Esperas.porXpath(self, '//span[contains(text(), "Logout")]')
        print (x)
        assert x != None, 'Falha no login'
        print('Logado com sucesso')