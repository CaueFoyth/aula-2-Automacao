# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa

# Entrar no link https://dlp.hashtagtreinamentos.com/python/intensivao/login
# pip install pyautogui

import pyautogui
import time

# pyautogui.write -> Escrever um texto
# pyautogui.press -> Apertar uma tecla
# pyautogui.click -> Clicar em algum lugar
# pyautogui.hotkey -> Combinação de teclas

pyautogui.PAUSE = 0.5

# Abrir navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(1)

# Entrar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

# Passo 2: Fazer login
# Selecionar o campo de email
# pyautogui.click(x=474, y=357)

# Escrever o email
pyautogui.press("tab")
pyautogui.write("foythcaue@gmail.com")

# Escrever senha
pyautogui.press("tab")
pyautogui.write("1234")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)

# Passo 3: Importar a base de produtos
import pandas as pd

tabela = pd.read_csv("produtos.csv")
pyautogui.press("tab")
    
# Passo 4: Cadastrar o produto

linha = 0
for linha in tabela.index:
    
    time.sleep(1)
    # Clicar no campo de código

    # Pegar a tabela do valor do campo
    codigo = tabela.loc[linha, "codigo"]

    # Preencher o campo
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    codigo = tabela.loc[linha, "marca"]
    pyautogui.write(str(codigo))

    pyautogui.press("tab")
    codigo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(codigo))

    pyautogui.press("tab")
    codigo = tabela.loc[linha, "categoria"]
    pyautogui.write(str(codigo))

    pyautogui.press("tab")
    codigo = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(codigo))

    pyautogui.press("tab")
    codigo = tabela.loc[linha, "custo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    if not pd.isna(tabela.loc[linha, "obs"]):
        codigo = tabela.loc[linha, "obs"]
        pyautogui.write(str(codigo))

    pyautogui.press("tab")
    pyautogui.press("enter") # Botão para enviar o formulário

    # Passo 5: Cadastrar até acabar os produtos
    # Dar um scroll full pra cima

    time.sleep(1)
    pyautogui.scroll(10000)
    pyautogui.click(x=459, y=239)

