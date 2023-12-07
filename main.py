import pyautogui
import time
import pandas as pd

# abrir o Chrome
pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(10)

# Clica na area de pesquisa
pyautogui.click(x=-1676, y=57)

# entrar no link
link = "https://www.virustotal.com/"

pyautogui.write(link)
pyautogui.press("enter")

# esperar o site carregar
time.sleep(4)

# Importa a tabela
    
# Carrega o txt com o Search a ser procurado
search_hashs = pd.read_csv('pags_pesquisa1.txt')
print(search_hashs)


count_num = 1
#count_pag = 1
for hash in search_hashs['Search_Paginas']:
    print(hash)

    count_num = count_num + 1  #(3)

    # Aperta no Button de Search da página
    pyautogui.click(x=-742, y=395, button="right")                
    #time.sleep(2)
    # Abre uma nova guia
    pyautogui.click(x=-709, y=406, button="left")
    time.sleep(2)


    # Passa para a nova guia
    pyautogui.hotkey('ctrl', "pgup")
    print(count_num)
    pyautogui.write(f"{hash}")
    pyautogui.press("enter")
    time.sleep(2)

    # Volta para a aba de pesquisa e pesquisa outro hash
    pyautogui.hotkey('ctrl', '1')