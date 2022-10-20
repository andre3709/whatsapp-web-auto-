from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
for c in range(0,40): # tempo para carregar o site
    print(c)
    sleep(1)
print('Continuando programa..')
des = str(input('Deseja Enviar msg automática no grupo 201?: '))
while True:
    if des in 'Ss':
        ok = True
        break
    elif des in 'Nn':
        ok = False
        break
    else:
        opc = str(input('Opção válida, digite apenas S ou N')).upper()
        continue

def linha(tam = 42):
    return '-' * 42


def cabeça(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    c = 1
    for item in lista:
        print(f'\033[33m{c} - \033[m \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = int(input('Sua Opção: '))
    return opc

def Msg_de_hoje(): # referente a escola onde estudo, onde na turma 201° ano os tempos de aula são esses a partir do 4° bimestre de 2022. OBS: vai apenas de segunda a sexta.
    from datetime import datetime
    from datetime import date
    mes = date.today().month
    dia = date.today().weekday()
    d = date.today().day
    ano = date.today().year
    diasema = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
    dhoje = f'--{diasema[dia]}-- {d}/{mes}/{ano}'
    hoje = datetime.today().weekday()
    dis = ['Português','Matemática','Biologia','Química','Física','Geografia','História','Inglês','Espanhol','Educacação_Física','Filosofia','Sociologia']
    if hoje == 0:
        msg = f"== BOM DIA! == \nHoje {dhoje} \nos tempos de aula São: \n1° -{dis[8]:_<21} \n2° -{dis[1]:_<21} \n3° -{dis[5]:_<21} \n4° -{dis[10]:_<21}\n"
    elif hoje == 1:
        msg = f"== BOM DIA! == \nHoje {dhoje} \nos tempos de aula São: \n1° -{dis[4]:_<21} \n2° -{dis[6]:_<21} \n3° -{dis[0]:_<21} \n4° -{dis[2]:_<21} \n5° -{dis[1]:_<21}\n"
    elif hoje == 2:
        msg = f"== BOM DIA! == \nHoje {dhoje} \nos tempos de aula São: \n1° -{dis[2]:_<21} \n2° -{dis[1]:_<21} \n3° -{dis[9]:_<21} \n4° -{dis[3]:_<21}\n"
    elif hoje == 3:
        msg = f"== BOM DIA! == \nHoje {dhoje} \nos tempos de aula São: \n1° -{dis[1]:_<21} \n2° -{dis[5]:_<21} \n3° -{dis[4]:_<21} \n4° -{dis[7]:_<21} \n5° -{dis[0]:_<21}\n"
    elif hoje == 4:
        msg = f"== BOM DIA! == \nHoje {dhoje} \nos tempos de aula São: \n1° -{dis[6]:_<21} \n2° -{dis[3]:_<21} \n3° -{dis[0]:_<21} \n4° -{dis[11]:_<21}\n"
    elif hoje == 6:
        msg = 'Hoje é domingo, pé de cachimbo, cachimbo é de ouro...'
    return msg

def buscar_contato(contato): # busca o contanto, podendo ser grupo. 
    campoP = driver.find_element("xpath",'//div[contains(@class,"copyable-text selectable-text")]') 
    sleep(5)
    campoP.click()
    sleep(1)
    campoP.send_keys(contato)
    sleep(1)
    campoP.send_keys(Keys.ENTER)
    sleep(1)


def enviarM_elogOut(mensagem,sim=False):    
    campoM = driver.find_element("xpath",'//p[contains(@class,"selectable-text copyable-text")]') #erro era o //div que era pra ser //p  <- erro percebido e corrigido por mim. andre3709
    sleep(5)
    campoM.click()
    sleep(1)
    campoM.send_keys(mensagem)
    sleep(5)
    try:
        campoM.send_keys(Keys.ENTER)
    except:
        print('Mensagem Enviada.')
    sleep(5)
    if sim: # se sim = False, o programa não deslogará automaticamente.
        print('Encerrando programa')
        Menu = driver.find_elements("xpath",'//span[contains(@data-icon, "menu")]')
        sleep(2)
        Menu[0].click()
        Fechar = driver.find_element("xpath",'//div[contains(@aria-label,"Desconectar")]')
        sleep(2)
        Fechar.click()
        confirma = driver.find_element("xpath", '//div[contains(@class, "_20C5O _2Zdgs")]')
        sleep(2)
        confirma.click()
        sleep(10)
        driver.close()

if ok == False:
    opci = ['Grupo 201','Escolher contato: ']
    opc = menu(opci)
    while True:
        if opc == 1:
            ctt = '_Turma 201_'
            break
        elif opc == 2:
            ctt = str(input('Digite o nome do Contato: ')) #no momento, programa irá enviar mensagem para 1 grupo ou contato por vês.
            print(f'Buscando contato {ctt}')
            break
        else:
            print(f'opção Inválida: digite um valor válido entre 1 e {len(opci)} ')
            menu(opci)
            continue
    msge = ['Mensagem do dia para o grupo 201','Personalizar Mensagem']
    opc1 = menu(msge)
    while True:
        if opc1 == 1:
            mensagem = Msg_de_hoje()
            break
        elif opc1 == 2:
            mensagem = str(input(f'Digite sua mensagem para {ctt}:'))
            break
        else:
            print(f'opção Inválida: digite um valor válido entre 1 e {len(opci)} ')
            menu(msge)
            continue
else:
    ctt = '_Turma 201_'
    mensagem = Msg_de_hoje()

contatos = ctt # se aqui for uma lista com mais de 1 contato, deverá criar um for para enviar as msg para todos os contatos na lista.

buscar_contato(contatos)

if ok == False:
    opc = str(input('Deseja deslogar?: '))
    while True:
        if opc in "Ss":
            sim = True
            break
        elif opc in "Nn":
            sim  = False
            break
        else:
            opc = str(input('Opção válida, digite apenas S ou N')).upper()
            continue
else:
    sim = True
enviarM_elogOut(mensagem,sim)

    
