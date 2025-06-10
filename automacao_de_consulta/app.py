from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
import openpyxl

numero_oab = "16645"
planilha_dados_consulta = openpyxl.load_workbook('dados da consulta.xlsx')
pagina_processos = planilha_dados_consulta['processos']

# //tag[@atributo='valor']
# //div[@class='propertyView']  XPATH PAI
# //div[@class='col-sm-12'] XPATH FILHO

    #XPATH composto
# //div[@class='propertyView']//div[@class='col-sm-12']

    #XPATH que tem um atributo variavel
# //tbody[contains(@id,'processoPartesPoloAtivoResumidoList:tb')]//span[@class='text-bold']


# 1 - Entrar no site https://pje-consulta-publica.tjmg.jus.br/
driver = webdriver.Chrome()
driver.get("https://pje-consulta-publica.tjmg.jus.br/") 

# 2 - Clicar no campo de oab e digitar o numero do advogado
    # //tag[]
campo_numero_oab = driver.find_element(By.XPATH,"//input[@id='fPP:Decoration:numeroOAB']")
sleep(1)
campo_numero_oab.click() # Clica no lugar selecionado
sleep(1)
campo_numero_oab.send_keys(numero_oab)
sleep(1)

# 3 - Selecionar o estado daquele advogado
selecao_uf = driver.find_element(By.XPATH,"//select[@id='fPP:Decoration:estadoComboOAB']")
sleep(1)
opcoes_uf = Select(selecao_uf)
sleep(1)
opcoes_uf.select_by_visible_text("ES")
sleep(1)

# 4 - Clicar em pesquisar
botao_pesquisar = driver.find_element(By.XPATH,"//input[@id='fPP:searchProcessos']")
sleep(1)
botao_pesquisar.click()
sleep(5)

# 5 - Entrar em cada um dos processos e extrair o numero do advogado, numero do processo e nome dos participantes
links_abrir_processo = driver.find_elements(By.XPATH,"//a[@title='Ver Detalhes']")

# 7 - Repetir ate finalizar todos os processos daquele advogado
for link in links_abrir_processo:
    janela_principal = driver.current_window_handle
    link.click()
    sleep(5)
    janelas_abertas = driver.window_handles
    
    # Ve se a janela aberta e a que foi aberta no momento
    for janela in janelas_abertas:
        if janela not in janela_principal:
            driver.switch_to.window(janela)
            sleep(5)
            numero_processo = driver.find_elements(By.XPATH,"//div[@class='propertyView']//div[@class='col-sm-12']")[0] #o zero e para pegar o primeiro elemento
            participantes = driver.find_elements(By.XPATH,"//tbody[contains(@id,'processoPartesPoloAtivoResumidoList:tb')]//span[@class='text-bold']")
            lista_participantes = [participante.text for participante in participantes]
            # Como guardar um participante (se houver apenas um)
            if len(lista_participantes) == 1:
                #n oab, n processo, nome dos participantes
                pagina_processos.append([numero_oab, numero_processo.text, lista_participantes[0]])
            else:
                # Guardar mais de um participante (se houver mais que um)
                pagina_processos.append([numero_oab, numero_processo.text,','.join(lista_participantes)])

            # 6 - Salvar os dados para uma planilha
            planilha_dados_consulta.save('dados da consulta.xlsx')
            driver.close()
    driver.switch_to.window(janela_principal)


