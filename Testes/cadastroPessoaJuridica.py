import time
from cadastroPessoaFisica import CadastroPessoaFisica

class CadastroPessoaJuridica():

    def __init__(self, driver, login, senha, email, nome, razao, telefone, instituicao, cnpj, razaoInst, cargo):
        self.driver = driver
        self.inicioCadastro(login, senha, email, nome, razao, telefone, instituicao, cnpj, razaoInst, cargo)

    def inicioCadastro(self, login, senha, email, nome, razao, telefone, instituicao, cnpj, razaoInst, cargo):
        self.driver.find_element_by_xpath('//span[contains(text(), "Cadastro")]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//div[contains(text(), "Pessoa Jurídica")]').click()
        self.inserirInputs(login, senha, email, nome, razao, instituicao, cnpj, razaoInst, cargo)
        CadastroPessoaFisica.inserirTelefone(self, telefone)
        self.inserirImagens()
        self.inserirSelect()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # self.driver.find_element_by_xpath('//div[contains(text(), "Salvar")]').click()

    def inserirSelect(self):
        element = self.driver.find_element_by_name("tipoInstituicao")
        all_options = element.find_elements_by_tag_name("option")
        for option in all_options:
            if option.get_attribute("value") == 'EMPRESA':
                option.click()

    def inserirInputs(self, login, senha, email, nome, razao, instituicao, cnpj, razaoInst, cargo):
        self.driver.find_element_by_id("login").send_keys(login)
        self.driver.find_element_by_id("password").send_keys(senha)
        self.driver.find_element_by_id("email").send_keys(email)
        self.driver.find_element_by_id("nome").send_keys(nome)
        self.driver.find_element_by_id("razaoSocial").send_keys(razao)
        self.driver.find_element_by_id("instituicaoNome").send_keys(instituicao)
        self.driver.find_element_by_id("instituicaoCnpj").send_keys(cnpj)
        self.driver.find_element_by_id("instituicaoRazaoSocial").send_keys(razaoInst)
        self.driver.find_element_by_id("cargo").send_keys(cargo)

    def inserirImagens(self):
        inputImagens = self.driver.find_elements_by_xpath("//input[@type='file']")
        for x in range(len(inputImagens)):
            inputImagens[x].send_keys("C:\\Users\\moaci\\OneDrive\\Área de Trabalho\\tcc marcos\\TesteUnimpact\\Testes\\imgtest.jpg")
        print("batata")