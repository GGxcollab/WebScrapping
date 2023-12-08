import pyautogui
import time
import pandas as pd


# Carrega o txt com o Search a ser procurado
search_hashs = pd.read_csv('pags_pesquisa1.txt')
print(search_hashs)


# abrir o Chrome
pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(3)

# Clica na area de pesquisa

# pyautogui.click(x=-1676, y=57)

count_num = 1
# #count_pag = 1

for hash in search_hashs['Search_Paginas']:
    print(hash)

    count_num = count_num + 1  #(3)
    print(count_num)
    # entrar no link
    link = "https://www.virustotal.com/"
    pyautogui.write(link)
    pyautogui.press("enter")

    # esperar o site carregar
    time.sleep(4)

    # navega ate o "search" atraves do tab
    pyautogui.press('tab', presses=10)
    pyautogui.press("enter")
    time.sleep(3)

    # Entra no espaço de escrita e preescreve a hash que vai ser utilizada pelo txt "pags_pesquisa1"
    pyautogui.press('tab')
    pyautogui.write(f"{hash}")
    pyautogui.press("enter")

    # abre uma nova aba/guia
    pyautogui.hotkey('ctrl', "t")