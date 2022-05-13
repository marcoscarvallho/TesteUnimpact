from esperas import Esperas

class Login():

    def __init__(self, driver):
        self.driver = driver
        self.inicioLogin()
    
    def inicioLogin(self):
        inputLogin = Esperas.porId(self, "login")
        inputLogin.send_keys("testeLogin")
        self.driver.find_element_by_id("password").send_keys("testeSenha")
        self.driver.find_element_by_xpath('//span[contains(text(), "Entrar")]').click()