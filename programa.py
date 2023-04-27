# SUMÁRIO
# 1) Importações
# 2) Definições necessárias
# 3) Função email Ewelyn
# 4) Função pontuar professores pela planilha 
# 5) Função enviar email sobre o prazo do ICT para os não preenchidos
# 6) Função para estatística com dados da planilha relatório parcial ICT
# 7) Função para coleta Lattes
# 8) Função colocar CPF na planilha longa
# 9) Change character
# Menu
#=============================================================================================
#=============================================================================================
#
# 1) Importações
#
import time
from openpyxl import load_workbook
import pyautogui
from datetime import datetime
from datetime import timedelta
from datetime import date
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import keyboard
from selenium_recaptcha_solver import RecaptchaSolver
#
# 2) Definições necessárias
#
p = subprocess.Popen("whoami && exit", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
user = str(p).split('\\')[2]
options = webdriver.ChromeOptions()
options.add_argument('--log-level=3')
options.add_argument('--disable-gpu')
path_user = '--user-data-dir=C:\\Users\\' + str(user) + '\\AppData\\Local\\Google\\Chrome\\User Data'
options.add_argument(path_user)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--no-sandbox')
options.add_argument("--disable-extensions")
email_utfpr = 'philippeidalgo@alunos.utfpr.edu.br'
senha_utfpr = 'cZG$863?&pdJ'
user_emailpib = 'pibic'
senha_emailpib = 'proppg01'
planilha_base_ICT = 'https://docs.google.com/spreadsheets/d/1Xu_tOTT16isAvKHzF-4iPcKiX0Weg9T-/edit?rtpof=true#gid=450512029'
forms_relatorio_ICT = 'https://docs.google.com/forms/d/1FenyGiVb-i9v_u91q74p_m5oT8YxIp2Ajh0OCo6bBHg/edit#responses'
#
#=============================================================================================
#=============================================================================================
#
# 3) Função email Ewelyn
#
def email_sub_fa():
 ## 3.1) Acessar o email
 driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
 driver.maximize_window()
 action = ActionChains(driver)
 driver.get('https://webmail.utfpr.edu.br/?_task=mail&_mbox=INBOX')
 time.sleep(3)
 try:
  driver.find_element(by='xpath', value='/html/body/div[2]/div[1]/form/table/tbody/tr[1]/td[2]/input').send_keys(user_emailpib)
  time.sleep(1)
  driver.find_element(by='xpath', value='/html/body/div[2]/div[1]/form/table/tbody/tr[2]/td[2]/input').send_keys(senha_emailpib)
  time.sleep(1)
  driver.find_element(by='xpath', value='/html/body/div[2]/div[1]/form/p/button').click()
  time.sleep(5)
 except NoSuchElementException:
  pass
 ## 3.2) Pesquisar os emails de Ewelyn Christine Mendes e salvar seus assuntos & datas & de
 ## Observações: os assuntos normalmente começam com PROTOCOLADO ou PROCESSO APROVADO, mas também podem ter CANCELADO. Os nomes dos alunos substituído e substituto normalmente estão ou separados por "por ", ou por "por_", ou ainda por "x "
 driver.find_element(by='xpath', value='/html/body/div[2]/div[2]/div[2]/form/input').send_keys('ewelyn')
 driver.find_element(by='xpath', value='/html/body/div[2]/div[2]/div[2]/form/input').send_keys(Keys.ENTER)
 time.sleep(10)
 mensagens = str(driver.find_element(by='xpath', value='/html/body/div[2]/div[3]/div[2]/div[1]/div[4]/div[3]/span[1]').text).split('de ')[1]
 pags = int(float(int(mensagens)/50))
 assunto_data = []
 substituido_substituto_estado_data = []
 for i in range(0, pags):
  for j in range(1, 51):
   xpath_assunto = '/html/body/div[2]/div[3]/div[2]/div[1]/div[2]/table[2]/tbody/tr[' + str(j) + ']/td[2]/a/span'
   xpath_de = '/html/body/div[2]/div[3]/div[2]/div[1]/div[2]/table[2]/tbody/tr[' + str(j) + ']/td[4]/span/span'
   xpath_data = '/html/body/div[2]/div[3]/div[2]/div[1]/div[2]/table[2]/tbody/tr[' + str(j) + ']/td[5]'
   xpath_class = '/html/body/div[2]/div[3]/div[2]/div[1]/div[2]/table[2]/tbody/tr[' + str(j) + ']'
   assunto = driver.find_element(by='xpath', value=xpath_assunto).text
   de = driver.find_element(by='xpath', value=xpath_de).text
   data = driver.find_element(by='xpath', value=xpath_data).text
   classs = driver.find_element(by='xpath', value=xpath_class).get_attribute('class')
   a = 0
   palavras_ass = assunto.split(' ')
   palavras_procuradas = ['PROTOCOLADO', 'PROCESSO', 'APROVADO']
   for palavra in palavras_ass:
    try:
     palavras_procuradas.index(palavra)
     a = 1
    except (ValueError, IndexError):
     pass
   if de == 'Ewelyn Christine Mendes' and classs == 'message unread' and a == 1:
    a = [assunto, data]
    assunto_data.append(a)
  driver.find_element(by='xpath', value='/html/body/div[2]/div[3]/div[2]/div[1]/div[4]/div[3]/span[2]/a[3]').click()
  time.sleep(10)
 if len(list(assunto_data)) > 0:
  print('- Encontrei ' + str(len(list(assunto_data))) + ' emails novos de Ewelyn sobre substituição FA')
  for email in assunto_data:
   print(email[1] + ': ' + email[0])
 else:
  print('- Na pesquisa programada, não foram encontrados novos emails de Ewelyn sobre substituição FA')
 ## 3.3) Grande if para preencher a planilha de substituição
 # driver.get('https://docs.google.com/spreadsheets/d/1YV6SRmD30jD7vh9wT10w1ep4bfamjxnfg19VxniKslU/edit#gid=0')
 # time.sleep(3)
 # try:
 #  driver.find_element(by='xpath', value='/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input').send_keys(email_utfpr)
 #  time.sleep(1)
 #  driver.find_element(by='xpath', value='/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
 #  time.sleep(4)
 #  driver.find_element(by='xpath', value='/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div#[1]/input').send_keys(senha_utfpr)
 #  time.sleep(1)
 #  driver.find_element(by='xpath', value='/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
 #  time.sleep(5)
 # except NoSuchElementException:
 #  pass
 # for parte in assunto_data:
 #  data = parte[1]
 #  palavras_assunto = parte[0].split(' ')
 #  for i in range(0, len(list(palavras_assunto))):
 #   try:
 #    if palavras_assunto[i] == 'PROCESSO' and palavras_assunto[i+1] == 'APROVADO':
 #     estado = 'Aprovado'
 #     break
 #   except IndexError:
 #    continue
 #   if palavras_assunto[i] == 'PROTOCOLADO':
 #    estado = 'Protocolado'
 #    break
 #   else:
 #    estado = 'Verificar'
 #  for j in range(0, len(list(palavras_assunto))):
 #   substituido = parte[0]
 #   substituto = 0
 #   ### VER O ESTADO DOS ASSUNTOS para poder oegar os subtituidos e substituto
 #  b = [substituido, substituto, estado, data]
 #  substituido_substituto_estado_data.append(b)
 # print(substituido_substituto_estado_data)
 # f = input()
 # for part in substituito_substituto_estado_data:
 #  a = 0
 #  #verficair se o aluno já está na lista
 #  # se não, adiciona
 ## 3.4) Verificar se os nomes dos substituídos e substitutos estão atualizados na planilha ICT, bem como suas informações & estados
 # driver.get('https://docs.google.com/spreadsheets/d/1Xu_tOTT16isAvKHzF-4iPcKiX0Weg9T-/edit#gid=450512029')
 # time.sleep(3)
 # for part in substituidos_substitutos_estado_data:
 #  print('a')
 #  ### verifiar todas as lnhas da palnilha, procurando substituido e substituto,. para atuzzalir a iobservação e sua cor
#
# 4) Função pontuar professores pela planilha
#
def prof_planilha():
 driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
 driver.maximize_window()
 action = ActionChains(driver)
 driver.get('https://docs.google.com/spreadsheets/d/1rerrMSRcPT16r84R1zji1f_SO1aqGpb2c2Esr9zzUR0/edit#gid=0')
 time.sleep(5)
 last_name = ''
 last_comis = ''
 last_pont = ''
 i = 1
 while True:
  cellname = 'A' + str(i)
  cellcomis = 'B' + str(i)
  cellpont = 'C' + str(i)
  driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').clear()
  driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(cellname)
  driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(Keys.ENTER)
  name = str(driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[3]/div[3]/div/div/div').text).replace('=PRI.MAIÚSCULA("', '').replace('")', '')
  driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').clear()
  driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(cellcomis)
  driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(Keys.ENTER)
  comis = driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[3]/div[3]/div/div/div').text
  driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').clear()
  driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(cellpont)
  driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(Keys.ENTER)
  pont = driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[3]/div[3]/div/div/div').text
  if name == last_name and last_comis == comis:
   action.key_down(Keys.CONTROL).key_down(Keys.ALT).send_keys('-').key_up(Keys.ALT).key_up(Keys.CONTROL).perform()
   for j in range(1, 3):
    action.send_keys(Keys.DOWN).perform()
   action.send_keys(Keys.ENTER).perform()
   try:
    int(name)
    break
   except:
    print('- ' + name + ' está repetido e excluído')
  elif name == last_name and last_comis != comis:
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').clear()
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(cellcomis)
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(Keys.ENTER)
   for k in range(0, len(comis)):
    driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[3]/div[3]/div/div/div').send_keys(Keys.BACKSPACE)
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[3]/div[3]/div/div/div').send_keys(comis + ' e ' + last_comis)
   action.send_keys(Keys.ENTER).perform()
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').clear()
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(cellpont)
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(Keys.ENTER)
   for k in range(0, len(pont)):
    driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[3]/div[3]/div/div/div').send_keys(Keys.BACKSPACE)
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[3]/div[3]/div/div/div').send_keys(str(int(last_pont) + int(pont)))
   action.send_keys(Keys.ENTER).perform()
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').clear()
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys('A' + str(i - 1))
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(Keys.ENTER)
   action.key_down(Keys.CONTROL).key_down(Keys.ALT).send_keys('-').key_up(Keys.ALT).key_up(Keys.CONTROL).perform()
   for j in range(1, 3):
    action.send_keys(Keys.DOWN).perform()
   action.send_keys(Keys.ENTER).perform()
   last_name = name
   last_comis = comis + ' e ' + last_comis
   last_pont = str(int(last_pont) + int(pont))
   print('- ' + name + ' foi somado')
  else:
   last_name = name
   last_comis = comis
   last_pont = pont
   i = i + 1
 f = input()
#
# 5) Função enviar email sobre o prazo do ICT para os não preenchidos
#
def email_ict():
 driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
 driver.maximize_window()
 action = ActionChains(driver)
 # Pegar emails sem repetir na planilha de 27 de março
 emails_totais = []
 driver.get('https://docs.google.com/spreadsheets/d/1Xu_tOTT16isAvKHzF-4iPcKiX0Weg9T-/edit#gid=450512029')
 time.sleep(10)
 for i in range(2, 1294):
  cell = 'H' + str(i)
  driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').clear()
  driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(cell)
  driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(Keys.ENTER)
  email = driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[3]/div[3]/div/div/div').text
  if email != '':
   if len(list(emails_totais)) == 0:
    emails_totais.append(email)
   else:
    try:
     emails_totais.index(email)
    except ValueError:
     emails_totais.append(email)
 print('- Total de emails na planilha: ' + str(len(list(emails_totais))))
 # No forms, rodar todos os emails e concluir quais ainda não enviaram
 emails_dos_completos = []
 driver.get('https://docs.google.com/forms/d/1FenyGiVb-i9v_u91q74p_m5oT8YxIp2Ajh0OCo6bBHg/edit#response=ACYDBNgBftlzjD0Y_lTpniPTwGWHhZnY4Cl1WfobplNtNbxlHTUhW83EprHMi3BAnT0ycf8')
 time.sleep(5)
 for j in range(1, 740):
  try:
   driver.find_element(by='xpath', value='/html/body/div[3]/div[2]/div[2]/div/div[4]/div/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div/div[1]/input').clear()
   driver.find_element(by='xpath', value='/html/body/div[3]/div[2]/div[2]/div/div[4]/div/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div/div[1]/input').send_keys(str(j))
   driver.find_element(by='xpath', value='/html/body/div[3]/div[2]/div[2]/div/div[4]/div/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div/div[1]/input').send_keys(Keys.ENTER)
   time.sleep(2)
   xpath_email = '/html/body/div[3]/div[2]/div[2]/div/div[4]/div/div[1]/div[1]/div[1]/div/div[1]/div[1]/div[' + str(j) + ']/span'
   email = str(driver.find_element(by='xpath', value=xpath_email).text).split(' (')[0]
   if email != '':
    if len(list(emails_dos_completos)) == 0:
     emails_dos_completos.append(email)
    else:
     try:
      emails_dos_completos.index(email)
     except ValueError:
      emails_dos_completos.append(email)
  except NoSuchElementException:
   pass
 print('- Total de emails no formulário: ' + str(len(list(emails_dos_completos))))
 print('- O número esperado de emails a serem enviados é: ' + str(len(list(emails_totais)) - len(list(emails_dos_completos))))
 # Escrever um email sobre
 email_a_serem_enviados = []
 for email in emails_totais:
  try:
   emails_dos_completos.index(email)
  except ValueError:
   email_a_serem_enviados.append(email)
 print('- Total de emails a serem enviados: ' + str(len(list(email_a_serem_enviados))))
 driver.get('https://webmail.utfpr.edu.br/')
 time.sleep(3)
 driver.find_element(by='xpath', value='/html/body/div[2]/div[1]/form/table/tbody/tr[1]/td[2]/input').send_keys(user_emailpib)
 driver.find_element(by='xpath', value='/html/body/div[2]/div[1]/form/table/tbody/tr[2]/td[2]/input').send_keys(senha_emailpib)
 driver.find_element(by='xpath', value='/html/body/div[2]/div[1]/form/p/button').click()
 time.sleep(5)
 driver.find_element(by='xpath', value='/html/body/div[2]/div[1]/a[2]').click()
 time.sleep(5)
 for k in range(0, int(len(list(email_a_serem_enviados))/50) + 1):
  for l in range(0, 50):
   ind = k*50 + l
   try:
    if l != 0:
     keyboard.write(', ' + email_a_serem_enviados[ind])
    else:
     keyboard.write(email_a_serem_enviados[ind])
   except IndexError:
    pass
  action.send_keys(Keys.TAB)
  keyboard.write('Aviso DEICT: Prazo para responder o Relatório Parcial da Iniciação Científica e Tecnológica')
  action.send_keys(Keys.TAB)
  keyboard.write('Prezados Orientadores,')
  action.send_keys(Keys.ENTER)
  keyboard.write('O prazo para responder o Relatório Parcial referente a atuação dos estundantes do Programa de Iniciação Científica e Tecnológica encerra amanhã, dia 14 de abril/2023.')
  action.send_keys(Keys.ENTER)
  keyboard.write('Lembramos, que a sua resposta para esse relatório tem o intuito de acompanhar o (a) estudante, bem como observar o cumprimento do plano de trabalho. A UTFPR atende a RN 17/2006 - CNPq.')
  action.send_keys(Keys.ENTER)
  keyboard.write('Solicitamos que o formulário do Relatório Parcial seja respondido para cada estudante orientado.')
  action.send_keys(Keys.ENTER)
  keyboard.write('O formulário do relatório parcial está disponível no link abaixo:')
  action.send_keys(Keys.ENTER)
  keyboard.write('https://docs.google.com/forms/d/e/1FAIpQLSdzNk1RZTsIF-e5ehJ2uMrQmx7FQqIdb1MpYBbsfwQCdKWpiQ/viewform?usp=sharing')
  action.send_keys(Keys.ENTER)
  keyboard.write('DATA LIMITE: 14 DE ABRIL')
  action.send_keys(Keys.ENTER)
  keyboard.write('Ficamos à disposição')
  action.send_keys(Keys.ENTER)
  input('Próximo?')
#
# 6) Função para estatística com dados da planilha relatório parcial ICT
#
def estatistica_ict():
 # 2) Pega os dados da planilha
 driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
 driver.get('https://docs.google.com/spreadsheets/d/1krV_GOdJmOhnsgNqGllEBS78WOttP6ME/edit#gid=1167363091')
 time.sleep(3)
 dados = []
 for i in range(2, 842):
  data = []
  cell_nome_professor = 'A' + str(i)
  cell_nome_estudante = 'C' + str(i)
  cell_curso = 'D' + str(i)
  cell_area = 'E' + str(i)
  cell_fomento = 'H' + str(i)
  cell_concluido = 'I' + str(i)
  cell_expectativa = 'J' + str(i)
  cell_carga_horaria = 'K' + str(i)
  cell_regularidade = 'L' + str(i)
  cell_potencial_pesquisa = 'M' + str(i)
  cell_desempenho_estudante = 'O' + str(i)
  cell_perfil_pg = 'Q' + str(i)
  temas = [cell_nome_professor, cell_nome_estudante, cell_curso, cell_area, cell_fomento, cell_concluido, cell_expectativa, cell_carga_horaria, cell_regularidade, cell_potencial_pesquisa, cell_desempenho_estudante, cell_perfil_pg]
  for tema in temas:
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').clear()
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(tema)
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(Keys.ENTER)
   resposta = driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[3]/div[3]/div/div/div').text
   data.append(resposta)
  dados.append(data)
 #
 # 3) Estatística
 #
 #
 # média da porcentagem do trabalho feito por alunos prováveis de pós graduação
 #
 dados_selec = []
 for parte in dados:
  if parte[11] == 'Sim':
   dados_selec.append(parte[5])
 try:
  media = 0
  for porc in dados_selec:
   media = media + int(porc)
  media = round((media/len(list(dados_selec)))*10, 2)
  print('\n- A média da porcentagem do trabalho feita por alunos prováveis de pós graduação: ' + str(media) + '%')
 except ZeroDivisionError:
  print('\n- Não foi possível evaluar a média da porcentagem do trabalho feito por alunos prováveis de pós graduação')
 #
 # média da porcentagem do trabalho feita por alunos de cada fomento
 #
 fomentos = ['CNPq', 'UTFPR', 'Fundação Araucária']
 for fomento in fomentos:
  dados_selec = []
  for parte in dados:
   if parte[4] == fomento:
    dados_selec.append(parte[5])
  try:
   media = 0
   for porc in dados_selec:
    media = media + int(porc)
   media = round((media/len(list(dados_selec)))*10, 2)
   print('\n- A média da porcentagem do trabalho feita por alunos ' + fomento + ': ' + str(media) + '%')
  except ZeroDivisionError:
   print('\n- Não foi possível evaluar a média da porcentagem do trabalho feito por alunos ' + fomento)
 #
 # média da expectativa de porcentagem de conclusão do trabalho dos alunos de cada fomento
 #
 fomentos = ['CNPq', 'UTFPR', 'Fundação Araucária']
 for fomento in fomentos:
  dados_selec = []
  for parte in dados:
   if parte[4] == fomento:
    dados_selec.append(parte[6])
  try:
   media = 0
   for porc in dados_selec:
    media = media + int(porc)
   media = round((media/len(list(dados_selec)))*10, 2)
   print('\n- A média da expectativa de porcentagem do trabalho entregue por alunos ' + fomento + ': ' + str(media) + '%')
  except ZeroDivisionError:
   print('\n- Não foi possível evaluar a média da expectativa de porcentagem do trabalho entregue por alunos ' + fomento)
 #
 # Curso de graduação com as melhores porcentagens de trabalho concluído até agora
 #
 # cursos_apar_soma = []
 # for parte in dados:
 #  if len(list(cursos_apar_soma)) == 0:
 #   cursos_apar_soma.append([parte[2], 1, int(parte[5])])
 #  else:
 #   tent = 0
 #   for part in cursos_apar_soma:
 #    if part[0] == parte[2]:
 #     part[1] = part[1] + 1
 #     part[2] = part[2] + int(parte[5])
 #   else:
 #    tent = tent + 1
 #   if tent == len(list(cursos_apar_soma)):
 #    cursos_apar_soma.append([parte[2], 1, int(parte[5])])
 # for art in cursos_apar_soma:
 #  media = media + art[2]
 #  media = round((media/art[1])*10, 4)
 #  art = [media, art[0], int(art[1])]
 # cursos_apar_soma.sort(reverse=True)
 # print('- Os cursos com maiores porcentagens de trabalho concluído são:')
 # for parte in cursos_apar_soma:
 #  print('-- ' + str(parte[1]) + ': ' + str(parte[0]) + '% (' + str(parte[2]) + ' aparições)')
 #
 # cursos mais financiados por cada fomento
 #
 fomentos = ['CNPq', 'UTFPR', 'Fundação Araucária']
 for fomento in fomentos:
  cursos_apar = []
  for parte in dados:
   if parte[4] == fomento:
    if len(list(cursos_apar)) == 0:
     cursos_apar.append([1, parte[2]])
    else:
     tent = 0
     for part in cursos_apar:
      if part[1] == parte[2]:
       part[0] = part[0] + 1
      else:
       tent = tent + 1
     if tent == len(list(cursos_apar)):
      cursos_apar.append([1, parte[2]])
  cursos_apar.sort(reverse=True)
  total = 0
  for cur in cursos_apar:
   total = total + cur[0]
  print('\n- Os cursos com os maiores investimentos pelo ' + fomento  + ' são:')
  for parte in cursos_apar:
   if cursos_apar.index(parte) <= 5:
    media = round((parte[0]/total)*100, 2)
    print('- ' + parte[1] + ': ' + str(media) + '% (' + str(parte[0]) + ' aparições)')
 #
 # áreas de pesquisa mais financiadas por cada fomento
 #
 fomentos = ['CNPq', 'UTFPR', 'Fundação Araucária']
 for fomento in fomentos:
  cursos_apar = []
  for parte in dados:
   if parte[4] == fomento:
    if len(list(cursos_apar)) == 0:
     cursos_apar.append([1, parte[3]])
    else:
     tent = 0
     for part in cursos_apar:
      if part[1] == parte[3]:
       part[0] = part[0] + 1
      else:
       tent = tent + 1
     if tent == len(list(cursos_apar)):
      cursos_apar.append([1, parte[3]])
  cursos_apar.sort(reverse=True)
  total = 0
  for cur in cursos_apar:
   total = total + cur[0]
  print('\n- As áreas de pesquisas mais financiadas pelo ' + fomento  + ' são:')
  for parte in cursos_apar:
   if cursos_apar.index(parte) <= 5:
    media = round((parte[0]/total)*100, 2)
    print('- ' + parte[1] + ': ' + str(media) + '% (' + str(parte[0]) + ' aparições)')
 #
 # carga horária média
 #
 dados_selec = []
 for parte in dados:
  if len(list(dados_selec)) == 0:
   dados_selec.append([1, parte[7]])
  else:
   tent = 0
   for part in dados_selec:
    if part[1] == parte[7]:
     part[0] = part[0] + 1
    else:
     tent = tent + 1
   if tent == len(list(dados_selec)):
    dados_selec.append([1, parte[7]])
 dados_selec.sort(reverse=True)
 total = 0
 for par in dados_selec:
  total = total + par[0]
 print('\n- As cargas horárias mais vistas são:')
 for par in dados_selec:
  media = round((par[0]/total)*100, 2)
  print('- ' + par[1] + ': ' + str(media) + '% (' + str(par[0]) + ' aparições)')
 #
 # carga horária por cada fomento
 #
 fomentos = ['CNPq', 'UTFPR', 'Fundação Araucária']
 for fomento in fomentos:
  cursos_apar = []
  for parte in dados:
   if parte[4] == fomento:
    if len(list(cursos_apar)) == 0:
     cursos_apar.append([1, parte[7]])
    else:
     tent = 0
     for part in cursos_apar:
      if part[1] == parte[7]:
       part[0] = part[0] + 1
      else:
       tent = tent + 1
     if tent == len(list(cursos_apar)):
      cursos_apar.append([1, parte[7]])
  cursos_apar.sort(reverse=True)
  total = 0
  for cur in cursos_apar:
   total = total + cur[0]
  print('\n- As cargas horárias mais vistas em ' + fomento  + ' são:')
  for parte in cursos_apar:
   media = round((parte[0]/total)*100, 2)
   print('- ' + parte[1] + ': ' + str(media) + '% (' + str(parte[0]) + ' aparições)')
 #
 # carga horária por cada curso
 #
 #
 # carga horária por cada área
 #
 #
 # potencial da pesquisa por fomento
 #
 fomentos = ['CNPq', 'UTFPR', 'Fundação Araucária']
 for fomento in fomentos:
  cursos_apar = []
  for parte in dados:
   if parte[4] == fomento:
    if len(list(cursos_apar)) == 0:
     cursos_apar.append([1, parte[9]])
    else:
     tent = 0
     for part in cursos_apar:
      if part[1] == parte[9]:
       part[0] = part[0] + 1
      else:
       tent = tent + 1
     if tent == len(list(cursos_apar)):
      cursos_apar.append([1, parte[9]])
  cursos_apar.sort(reverse=True)
  total = 0
  for cur in cursos_apar:
   total = total + cur[0]
  print('\n- Os potenciais de pesquisa mais vistos em ' + fomento  + ' são:')
  for parte in cursos_apar:
   media = round((parte[0]/total)*100, 2)
   print('- ' + parte[1] + ': ' + str(media) + '% (' + str(parte[0]) + ' aparições)')
 #
 # potencial da pesquisa por curso
 #
 #
 # potencial da pesquisa por área
 #
 #
 # desempenho do estudante por curso
 #
 #
 # desempenho do estudante por fomento
 #
 fomentos = ['CNPq', 'UTFPR', 'Fundação Araucária']
 for fomento in fomentos:
  cursos_apar = []
  for parte in dados:
   if parte[4] == fomento:
    if len(list(cursos_apar)) == 0:
     cursos_apar.append([1, parte[10]])
    else:
     tent = 0
     for part in cursos_apar:
      if part[1] == parte[10]:
       part[0] = part[0] + 1
      else:
       tent = tent + 1
     if tent == len(list(cursos_apar)):
      cursos_apar.append([1, parte[10]])
  cursos_apar.sort(reverse=True)
  total = 0
  for cur in cursos_apar:
   total = total + cur[0]
  print('\n- Os desempenhos dos alunos mais vistos em ' + fomento  + ' são:')
  for parte in cursos_apar:
   media = round((parte[0]/total)*100, 2)
   print('- ' + parte[1] + ': ' + str(media) + '% (' + str(parte[0]) + ' aparições)')
 #
 # desempenho do estudante por área
 #
 #
 # perfil do estudante por fomento
 #
 fomentos = ['CNPq', 'UTFPR', 'Fundação Araucária']
 for fomento in fomentos:
  cursos_apar = []
  for parte in dados:
   if parte[4] == fomento:
    if len(list(cursos_apar)) == 0:
     cursos_apar.append([1, parte[11]])
    else:
     tent = 0
     for part in cursos_apar:
      if part[1] == parte[11]:
       part[0] = part[0] + 1
      else:
       tent = tent + 1
     if tent == len(list(cursos_apar)):
      cursos_apar.append([1, parte[11]])
  cursos_apar.sort(reverse=True)
  total = 0
  for cur in cursos_apar:
   total = total + cur[0]
  print('\n- Os perfis de estudante PG mais vistos em ' + fomento  + ' são:')
  for parte in cursos_apar:
   media = round((parte[0]/total)*100, 2)
   print('- ' + parte[1] + ': ' + str(media) + '% (' + str(parte[0]) + ' aparições)')
 #
 # perfil do estudante por curso
 #
 #
 # perfil do estudante por área
 #
 #
 ## [nome_professor, nome_estudante, curso, area, fomento, concluido, expectativa, carga_horaria, regularidade, potencial_pesquisa, desempenho_estudante, perfil_pg]
# 
# 7) Função coletar dados de publicação no lattes
#
def coleta_lattes():
  driver1 = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
  ids_pesquisadores = ['K4755167Z6']
  nome_publicacoes = []
  for id in ids_pesquisadores:
    driver1.get('http://buscatextual.cnpq.br/buscatextual/visualizacv.do?metodo=apresentar&id=' + id)
    nome_pesq = str(driver1.getTitle()).split(' (')[1].replace(')','')
    time.sleep(30)
    # 7.1) Verifica e realiza o reCAPTCHA
    #try:
    # recaptcha_driver = RecaptchaSolver(driver=driver1)
    # recaptcha_iframe = driver1.find_element(by='xpath', value='//iframe[@title="reCAPTCHA"]')
    # try:
    #  recaptcha_driver.click_recaptcha_v2(iframe=recaptcha_iframe)
    # except TimeoutException:
    #  pass
    # time.sleep(3)
    # driver1.find_element(by='xpath', value='/html/body/form/div/div/div/div/div/div/div/div/div[4]/div/input').click()
    # time.sleep(5)
    #except NoSuchElementException:
    # pass
    # 7.2) Coleta os dados
    i = 1
    found_prod = 0
    while True:
      try:
       element = driver1.find_element(by='xpath', value='/html/body/div[1]/div[3]/div/div/div/div[' + str(i) + ']/a')
       driver1.execute_script("arguments[0].scrollIntoView(true);", element)
       a_name = element.get_attribute("name")
       if a_name == "ProducoesCientificas":
        found_prod = 1
        j = 1
        while True:
          div_id = driver1.find_element(by='xpath', value='/html/body/div[1]/div[3]/div/div/div/div[' + str(i) +']/div/div[' + str(j) + ']').get_attribute("id")
          if div_id == "artigos-completos":
            k = 1
            publicacoes = []
            while True:
             try:
              eleme = driver1.find_element(by='xpath', value='/html/body/div[1]/div[3]/div/div/div/div[' + str(i) +']/div/div[' + str(j) + ']/div[' + str(k) + ']')
              driver1.execute_script("arguments[0].scrollIntoView(true);", eleme)
              eleme_class = eleme.get_attribute('class')
              if eleme_class == "artigo-completo":
                publicacao = []
                l = 1
                while True:
                 try:
                  div_span = driver1.find_element(by='xpath', value='/html/body/div[1]/div[3]/div/div/div/div[' + str(i) +']/div/div[' + str(j) + ']/div[' + str(k) + ']/div[2]/div/span[' + str(l) + ']')
                  div_span_tipo = div_span.get_attribute('data-tipo-ordenacao')
                  if div_span_tipo == 'ano':
                   publicacao.append(['ano', str(div_span.get_attribute('textContent'))])
                   break
                 except NoSuchElementException:
                  pass
                 l = l + 1
                div_cvuri = driver1.find_element(by='xpath', value='/html/body/div[1]/div[3]/div/div/div/div[' + str(i) +']/div/div[' + str(j) + ']/div[' + str(k) + ']/div[2]/div/div').get_attribute('cvuri')
                dados = str(div_cvuri).split('&')
                for dado in dados:
                 tipo = dado.split('=')
                 try:
                  publicacao.append([tipo[0], tipo[1]])
                 except IndexError:
                  pass
                publicacoes.append(publicacao)
             except NoSuchElementException:
              break
             nome_publicacoes.append([nome_pesq, publicacoes])
             k = k + 1
            break
          j = j + 1
      except NoSuchElementException:
       pass
      if found_prod == 1:
       break
      else:
       i = i + 1
    print(nome_publicacoes)
#
# 8) Função colocar CPF na planilha longa
#
def cpf():
  nomes = []
  nomes_cpf = []
  driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
  action = ActionChains(driver)
  driver.get('https://docs.google.com/spreadsheets/d/1xLFXp4hVY8DsD5iQ2Tfdpn2AAKvoYy9Y/edit#gid=1966649337')
  time.sleep(8)
  for i in range(5, 53380):
    cellname = 'B' + str(i)
    driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').clear()
    driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(cellname)
    driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(Keys.ENTER)
    name = driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[3]/div[3]/div/div/div').text
    if len(list(nomes)) == 0:
      nomes.append(name)
    else:
      try:
        nomes.index(name)
      except ValueError:
        nomes.append(name)
  driver.get('https://docs.google.com/spreadsheets/d/1HHRplGnAA-yEmsFbynb_QDufS6EfxjFb/edit#gid=95382403')
  time.sleep(8)
  for name in nomes:
    action.key_down(Keys.CONTROL).send_keys("f").key_up(Keys.CONTROL).perform()
    time.sleep(1)
    driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[2]/div/div/div[1]/div[1]/div/div[2]/table/tbody/tr/td[1]/input').send_keys(name)
    time.sleep(2)
    index_primeiro = int(str(driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[2]/div/div/div[1]/div[1]/div/div[2]/table/tbody/tr/td[2]/span').text).split(' ')[0])
    if index_primeiro != 0:
      action.send_keys(Keys.ESCAPE).perform()
      time.sleep(1)
      cell_found = driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').get_attribute("value")
      driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').clear()
      driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(cell_found.replace("C", "H"))
      driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(Keys.ENTER)
      cpf = driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[3]/div[3]/div/div/div').text
      dado = [name, cpf]
      if len(list(nomes_cpf)) == 0:
        nomes_cpf.append(dado)
      else:
        try:
          nomes_cpf.index(dado)
        except ValueError:
          nomes_cpf.append(dado)
    else:
      print('ERRO: nome não encontrado na pontuação; ' + name)
  driver.get('https://docs.google.com/spreadsheets/d/1xLFXp4hVY8DsD5iQ2Tfdpn2AAKvoYy9Y/edit#gid=1966649337')
  for k in range(5, 53380):
    cell_name = "B" + str(k)
    cell_cpf = "C" + str(k)
    driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').clear()
    driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(cell_name)
    driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(Keys.ENTER)
    name = driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[3]/div[3]/div/div/div').text
    for par in nomes_cpf:
      if par[0] == name:
        driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').clear()
        driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(cell_cpf)
        driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(Keys.ENTER)
        driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[3]/div[3]/div/div/div').send_keys(par[1])
        action.send_keys(Keys.ENTER).perform()
#
# 9) Change character
#
def change_char():
 driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
 action = ActionChains(driver)
 driver.get('https://docs.google.com/spreadsheets/d/1xLFXp4hVY8DsD5iQ2Tfdpn2AAKvoYy9Y/edit#gid=1966649337')
 time.sleep(3)
 dados = []
 colunas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
 for i in range(5, 53380):
  for coluna in colunas:
   cell = coluna + str(i)
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').clear()
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(cell)
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(Keys.ENTER)
   texto = driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[3]/div[3]/div/div/div').text
   pyautogui.moveTo(x=1752, y=198)
   for k in range(0, 3):
    pyautogui.click()
   keyboard.press('backspace')
   new_texto = texto.replace('-', ' ').replace('?', ' ').replace('&', ' ').replace('*', ' ').replace('@', ' ').replace('#', ' ').replace('$', ' ').replace('£', ' ').replace('¢', ' ').replace('!', ' ').replace('/', ' ').replace("\\", ' ').replace('§', ' ').replace('=', ' ').replace('+', ' ').replace(';', ' ').replace('ã', 'a').replace('Ã', 'A').replace('õ', 'o').replace('Õ', 'O').replace('ô', 'o').replace('Ô', 'O').replace('â', 'a').replace('Â', 'A').replace('é', 'e').replace('É', 'E').replace('á', 'a').replace('Á', 'A').replace('ó', 'o').replace('Ó', 'O').replace('à', 'a').replace('À', 'A').replace('í', 'i').replace('Í', 'I').replace('ú', 'u').replace('Ú', 'U').replace('°', ' ').replace('º', ' ').replace('®', ' ').replace('ê', 'e').replace('ç', 'c').replace('Ê', 'E').replace('Ç', 'C')
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[3]/div[3]/div/div/div').send_keys(new_texto)
   action.send_keys(Keys.ENTER).perform()
#
# Menu
#
def menu():
 txt = ['Olá :)\n', '1) Email Sub FA', '2) Prof planilha', '3) Email ICT', '4) Estatística relatório parcial ICT', '5) Coleta Lattes', '6) Colocar CPF', '7) Change Char']
 for text in txt:
  print(text)
 while True:
  escolha = input('- Digite a opção: ')
  if escolha == '1':
   print('- Executando: ' + txt[int(escolha)].split(') ')[1])
   email_sub_fa()
   break
  elif escolha == '2':
   print('- Executando: ' + txt[int(escolha)].split(') ')[1])
   prof_planilha()
   break
  elif escolha == '3':
   print('- Executando: ' + txt[int(escolha)].split(') ')[1])
   email_ict()
   break
  elif escolha == '4':
   print('- Executando: ' + txt[int(escolha)].split(') ')[1])
   estatistica_ict()
   break
  elif escolha == '5':
   print('- Executando: ' + txt[int(escolha)].split(') ')[1])
   coleta_lattes()
   break
  elif escolha == '6':
   print('- Executando: ' + txt[int(escolha)].split(') ')[1])
   cpf()
   break
  elif escolha == '7':
   print('- Executando: ' + txt[int(escolha)].split(') ')[1])
   change_char()
   break
  else:
   print('Tente novamente! Número inválido')
 menu()
menu()
f=input('fim')
