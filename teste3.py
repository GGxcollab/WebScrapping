from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui
import time
import pandas as pd

#servico = Service(ChromeDriverManager().install())
# Criar o navegador
nav = webdriver.Chrome()


# Entrar no navegador 
arquivo = 'https://www.virustotal.com/'
nav.get(arquivo)
# esperar o site carregar
time.sleep(5)

# Importa a tabela
    # Carrega o txt com o Search a ser procurado
search_hashs = pd.read_csv('pags_pesquisa1.txt')
print(search_hashs)


#count_num = 1
#count_pag = 1
for hash in search_hashs['Search_Paginas']:
    print(hash)

    #count_num = count_num + 1  #(3)

    # Aperta no Button de Search da página
    pyautogui.click(x=921, y=433, button="right")                
    #time.sleep(2)
    # Abre uma nova guia
    pyautogui.click(x=944, y=447, button="left")
    time.sleep(2)


    # Passa para a nova guia
    pyautogui.hotkey('ctrl', "pgup")
    pyautogui.write(f"{hash}")
    pyautogui.press("enter")
    time.sleep(4)



time.sleep(2000)
    # Volta para a aba de pesquisa