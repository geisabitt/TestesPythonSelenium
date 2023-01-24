from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time


class TestLogin:

    def setup_class(self):
        global driver
        driver = webdriver.Firefox()
        driver.maximize_window()

    def test_login(self):
        #Define qual página o browser deve abrir
        driver.get('http://192.168.101.6:3000/')
        
        time.sleep(3)


        field_nome = driver.find_element(By.ID, 'nome')
        field_nome.send_keys('Seleniun')
        

        field_sobrenome = driver.find_element(By.ID, 'sobrenome')
        field_sobrenome.send_keys('Python')
       

        field_cpf = driver.find_element(By.ID, 'cpf')
        field_cpf.send_keys('12312312345')
       

        field_data_nascimento = driver.find_element(By.ID, 'data_nascimento')
        field_data_nascimento.send_keys('1990-07-13')
       

        field_cep = driver.find_element(By.ID, 'cep')
        field_cep.send_keys('12312123')
       

        field_endereco = driver.find_element(By.ID, 'endereco')
        field_endereco.send_keys('Rua')
       

        field_numero = driver.find_element(By.ID, 'numero')
        field_numero.send_keys('N°')
      

        field_complemento = driver.find_element(By.ID, 'complemento')
        field_complemento.send_keys('Casa')
      

        field_cidade = driver.find_element(By.ID, 'cidade')
        field_cidade.send_keys('Nova Iguaçú')
     

        field_estado = driver.find_element(By.ID, 'estado')
        field_estado.send_keys('RJ')

        #Realizamos uma captura de tela

        btn_cadastrar = driver.find_element(By.ID, 'btn-cadastrar')
        btn_cadastrar.click()
        print(btn_cadastrar)

        time.sleep(3)

        btn_editar = driver.find_element(By.CLASS_NAME, 'editar')
        btn_editar.click()

        field_nome = driver.find_element(By.ID, 'nome')
        field_nome.send_keys('Editado')
        

        field_sobrenome = driver.find_element(By.ID, 'sobrenome')
        field_sobrenome.send_keys('PorTeste')
       

        field_cpf = driver.find_element(By.ID, 'cpf')
        field_cpf.send_keys('12312312346')
       

        field_data_nascimento = driver.find_element(By.ID, 'data_nascimento')
        field_data_nascimento.send_keys('1978-10-15')
       

        field_cep = driver.find_element(By.ID, 'cep')
        field_cep.send_keys('34534345')
       

        field_endereco = driver.find_element(By.ID, 'endereco')
        field_endereco.send_keys('TRua')
       

        field_numero = driver.find_element(By.ID, 'numero')
        field_numero.send_keys('TN°')
      

        field_complemento = driver.find_element(By.ID, 'complemento')
        field_complemento.send_keys('TCasa')
      

        field_cidade = driver.find_element(By.ID, 'cidade')
        field_cidade.send_keys('TNova Iguaçú')
     

        field_estado = driver.find_element(By.ID, 'estado')
        field_estado.send_keys('SP')

        #Realizamos uma captura de tela

        btn_att_cadastro = driver.find_element(By.ID, 'btn-att-cadastro')
        btn_att_cadastro.click()
        print(btn_att_cadastro)

        time.sleep(3)

        btn_editar = driver.find_element(By.CLASS_NAME, 'deletar')
        btn_editar.click()
        time.sleep(5)
        


    def teardown_class(self):
        driver.close()