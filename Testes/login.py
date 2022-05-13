from esperas import Esperas

class Login():

    def __init__(self, driver):
        self.driver = driver
        self.inicioLogin()
    
    def inicioLogin(self):
        inputLogin = Esperas.porId(self, "login")
        inputLogin.send_keys("juliaamato10@gmail.com")
        self.driver.find_element_by_id("password").send_keys("123456")
        self.driver.find_element_by_xpath('//span[contains(text(), "Entrar")]').click()