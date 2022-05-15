import time

class CadastroPessoaFisica():
    
    def __init__(self, driver, login, senha, email, nome, cpf, telefone):
        self.driver = driver
        self.inicioCadastro(login, senha, email, nome, cpf, telefone)

    def inicioCadastro (self, login, senha, email, nome, cpf, telefone):
        self.driver.find_element_by_xpath('//span[contains(text(), "Cadastro")]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//div[contains(text(), "Pessoa Física")]').click()
        self.inserirInputs(login, senha, email, nome, cpf)
        self.inserirTelefone(telefone)
        self.inserirDocumento()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element_by_xpath('//span[contains(text(), "Salvar")]').click()

    def inserirInputs(self, login, senha, email, nome, cpf):
        campoLogin = self.driver.find_element_by_id('login')
        campoLogin.clear()
        campoLogin.send_keys(login)
        campoSenha = self.driver.find_element_by_id('password')
        campoSenha.clear()
        campoSenha.send_keys(senha)
        campoEmail = self.driver.find_element_by_id('email')
        campoEmail.clear()
        campoEmail.send_keys(email)
        campoNome = self.driver.find_element_by_id('nome')
        campoNome.clear()
        campoNome.send_keys(nome)
        campoCpf = self.driver.find_element_by_id('cpf')
        campoCpf.clear()
        campoCpf.send_keys(cpf)
    
    def inserirTelefone(self, telefone):
        campoTelefone = self.driver.find_element_by_id('telefone')
        campoTelefone.clear()
        campoTelefone.send_keys('+5581998329317')

    def inserirDocumento(self):
        inputFiles = self.driver.find_elements_by_xpath("//input[@type='file']")
        for x in range(len(inputFiles)):
            inputFiles[x].send_keys("C:\\Users\\moaci\\OneDrive\\Área de Trabalho\\tcc marcos\\TesteUnimpact\\Testes\\imgtest.jpg")





