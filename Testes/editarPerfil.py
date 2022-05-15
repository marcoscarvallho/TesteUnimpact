from esperas import Esperas
from selenium.webdriver.common.keys import Keys

class EditarPerfil():
    def __init__(self, driver, email, nome, telefone, razao):
        self.driver = driver
        self.editar(email, nome,telefone,razao)
    
    def editar(self,email, nome, telefone, razao):
        botaoPerfil = Esperas.porXpath(self, '//p[contains(text(), "Meu Perfil")]')
        botaoPerfil.click()
        campoEmail = self.driver.find_element_by_id('email')
        campoEmail.send_keys(Keys.CONTROL,"a")
        campoEmail.send_keys(Keys.DELETE)
        campoEmail.send_keys(email)
        campoNome = self.driver.find_element_by_id('nome')
        campoNome.send_keys(Keys.CONTROL,"a")
        campoNome.send_keys(Keys.DELETE)
        campoNome.send_keys(nome)
        campoCpf = self.driver.find_element_by_id('telefone')
        campoCpf.send_keys(Keys.CONTROL,"a")
        campoCpf.send_keys(Keys.DELETE)
        campoCpf.send_keys(telefone)
        campoRazao = self.driver.find_element_by_id('razaoSocial')
        campoRazao.send_keys(Keys.CONTROL,"a")
        campoRazao.send_keys(Keys.DELETE)
        campoRazao.send_keys(razao)
        botoes = self.driver.find_elements_by_tag_name("button")
        print(len(botoes))
        self.driver.find_elements_by_tag_name("button")[1].click()