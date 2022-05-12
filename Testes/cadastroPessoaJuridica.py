from selenium import webdriver
import time
import sys

class CadastroPessoaJuridica():

    def __init__(self, driver):
        self.driver = driver
        self.inicioCadastro()

    def inicioCadastro(self):
        self.driver.find_element_by_xpath('//span[contains(text(), "Cadastro")]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//div[contains(text(), "Pessoa Jurídica")]').click()
        self.inserirInputs()
        self.inserirImagens()
        self.inserirSelect()
        # self.driver.find_element_by_xpath('//div[contains(text(), "Salvar")]').click()

    def inserirSelect(self):
        element = self.driver.find_element_by_name("tipoInstituicao")
        all_options = element.find_elements_by_tag_name("option")
        for option in all_options:
            if option.get_attribute("value") == 'EMPRESA':
                option.click()

    def inserirInputs(self):
        self.driver.find_element_by_id("login").send_keys("testeLogin")
        self.driver.find_element_by_id("password").send_keys("testeSenha")
        self.driver.find_element_by_id("email").send_keys("testeEmail")
        self.driver.find_element_by_id("nome").send_keys("testeNome")
        self.driver.find_element_by_id("razaoSocial").send_keys("testeRazao")
        self.driver.find_element_by_id("telefone").send_keys("5540028922")
        self.driver.find_element_by_id("instituicaoNome").send_keys("testeInstituicao")
        self.driver.find_element_by_id("instituicaoCnpj").send_keys("11111111111111")
        self.driver.find_element_by_id("instituicaoRazaoSocial").send_keys("testeRazaoInstituto")
        self.driver.find_element_by_id("cargo").send_keys("testeCargo")

    def inserirImagens(self):
        # inputImagens = self.driver.find_elements_by_xpath("//input[@type='file']")
        # for x in range(len(inputImagens)):
        #     inputImagens[x].send_keys("C:\\Users\\moaci\\OneDrive\\Área de Trabalho\\tcc marcos\\TesteUnimpact\\Testes\\imgtest.jpg")
        print("batata")