import time

class CadastroPessoaFisica():
    
    def __init__(self, driver):
        self.driver = driver
        self.inicioCadastro()

    def inicioCadastro (self):
        self.driver.find_element_by_xpath('//span[contains(text(), "Cadastro")]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//div[contains(text(), "Pessoa Física")]').click()
        self.inserirInputs()
        self.inserirTelefone()
        self.inserirDocumento()
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # self.driver.find_element_by_xpath('//div[contains(text(), "Salvar")]').click()

    def inserirInputs(self):
        campoLogin = self.driver.find_element_by_id('login')
        campoLogin.clear()
        campoLogin.send_keys('teste1212')
        campoSenha = self.driver.find_element_by_id('password')
        campoSenha.clear()
        campoSenha.send_keys('teste2')
        campoEmail = self.driver.find_element_by_id('email')
        campoEmail.clear()
        campoEmail.send_keys('Email@a')
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
            inputFiles[x].send_keys("C:\\Us ers\\moaci\\OneDrive\\Área de Trabalho\\tcc marcos\\TesteUnimpact\\Testes\\imgtest.jpg")
        print ("batatadoce")





