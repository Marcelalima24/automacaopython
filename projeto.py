import pyautogui
import time
pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

# Passo 2 :Fazer login

pyautogui.click(x=1459, y=372)
pyautogui.write("emailteste@gmail.com")
pyautogui.press("tab")
pyautogui.write("senhateste")
pyautogui.press("enter")


# Passo 3: Importar base de dados

import pandas
tabela = pandas.read_csv("produtos.csv")
print (tabela)

# Passo 4: Cadastrar 1 produto
pyautogui.click(x=1493, y=258)

linha = 0

for linha in tabela.index:
    pyautogui.click(x=1493, y=258)
    
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    pyautogui.write(str(obs))
    pyautogui.press ("tab")
    
    pyautogui.press("enter")
    pyautogui.scroll(5000)
        


    