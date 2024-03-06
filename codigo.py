#Passo a passo do projeto de Automação
#passo 1: Enter no sistema da empresa
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(3)

# Passo 2: Fazer login

pyautogui.click(x=782, y=353)
pyautogui.write("emailteste@gmail.com")
pyautogui.press("tab")
pyautogui.write("senhateste")

pyautogui.click(x=942, y=512)
time.sleep(3)

# Passo 3: Importar a base de dados

import pandas
tabela = pandas.read_csv("produtos.csv")

# Passo 4: Cadastrar os produtos

for linha in tabela.index:
    pyautogui.click(x=756, y=232)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
   
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
   
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
   
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")
    pyautogui.scroll(5000)   

# Passo 5: Repetir o processo de cadastro até acabar a base de dados