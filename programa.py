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
# 10) Programa catai
# 11) exclui linha de planilha
# 12) Planilha Ju
# 13) Pegar txt
# 14) Exclui repetidos
# 15) Ver dados e compara
# 16) Dados catai
# Menu
#=============================================================================================
#=============================================================================================
#
# 1) Importações
#
import time
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
from selenium.webdriver.common.action_chains import ActionChains
import keyboard
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
 # Pegar emails sem repetir na planilha
 emails_totais = []
 driver.get('https://docs.google.com/spreadsheets/d/1HNVyWNxFyjA-5qWQ4Zc6ChhmqBiS93Ke/edit#gid=1957127511')
 time.sleep(10)
 for i in range(2, 829):
  cell = 'C' + str(i)
  driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[7]/div[1]/input').clear()
  driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[7]/div[1]/input').send_keys(cell)
  driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[7]/div[1]/input').send_keys(Keys.ENTER)
  nome = driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[7]/div[3]/div[3]/div/div/div').text
  color = driver.find_element(by='xpath', value='/html/body/div[2]/div[4]/div[2]/div[1]/div[2]/div[27]/div/div/div/div').get_attribute('style').split(';')[0].split(': ')[1]
  time.sleep(1)
  if nome != '' and nome != ' ' and color != 'rgb(255, 0, 0)':
    emails_totais.append(nome.upper())
 #fil = open("C:/Users/DIREPQ/Desktop/cnpq.txt", 'r')
 #conj = fil.readlines()
 #print(conj)
 #driver.get('https://docs.google.com/spreadsheets/d/1Xu_tOTT16isAvKHzF-4iPcKiX0Weg9T-/edit#gid=450512029')
 #time.sleep(10)
 #for i in range(2, 1294):
 # cell = 'G' + str(i)
 # driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').clear()
 # driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(cell)
 # driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(Keys.ENTER)
 # name = driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[3]/div[3]/div/div/div').text
 # for nome in nomes:
 #   if name == nome:
 #     cell = 'H' + str(i)
 #     driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').clear()
 #     driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(cell)
 #     driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(Keys.ENTER)
 #     email = driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[3]/div[3]/div/div/div').text
 #     if email != '':
 #       if len(list(emails_totais)) == 0:
 #         emails_totais.append(email)
 #       else:
 #         try:
 #           emails_totais.index(email)
 #         except ValueError:
 #           emails_totais.append(email)
 print('- Total de emails na planilha: ' + str(len(list(emails_totais))))
 # Escrever um email sobre
 email_a_serem_enviados = emails_totais
 driver.get('https://webmail.utfpr.edu.br/')
 time.sleep(3)
 try:
  driver.find_element(by='xpath', value='/html/body/div[2]/div[1]/form/table/tbody/tr[1]/td[2]/input').send_keys(user_emailpib)
  driver.find_element(by='xpath', value='/html/body/div[2]/div[1]/form/table/tbody/tr[2]/td[2]/input').send_keys(senha_emailpib)
  driver.find_element(by='xpath', value='/html/body/div[2]/div[1]/form/p/button').click()
 except NoSuchElementException:
  pass
 time.sleep(5)
 driver.find_element(by='xpath', value='/html/body/div[2]/div[1]/a[2]').click()
 time.sleep(5)
 for k in range(0, int(len(list(email_a_serem_enviados))/50)):
  for l in range(0, 50):
   ind = k*50 + l
   try:
    action.send_keys(email_a_serem_enviados[ind]).perform()
    time.sleep(1)
    action.send_keys(Keys.ENTER).perform()
    action.send_keys(', ').perform()
   except IndexError:
    pass
  # Assunto
  action.send_keys(Keys.TAB).perform()
  action.send_keys('Informativo DEICT 01 2023 - Indicação do estudante').perform()
  action.send_keys(Keys.TAB).perform()
  # Texto
  #action.key_down(Keys.CONTROL).send_keys('b').key_up(Keys.CONTROL).perform()
  action.send_keys('Prezados Pesquisadores').perform()
  action.send_keys(Keys.ENTER).perform()
  action.send_keys('Parabéns pela admissibilidade nos Editais de Iniciação Científica e Tecnológica Ciclo 2023-2024.').perform()
  action.send_keys(Keys.ENTER).perform()
  action.send_keys('Essa foi a primeira etapa! Lembrando que a admissibilidade não é sinônimo de recebimento de cota. A concorrência ainda continua.').perform()
  action.send_keys(Keys.ENTER).perform()
  action.send_keys('A segunda etapa é a indicação do(a) estudante com a submissão do Plano de Trabalho.').perform()
  action.send_keys(Keys.ENTER).perform()
  action.send_keys('Prazo para indicação dos estudantes: 07 de junho a 08 de julho/2023.').perform()
  action.send_keys(Keys.ENTER).perform()
  action.send_keys('Os Planos de trabalho são analisados pelo Comitê Institucional de Iniciação Científica e Tecnológica e correm o risco de serem indeferidos por ausência de assinaturas, informações incorretas ou incompatibilidade das atividades.').perform()
  action.send_keys(Keys.ENTER).perform()
  action.send_keys('A atribuição de cotas é realizada conforme o quantitativo disponibilizado pelas agências de fomento para a UTFPR e a classificação do(a) pesquisador(a).').perform()
  action.send_keys(Keys.ENTER).perform()
  action.send_keys('O Plano de trabalho a ser preenchido é o Apêndice C disponível nos links dos Editais:').perform()
  action.send_keys(Keys.ENTER).perform()
  action.key_down(Keys.CONTROL).send_keys('b').key_up(Keys.CONTROL).perform()
  action.send_keys('PIBIC/PIBIC AF').perform()
  action.key_down(Keys.CONTROL).send_keys('b').key_up(Keys.CONTROL).perform()
  action.send_keys(Keys.ENTER).perform()
  action.send_keys('http://portal.utfpr.edu.br/editais/pesquisa-e-pos-graduacao/reitoria/programa-institucional-de-iniciacao-cientifica-pibic-e-programa-institucional-de-iniciacao-cientifica-acoes-afirmativas-pibic-af-ciclo-2023-2024').perform()
  action.send_keys(Keys.ENTER).perform()
  action.key_down(Keys.CONTROL).send_keys('b').key_up(Keys.CONTROL).perform()
  action.send_keys('PIBIC-EM').perform()
  action.key_down(Keys.CONTROL).send_keys('b').key_up(Keys.CONTROL).perform()
  action.send_keys(Keys.ENTER).perform()
  action.send_keys('http://portal.utfpr.edu.br/editais/pesquisa-e-pos-graduacao/reitoria/programa-institucional-de-iniciacao-cientifica-2013-ensino-medio-pibic-em-ciclo-2023-2024').perform()
  action.send_keys(Keys.ENTER).perform()
  action.send_keys('Pré-cadastro de estudantes externos: https://forms.gle/iLdEYL1hXpaX7gux7 ').perform()
  action.send_keys(Keys.ENTER).perform()
  action.send_keys('Após 48 horas do pré-cadastro, indicar o estudante no SISPEQ.').perform()
  action.send_keys(Keys.ENTER).perform()
  action.key_down(Keys.CONTROL).send_keys('b').key_up(Keys.CONTROL).perform()
  action.send_keys('PIBIT').perform()
  action.key_down(Keys.CONTROL).send_keys('b').key_up(Keys.CONTROL).perform()
  action.send_keys(Keys.ENTER).perform()
  action.send_keys('http://portal.utfpr.edu.br/editais/pesquisa-e-pos-graduacao/reitoria/programa-institucional-de-iniciacao-tecnologica-pibit-ciclo-2023-2024').perform()
  action.send_keys(Keys.ENTER).perform()
  action.send_keys(Keys.ENTER).perform()
  action.send_keys('Atenciosamente,').perform()
  action.send_keys(Keys.ENTER).perform()
  action.send_keys('Profª Sascha Habu').perform()
  input('Próximo? Ao final, clique no campo dos destinatários')
  time.sleep(10)  
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
  ids_pesquisadores = ['1000077717733917']
  partes = [['ProducoesCientificas', "artigos-completos", "artigo-completo"], ['Eventos', 'ParticipacaoEventos', 'layout-cell layout-cell-11'], ['Orientacoes', 'Orientacoesconcluidas', 'layout-cell layout-cell-11']]
  nome_publicacoes = []
  for id in ids_pesquisadores:
    driver1.get('http://lattes.cnpq.br/' + id)
    while True:
      if len(driver1.current_url.split('?')) == 1:
        time.sleep(3)
        break
    i = 1
    nome_pesq = str(driver1.title).split(' (')[1].replace(')','')
    publicacoes = []
    for parte in partes:
      par = []
      found_prod = 0
      # esse WHILE procura o campo de ProduçõesCientíficas
      while True:
        try:
          element = driver1.find_element(by='xpath', value='/html/body/div[1]/div[3]/div/div/div/div[' + str(i) + ']/a')
          driver1.execute_script("arguments[0].scrollIntoView(true);", element)
          a_name = element.get_attribute("name")
          if a_name == parte[0]:
            found_prod = 1
            j = 1
            # esse WHILE procura o campo artigos completos, dentro do produções
            while True:
              if parte[0] == "Eventos":
                div_id = driver1.find_element(by='xpath', value='/html/body/div[1]/div[3]/div/div/div/div[' + str(i) +']/div[' + str(j) + ']/div/a').get_attribute("name")
              elif parte[0] == 'Orientacoes':
                div_id = driver1.find_element(by='xpath', value='/html/body/div[1]/div[3]/div/div/div/div[' + str(i) +']/div/a[' + str(j) + ']').get_attribute("name")
              else:
                div_id = driver1.find_element(by='xpath', value='/html/body/div[1]/div[3]/div/div/div/div[' + str(i) +']/div/div[' + str(j) + ']').get_attribute("id")
              if div_id == parte[1]:
                k = 1
                # Esse procura os artigos individualmente e trata
                while True:
                  try:
                    if parte[0] == 'Orientacoes':
                      eleme = driver1.find_element(by='xpath', value='/html/body/div[1]/div[3]/div/div/div/div[' + str(i) +']/div/div[' + str(k) + ']')
                    else:
                      eleme = driver1.find_element(by='xpath', value='/html/body/div[1]/div[3]/div/div/div/div[' + str(i) +']/div/div[' + str(j) + ']/div[' + str(k) + ']')
                    driver1.execute_script("arguments[0].scrollIntoView(true);", eleme)
                    eleme_class = eleme.get_attribute('class')
                    if eleme_class == parte[2]:
                      publicacao = []
                      l = 1
                      # Já dentro da publicação
                      if parte[0] == 'Eventos':
                        event = driver1.find_element(by='xpath', value='/html/body/div[1]/div[3]/div/div/div/div[' + str(i) +']/div/div[' + str(j) + ']/div[' + str(k) + ']/div').text
                        publicacao.append(event)
                      elif parte[0] == 'Orientacoes':
                        event = driver1.find_element(by='xpath', value='/html/body/div[1]/div[3]/div/div/div/div[' + str(i) +']/div/div[' + str(k) + ']/div').text
                        try:
                          a = event.split(' ').index('Início:')
                        except ValueError:
                          publicacao.append(event)
                      else:
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
                            if tipo[0] == 'issn':
                              new_tip = ""
                              p = 0
                              for letter in tipo[1]:
                                if p == 4:
                                  new_tip = new_tip + '-' + letter
                                else:
                                  new_tip = new_tip + letter
                                p = p + 1
                              tipo[1] = new_tip
                            if tipo[0] == 'ano' or tipo[0] == 'issn' or tipo[0] == 'titulo' or tipo[0] == 'nomePeriodico':
                              publicacao.append([tipo[0], tipo[1]])
                          except IndexError:
                            pass
                      if publicacao != []:
                        par.append(publicacao)
                  except NoSuchElementException:
                    break
                  k = k + 1
                break
              j = j + 1
        except NoSuchElementException:
          pass
        if found_prod == 1 or i > 100:
          break
        else:
          i = i + 1
      publicacoes.append(par)
    nome_publicacoes.append([nome_pesq, publicacoes])
  for a in nome_publicacoes:
   print('\n\n--------------- ' + a[0])
   print("\n----- Publicações")
   for parte in a[1][0]:
    print('--- Título: ' + parte[2][1] + ' - do ano de ' + parte[0][1])
    print('- Periódico: ' + parte[3][1])
    print('- ISSN do periódico: ' + parte[1][1])
   print('\n----- Eventos')
   for parte in a[1][1]:
    print(parte)
   print('\n----- Orientações')
   for parte in a[1][2]:
    print(parte)
  f = input()
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
# 10) Programa catai
#
def catai():
  driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
  driver.maximize_window()
  action = ActionChains(driver)
  input("- Logue com sua conta google, depois aperte aqui ok")
  # pega os nomes da 3k
  nomes = []
  driver.get('https://docs.google.com/spreadsheets/d/1A7ToqN63RpSI4kH7mOpXkmvnJSnEdqDt/edit#gid=190066373')
  time.sleep(5)
  for a in range(3, 338):
    cell_name = 'A' + str(a)
    driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').clear()
    driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(cell_name)
    driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(Keys.ENTER)
    name = str(driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[3]/div[3]/div/div/div').text)
    nomes.append(name)
  # pega os dados da bruta
  nomes_dados = []
  driver.get('https://docs.google.com/spreadsheets/d/1eKFfzhypr8gh0IlKDfrYgpTtg7r5mGiX/edit#gid=1966649337')
  time.sleep(5)
  for b in range(5, 53380):
    cell_name = 'B' + str(b)
    cell_tipo_agrupador = 'F' + str(b)
    cell_tipo_producao = 'G' + str(b)
    cell_snip = 'P' + str(b)
    driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').clear()
    driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(cell_name)
    driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(Keys.ENTER)
    name = str(driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[3]/div[3]/div/div/div').text)
    driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').clear()
    driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(cell_tipo_agrupador)
    driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(Keys.ENTER)
    tipo_agrupador = str(driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[3]/div[3]/div/div/div').text)
    driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').clear()
    driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(cell_tipo_producao)
    driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(Keys.ENTER)
    tipo_producao = str(driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[3]/div[3]/div/div/div').text)
    driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').clear()
    driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(cell_snip)
    driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(Keys.ENTER)
    snip = str(driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[3]/div[3]/div/div/div').text)
    nomes_dados.append([name, tipo_agrupador, tipo_producao, snip])  
  # filtro de pontuação
  nomes_pontos = []
  for parte in nomes_dados:
    pontos = 0
    if parte[1] == 'Producao bibliografica' and parte[2] == 'Artigo publicado em periodicos':
      try:
        if float(parte[3]) >= 1.501:
          pontos = 100
        elif float(parte[3]) <= 1.500 and float(parte[3]) >= 1.001:
          pontos = 75
        elif float(parte[3]) <= 1.000 and float(parte[3]) >= 0.501:
          pontos = 50
        elif float(parte[3]) <= 0.500 and float(parte[3]) >= 0.001:
          pontos = 25
        else:
          pontos = 0
      except ValueError:
        pass
    elif parte[1] == 'Orientacao concluida' and parte[2] == 'Dissertacao de mestrado':
      pontos = 5
    elif parte[1] == 'Orientacao concluida' and parte[2] == 'Iniciacao Cientifica':
      pontos = 2.5
    elif parte[1] == 'Orientacao concluida' and parte[2] == 'Tese de doutorado':
      pontos = 10
    elif parte[1] == 'Producao tecnica' and parte[2] == 'Programa de computador':
      pontos = 50
    elif parte[1] == 'Producao tecnica' and parte[2] == 'Patentes e registros':
      pontos = 150
    if pontos != 0:
      found = 0
      for partezinha in nomes_pontos:
        if partezinha[0] == parte[0]:
          found = 1
          partezinha[1] = partezinha[1] + pontos
      if found == 0:
        nomes_pontos.append([parte[0], pontos])
  # escreve os pontos na 3k
  driver.get('https://docs.google.com/spreadsheets/d/1A7ToqN63RpSI4kH7mOpXkmvnJSnEdqDt/edit#gid=190066373')
  time.sleep(5)
  for c in range(3, 338):
    cell_name = 'A' + str(c)
    cell_pont = 'M' + str(c)
    driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').clear()
    driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(cell_name)
    driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(Keys.ENTER)
    name = str(driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[3]/div[3]/div/div/div').text)
    for nomes in nomes_pontos:
      if nomes[0] == name:
        driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').clear()
        driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(cell_pont)
        driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(Keys.ENTER)
        driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[3]/div[3]/div/div/div').send_keys(str(nomes[1]).replace('.', ','))
        action.send_keys(Keys.ENTER).perform()
  time.sleep(5)
#
# 11) exclui linha de planilha
#
def exclui_linha():
  driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
  driver.maximize_window()
  action = ActionChains(driver)
  input("- Logue com sua conta google, depois aperte aqui ok")
  # pega os nomes da 3k
  nomes = []
  driver.get('https://docs.google.com/spreadsheets/d/1A7ToqN63RpSI4kH7mOpXkmvnJSnEdqDt/edit#gid=190066373')
  time.sleep(5)
  for a in range(3, 338):
    cell_name = 'A' + str(a)
    driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').clear()
    driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(cell_name)
    driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(Keys.ENTER)
    name = str(driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[3]/div[3]/div/div/div').text)
    nomes.append(name)
  # compara com os da bruta
  driver.get('https://docs.google.com/spreadsheets/d/1eKFfzhypr8gh0IlKDfrYgpTtg7r5mGiX/edit#gid=1966649337')
  time.sleep(5)
  b = 3
  while b < 53380:
    cell_name = 'B' + str(b)
    driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').clear()
    driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(cell_name)
    driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(Keys.ENTER)
    name = str(driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[3]/div[3]/div/div/div').text)
    try:
     nomes.index(name)
     b = b + 1
    except ValueError:
     action.key_down(Keys.ALT).send_keys('E').key_up(Keys.ALT).perform()
     action.send_keys('D').perform()
     action.send_keys('D').perform()
  time.sleep(5)
#
# 12) Programa Ju
#
def ju():
 driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
 driver.maximize_window()
 action = ActionChains(driver)
 dados = []
 driver.get('https://docs.google.com/spreadsheets/d/1Xu_tOTT16isAvKHzF-4iPcKiX0Weg9T-/edit#gid=450512029')
 input('Deixe a planilha no jeito certo')
 time.sleep(5)
 a = 2
 b = True
 while b:
  cell_campus = 'A' + str(a)
  cell_proposta = 'B' + str(a)
  cell_orient_name = 'G' + str(a)
  cell_orient_email = 'H' + str(a)
  cell_est_name = 'K' + str(a)
  cell_est_curso = 'M' + str(a)
  cell_est_situacao_14022023 = 'N' + str(a)
  cell_est_banco = 'S' + str(a)
  cell_est_agencia = 'T' + str(a)
  cell_est_dv = 'U' + str(a)
  cell_est_conta = 'V' + str(a)
  cell_est_oper = 'W' + str(a)
  cell_modalidade = 'X' + str(a)
  cell_fomento = 'Z' + str(a)
  cell_observacao = 'AA' + str(a)
  cell_inicio_proj = 'AC' + str(a)
  cell_final_proj = 'AD' + str(a)
  idas = [cell_campus, cell_proposta, cell_orient_name, cell_orient_email, cell_est_name, cell_est_curso, cell_est_situacao_14022023, cell_est_banco, cell_est_agencia, cell_est_dv, cell_est_conta, cell_est_oper, cell_modalidade, cell_fomento, cell_observacao, cell_inicio_proj, cell_final_proj]
  datas = []
  for cell in idas:
    driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').clear()
    driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(cell)
    driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(Keys.ENTER)
    data = str(driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[3]/div[3]/div/div/div').text)
    cor_cell = driver.find_element(by='xpath', value='/html/body/div[2]/div[4]/div[2]/div[1]/div[2]/div[26]/div/div/div/div').get_attribute('style').split('border-bottom-color: rgb(')[1].split(');')[0]
    cor_r = cor_cell.split(', ')[0]
    cor_g = cor_cell.split(', ')[1]
    cor_b = cor_cell.split(', ')[2]
    if cell == cell_est_name and data != "":
     datas.append(data)
    elif cell == cell_est_name and data == "":
      b = False
  if b != False:
   dados.append(datas)
   a = a + 1
 utfpr = []
 arauc = []
 cnpq = []
 month = datetime.now().strftime("%m")
 year = datetime.now().strftime("%Y")
 day = datetime.now().strftime ("%d")
 for parte in dados:
  campus = parte[0]
  proposta = parte[1]
  orient_name = parte[2]
  orient_email = parte[3]
  est_name = parte[4]
  est_curso = parte[5]
  est_situacao_14022023 = parte[6]
  est_banco = parte[7]
  est_agencia = parte[8]
  est_dv = parte[9]
  est_conta = parte[10]
  est_oper = parte[11]
  modalidade = parte[12]
  fomento = parte[13]
  observacao = parte[14]
  inicio_proj = parte[15]
  final_proj = parte[16]
  if final_proj == "" or final_proj.split('/')[2] < year or (final_proj.split('/')[2] == year and final_proj.split('/')[1] < month) or (final_proj.split('/')[2] == year and final_proj.split('/')[1] == month and final_proj.split('/')[0] < day):
   d = [fomento, est_name, modalidade]
   if fomento == 'UTFPR':
    utfpr.append(d)
   elif fomento == 'CNPq':
    cnpq.append(d)
   elif fomento == 'Fund Arauc':
    arauc.append(d)
 fomentos = [utfpr, arauc, cnpq]
 for fom in fomentos:
   if len(fom) > 0:
    print('----- ' + fom[0][0] + '-----')
    for parte in fom:
     print(' - ' + parte[1] + ': ' + parte[2])
#
# 13) Pegar .txt
#
def jutxt():
 pares = []
 tr_lines = []
 trf_lines = []
 fil = open("C:/Users/DIREPQ/Desktop/cnpq.txt", 'r')
 conj = fil.read()
 # Divisão dos <tr e </tr
 for i in range(0, len(conj) - 2):
  try:
    if str(conj[i] + conj[i + 1] + conj[i + 2]) == '<tr':
     tr_lines.append(i)
    elif str(conj[i] + conj[i + 1] + conj[i + 2] + conj[i + 3]) == '</tr':
     trf_lines.append(i)
  except IndexError:
   pass
 # Trabalha no espaçõ entre o <tr e </tr
 for a in range(0, len(tr_lines)):
  comeco_line = tr_lines[a]
  fim_line = trf_lines[a]
  dados = []
  # Analisa o intervalo
  for b in range(comeco_line, fim_line + 1):
   try:
    if str(conj[b] + conj[b + 1] + conj[b + 2] + conj[b + 3] + conj[b + 4]) == 'title':
     # Pega o nome se encontrou Title
     comeco_nome = 0
     fim_nome = 0
     nome = ""
     for c in range(b, fim_line):
      if comeco_nome == 0:
       if conj[c] == '"':
        comeco_nome = c + 1
      elif comeco_nome != 0 and fim_nome == 0:
       if conj[c] == '"':
        fim_nome = c
        break
     for d in range(comeco_nome, fim_nome):
      nome = nome + conj[d]
     nome = nome.replace('Ã§', 'ç').replace('Ã£', 'ã').replace('Ã¡', 'á').replace('Ã', 'í').replace('í©', 'é').replace('í¡', 'á').replace('í£', 'ã').replace('í´', 'ô').replace('íª', 'ê').replace('í³', 'ó').replace('í¢', 'â').replace('íº', 'ú')
     nome = nome.replace('ç', 'c').replace('í', 'i').replace('é', 'e').replace('á', 'a').replace('ã', 'a').replace('ô', 'o').replace('ê', 'e').replace('ó', 'o').replace('â', 'a').replace('ú', 'u')
     dados.append(nome)
   except IndexError:
    pass
  if len(dados) == 3:
   try:
    pares.index(dados)
   except ValueError:
    pares.append(dados)
  else:
   # Pegar o nome na segunda <td
   found = 0
   for b in range(comeco_line, fim_line + 1):
    try:
     if str(conj[b] + conj[b + 1] + conj[b + 2]) == '<td':
      found = found + 1
      if found == 2:
       comeco_linetd = b
       for c in range(b, fim_line):
         if str(conj[c] + conj[c + 1] + conj[c + 2] + conj[c + 3]) == '</td':
          fim_linetd = c
       comeconome = 0
       fimnome = 0
       for d in range(comeco_linetd + 2, fim_linetd):
        if conj[d] == '>' and comeconome == 0:
         comeconome = d
        elif conj[d] == '<' and fimnome == 0:
         fimnome = d
       name = ""
       for e in range(comeconome + 1, fimnome):
        name = name + conj[e]
       dado2 = dados[1]
       name = name.replace('Ã§', 'ç').replace('Ã£', 'ã').replace('Ã¡', 'á').replace('Ã', 'í').replace('í©', 'é').replace('í¡', 'á').replace('í£', 'ã').replace('í´', 'ô').replace('íª', 'ê').replace('í³', 'ó').replace('í¢', 'â').replace('íº', 'ú')
       name = name.replace('ç', 'c').replace('í', 'i').replace('é', 'e').replace('á', 'a').replace('ã', 'a').replace('ô', 'o').replace('ê', 'e').replace('ó', 'o').replace('â', 'a').replace('ú', 'u')
       dados[1] = name
       dados.append(dado2)
       pares.append(dados)
    except IndexError:
     pass
 fil.close()
 driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
 action = ActionChains(driver)
 driver.get('https://docs.google.com/spreadsheets/d/1pgL7Ji_jwQSehd8QonbSLb1O8tNEvjClOE4N2lORaYI/edit#gid=0')
 time.sleep(3)
 for par in pares:
   i = pares.index(par) + 2
   cella = 'A' + str(i)
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').clear()
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(cella)
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(Keys.ENTER)
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[3]/div[3]/div/div/div').send_keys(par[0])
   action.send_keys(Keys.ENTER).perform()
   cellb = 'B' + str(i)
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').clear()
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(cellb)
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(Keys.ENTER)
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[3]/div[3]/div/div/div').send_keys(par[1])
   action.send_keys(Keys.ENTER).perform()
   cella = 'C' + str(i)
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').clear()
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(cella)
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(Keys.ENTER)
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[3]/div[3]/div/div/div').send_keys(par[2])
   action.send_keys(Keys.ENTER).perform()
 time.sleep(10)
#
# 14) Exclui repetidos
#
def sascha():
 driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
 driver.maximize_window()
 action = ActionChains(driver)
 input("- Logue com sua conta google, depois aperte aqui ok")
 # pega os nomes da 3k
 driver.get('https://docs.google.com/spreadsheets/d/1A7ToqN63RpSI4kH7mOpXkmvnJSnEdqDt/edit#gid=190066373')
 time.sleep(5)
 dados = []
 for a in range(2, 772):
   cell_name = 'G' + str(a)
   cell_data = 'I' + str(a)
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').clear()
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(cell_name)
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(Keys.ENTER)
   name = str(driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[3]/div[3]/div/div/div').text)
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').clear()
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(cell_data)
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(Keys.ENTER)
   data = str(driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[3]/div[3]/div/div/div').text)
   if len(dados) == 0:
    dados.append([name, data])
   elif len(dados) == 1:
    if dados[0][0] == name:
     dados.append([name, data])
    else: # dados[0][0] != name
     dados.clear()
     dados.append([name, data])
   else: #len(dados) > 1
    if dados[0][0] == name:
     dados.append([name, data])
    else: #dados[0][0] != name ====> foram encontradas inscrições iguais, logo deve ser feito o filtro
     imd = 0
     for inscricao in dados:
      # Conclui qual é a data mais recente
      data_dmy = inscricao[1].split(' ')[0]
      data_hour = inscricao[1].split(' ')[1]
      if dados.index(inscricao) != 0:
       data_day_atual = data_dmy.split('-')[0]
#
# 15) Ver dados e compara
#
def dado():
 driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
 driver.maximize_window()
 action = ActionChains(driver)
 input("- Logue com sua conta google, depois aperte aqui ok")
 edital_nome = []
 # pega os nomes da gerencal
 driver.get('https://docs.google.com/spreadsheets/d/1Opu9K2iLakkqjnQd0HyWH7rFFnwg8bkq/edit#gid=1096389799')
 time.sleep(5)
 for a in range(3, 834):
   cell_edital = 'A' + str(a)
   cell_name = 'C' + str(a)
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').clear()
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(cell_edital)
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(Keys.ENTER)
   edital = str(driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[3]/div[3]/div/div/div').text)
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').clear()
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(cell_name)
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(Keys.ENTER)
   name = str(driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[3]/div[3]/div/div/div').text)
   try:
    edital_nome.index([name, edital])
   except ValueError:
    edital_nome.append([name, edital])
 driver.get('https://docs.google.com/spreadsheets/d/1NljayKgh5lSxgo2HzDD_MSqAvJFXHXMr/edit#gid=1164543333')
 time.sleep(5)
 for a in range(2, 772):
   cell_edital = 'B' + str(a)
   cell_name = 'G' + str(a)
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').clear()
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(cell_edital)
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(Keys.ENTER)
   edital = str(driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[3]/div[3]/div/div/div').text).split(" ")[0]
   if edital == 'PIBIC-EM':
    edital = 'PIBIC EM'
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').clear()
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(cell_name)
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(Keys.ENTER)
   name = str(driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[3]/div[3]/div/div/div').text)
   try:
    edital_nome.index([name, edital])
   except ValueError:
    print(' - ' + name + ' não está na planilha "Lista Gerencial ICT 2023 24" na modalidade ' + edital)
#
# 16) Dados catai
#
def dado_catai():
 driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
 driver.maximize_window()
 action = ActionChains(driver)
 nome_campus = []
 # pega os nomes da gerencal
 driver.get('https://docs.google.com/spreadsheets/d/1-VnRwvHD_8B5V6vswSvgV2UzTgGv11na/edit#gid=315836080')
 time.sleep(5)
 for a in range(3, 203):
   cell_name = 'B' + str(a)
   cell_campus = 'C' + str(a)
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').clear()
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(cell_name)
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(Keys.ENTER)
   name = str(driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[3]/div[3]/div/div/div').text).upper()
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').clear()
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(cell_campus)
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(Keys.ENTER)
   campus = str(driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[3]/div[3]/div/div/div').text).upper()
   try:
    nome_campus.index([name, campus])
   except ValueError:
    nome_campus.append([name, campus])
 # Pega da outra planilha
 driver.get('https://docs.google.com/spreadsheets/d/1Ek7vKjogBIeLED33g-na_DfHbq81yDh6/edit#gid=1793723543')
 time.sleep(5)
 for a in range(3, 47):
   cell_name = 'B' + str(a)
   cell_campus = 'C' + str(a)
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').clear()
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(cell_name)
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(Keys.ENTER)
   name = str(driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[3]/div[3]/div/div/div').text).upper()
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').clear()
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(cell_campus)
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(Keys.ENTER)
   campus = str(driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[3]/div[3]/div/div/div').text).upper()
   try:
    nome_campus.index([name, campus])
   except ValueError:
    nome_campus.append([name, campus])
 # compara
 campara = []
 driver.get('https://docs.google.com/spreadsheets/d/15PPzydMN-2Gv9T5ajlzGAiml9JkHMnCZ/edit#gid=2105366550')
 time.sleep(5)
 for a in range(11, 2567):
   cell_name = 'B' + str(a)
   cell_porra = 'I' + str(a)
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').clear()
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(cell_name)
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(Keys.ENTER)
   name = str(driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[3]/div[3]/div/div/div').text).upper()
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').clear()
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(cell_porra)
   driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[1]/input').send_keys(Keys.ENTER)
   campus1 = str(driver.find_element(by='xpath', value='/html/body/div[2]/div[8]/div[6]/div[3]/div[3]/div/div/div').text).replace(' ', '')
   try:
    campus = str(campus1[len(campus1) - 2] + campus1[len(campus1) - 1]).upper()
    try:
     campara.index([name, campus])
    except ValueError:
     campara.append([name, campus])
   except IndexError:
    pass
 for parte in nome_campus:
  found = 0
  for parte2 in campara:
   if parte[0] == parte2[0]:
    found = 1
    if parte[1] != parte2[1]:
     print('- ' + parte[0] + ': encontrado no campus ' + parte[1] + ', porém é do campus ' + parte2[1])
  if found == 0:
   print('- ' + parte[0] + ': encontrado no campus ' + parte[1] + ', porém não foram encontrados dados para confirmação')
#
# Menu
#
def menu():
 txt = ['Olá :)\n', '1) Email Sub FA', '2) Prof planilha', '3) Email ICT', '4) Estatística relatório parcial ICT', '5) Coleta Lattes', '6) Colocar CPF', '7) Change Char', '8) Catai', '9) Exclui linhas', '10) Ju', '11) Ju txt', '12) dado', '13) Dado catai']
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
  elif escolha == '8':
   print('- Executando: ' + txt[int(escolha)].split(') ')[1])
   catai()
   break
  elif escolha == '9':
   print('- Executando: ' + txt[int(escolha)].split(') ')[1])
   exclui_linha()
   break
  elif escolha == '10':
   print('- Executando: ' + txt[int(escolha)].split(') ')[1])
   ju()
   break
  elif escolha == '11':
   print('- Executando: ' + txt[int(escolha)].split(') ')[1])
   jutxt()
   break
  elif escolha == '12':
   print('- Executando: ' + txt[int(escolha)].split(') ')[1])
   dado()
   break
  elif escolha == '13':
   print('- Executando: ' + txt[int(escolha)].split(') ')[1])
   dado_catai()
   break
  else:
   print('Tente novamente! Número inválido')
 menu()
menu()
f=input('fim')
