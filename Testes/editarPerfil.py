from esperas import Esperas
from selenium.webdriver.common.keys import Keys

class EditarPerfil():
    def __init__(self, driver):
        self.driver = driver
        self.editar()
    
    def editar(self):
        botaoPerfil = Esperas.porXpath(self, '//p[contains(text(), "Meu Perfil")]')
        botaoPerfil.click()
        campoEmail = self.driver.find_element_by_id('email')
        campoEmail.send_keys(Keys.CONTROL,"a")
        campoEmail.send_keys(Keys.DELETE)
        campoEmail.send_keys('Email@a')
        campoNome = self.driver.find_element_by_id('nome')
        campoNome.send_keys(Keys.CONTROL,"a")
        campoNome.send_keys(Keys.DELETE)
        campoNome.send_keys('Testinho bonitinho')
        campoCpf = self.driver.find_element_by_id('telefone')
        campoCpf.send_keys(Keys.CONTROL,"a")
        campoCpf.send_keys(Keys.DELETE)
        campoCpf.send_keys('12783092417')
        campoRazao = self.driver.find_element_by_id('razaoSocial')
        campoRazao.send_keys(Keys.CONTROL,"a")
        campoRazao.send_keys(Keys.DELETE)
        campoRazao.send_keys('testeRazao')
        botoes = self.driver.find_elements_by_tag_name("button")
        print(len(botoes))
        self.driver.find_elements_by_tag_name("button")[1].click()