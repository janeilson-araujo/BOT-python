import pyautogui 
import time
import pandas as pd 

pyautogui.PAUSE = 4

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(15)
pyautogui.click(x=490 , y=926)
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
pyautogui.click(x=802, y=484)
pyautogui.write("janeilson@gmail.com")
pyautogui.press("tab")
pyautogui.write("1234")
pyautogui.press("tab")
pyautogui.press("enter")

tabela = pd.read_csv("produtos.csv")

for L in tabela.index:
    pyautogui.click(x=511, y=340)
    pyautogui.write(str(tabela.loc[L , "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[L , "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[L , "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[L , "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[L , "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[L , "custo"]))
    pyautogui.press("tab")
    if not pd.isna("obs"):
        pyautogui.write(str(tabela.loc[L , "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(10000)