from selenium import webdriver

class CadastroPessoaFisica():
    
    def __init__(self, driver):
        self.driver = driver
        self.inicioCadastro()

    def inicioCadastro (self):
        self.driver.find_element_by_xpath('//div[contains(text(), "Pessoa Física")]').click()
        self.inserirInputs()
        self.inserirTelefone()
        self.inserirDocumento()

    def inserirInputs(self):
        campoLogin = self.driver.find_element_by_id('login')
        campoLogin.clear()
        campoLogin.send_keys('teste')
        campoSenha = self.driver.find_element_by_id('password')
        campoSenha.clear()
        campoSenha.send_keys('teste2')
        campoEmail = self.driver.find_element_by_id('email')
        campoEmail.clear()
        campoEmail.send_keys('Email')
        campoNome = self.driver.find_element_by_id('nome')
        campoNome.clear()
        campoNome.send_keys('Testinho bonitinho')
        campoCpf = self.driver.find_element_by_id('cpf')
        campoCpf.clear()
        campoCpf.send_keys('12783092417')
    
    def inserirTelefone(self):
        campoTelefone = self.driver.find_element_by_id('telefone')
        campoTelefone.clear()
        campoTelefone.send_keys('+5581998329317')

    def inserirDocumento(self):
        inputFiles = self.driver.find_elements_by_xpath("//input[@type='file']")
        for x in range(len(inputFiles)):
            inputFiles[x].send_keys("C:\\Users\\moaci\\OneDrive\\Área de Trabalho\\tcc marcos\\TesteUnimpact\\Testes\\imgtest.jpg")

    





