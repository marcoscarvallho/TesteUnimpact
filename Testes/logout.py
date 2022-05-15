from esperas import Esperas

class Logout():

    def __init__(self, driver):
        self.driver = driver
        self.logout()
    
    def logout(self):
        inputLogin = Esperas.porXpath(self, '//span[contains(text(), "Logout")]')
        inputLogin.click()
        