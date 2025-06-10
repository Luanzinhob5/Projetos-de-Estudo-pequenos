from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os

driver = webdriver.Chrome()

email = os.environ["EMAIL"]
senha = os.environ["SENHA"]


#Entra no site
driver.get("https://dataged.eastus.cloudapp.azure.com")
sleep(1)

#Adicionar email ao login
campo_email = driver.find_element(By.XPATH,"//input[@id='email']")
sleep(1)
campo_email.click()
sleep(1)
campo_email.send_keys(email)
sleep(1)

#Adicionar senha ao login
campo_senha = driver.find_element(By.XPATH,"//input[@id='senha']")
sleep(1)
campo_senha.click()
sleep(1)
campo_senha.send_keys(senha)
sleep(20)

#Clicar no botao
botao_logar = driver.find_element(By.XPATH,"//button[@class='buttonGoogle']")
sleep(1)
botao_logar.click()
sleep(1)

#Entrar na caixa de analise
caixa_analise = driver.find_element(By.XPATH,'//*[@id="side-menu"]/li[1]/ul/li[2]/a')
sleep(1)
caixa_analise.click()
sleep(1)

#Verificar documentos com certificado digital
links = driver.find_elements(By.XPATH, '//*[@id="normal"]/form/table/tbody/tr/td[1]/a')

#Verifica cada documento e pega o necessario
for link in links:
    if link.find_element(By.XPATH, './../../td[4]').text == "CERTIFICADO DIGITAL":
        janela_principal = driver.current_window_handle
        link.click()
        sleep(5)
        janelas_abertas = driver.window_handles

        for janela in janelas_abertas:
            if janela not in janela_principal:
                driver.switch_to.window(janela)
                sleep(5)
                aba_documentos = driver.find_elements(By.XPATH, '//*[@id="listaDeDocs"]/table/tbody/tr')
                for documento in aba_documentos:
                    if "OAB" in documento.find_element(By.XPATH, './td[2]').text.upper():
                        print("documentos completos. Fazer contato.")

    


															


