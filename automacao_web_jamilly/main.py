from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os
from dotenv import load_dotenv
from docx import Document

load_dotenv()

driver = webdriver.Chrome()

email = os.environ["EMAIL"]
senha = os.environ["SENHA"]

try:
    documento = Document("dados_adv_programa.docx")
except:
    documento = Document()

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
total_links = len(links)

for i in range(total_links):
    links = driver.find_elements(By.XPATH, '//*[@id="normal"]/form/table/tbody/tr/td[1]/a')
    link = links[i]

    if link.find_element(By.XPATH, './../../td[4]').text == "CERTIFICADO DIGITAL":
        janela_principal = driver.current_window_handle
        nome_adv = link.find_element(By.XPATH, "./../../td[3]").text
        link.click()
        sleep(5)

        #Verifica se cada documento possui OAB no nome
        entrar_aba_documentos = driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div/div[2]/div/ul/li[3]/a')
        entrar_aba_documentos.click()
        sleep(3)
        aba_documentos = driver.find_elements(By.XPATH, '//*[@id="listaDeDocs"]/table/tbody/tr')
        n = 0
        for documento_recebido in aba_documentos:
            if "OAB" in documento_recebido.find_element(By.XPATH, './td[2]').text.upper():
                n += 1

        documentacao = f"documentos OAB: {n}."

        #Volta para a pagina inicial do Dataged
        voltar_inicio = driver.find_element(By.XPATH, '//*[@id="wrapper"]/nav/div[2]/a/img').click()
        sleep(3)
        #Clica no Ficha do Advogado
        ficha_advogado = driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[4]/div/div/div[6]/form/button').click()
        sleep(5)
        janelas_abertas = driver.window_handles
        for janela in janelas_abertas:
            if janela not in janela_principal:
                driver.switch_to.window(janela)
                sleep(5)
                consulta_nome = driver.find_element(By.XPATH, '//*[@id="nome"]')
                consulta_nome.click()
                sleep(1)
                consulta_nome.send_keys(nome_adv)
                sleep(1)
                pesquisar = driver.find_element(By.XPATH, '//*[@id="Install2"]')
                pesquisar.click()
                sleep(1)
                #Pegar os dados de email, cpf, data de nascimento, telefone, subsecao, oab do advogado.
                try:
                    email = driver.find_element(By.XPATH, '//*[@id="frm"]/table[2]/tbody/tr[2]/td[8]').text
                    cpf = driver.find_element(By.XPATH, '//*[@id="frm"]/table[2]/tbody/tr[2]/td[5]').text
                    data_de_nascimento = driver.find_element(By.XPATH, '//*[@id="frm"]/table[2]/tbody/tr[2]/td[12]').text
                    telefone = driver.find_element(By.XPATH, '//*[@id="frm"]/table[2]/tbody/tr[2]/td[11]').text
                    subsecao = driver.find_element(By.XPATH, '//*[@id="frm"]/table[2]/tbody/tr[2]/td[14]').text
                    oab = driver.find_element(By.XPATH, '//*[@id="frm"]/table[2]/tbody/tr[2]/td[2]').text
                    texto = f"{documentacao}\n\nNome: {nome_adv}\nEmail: {email}\nCPF: {cpf}\nData de Nascimento: {data_de_nascimento}\nTelefone: {telefone}\nSubsecao: {subsecao}\nOAB: {oab}\n\n\n"
                    documento.add_paragraph(texto)
                    documento.save("dados_adv_programa.docx")
                except:
                    texto = f"{documentacao}\n\nNome: {nome_adv}\nERRO AO PEGAR email/cpf/ddn/tel/sub/oab\n\nFAZER MANUALMENTE\n\n\n"
                    documento.add_paragraph(texto)
                    documento.save("dados_adv_programa.docx")

                driver.close()
            
        driver.switch_to.window(janela_principal)
        sleep(5)
        caixa_analise2 = driver.find_element(By.XPATH, '//*[@id="side-menu"]/li[1]/ul/li[2]/a')
        caixa_analise2.click()
        sleep(1)


    


															


