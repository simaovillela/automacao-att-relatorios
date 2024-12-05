import pyautogui
import time
import os

# Função para abrir o Excel e esperar um pouco para garantir que o arquivo carregue
def abrir_excel(arquivo):
    os.startfile(arquivo)  
    time.sleep(10)  

# Função para clicar no botão de atualizar
def clicar_atualizar():
    pyautogui.hotkey('enter')  
    time.sleep(240)  

# Função para salvar e fechar o Excel
def salvar_fechar_excel():
    pyautogui.click(1054, 328)
    time.sleep(15)

# Lista de arquivos Excel na mesma pasta
caminho_pasta = r"C:\ACOMP_SV"  
arquivos_excel = [
    os.path.join(caminho_pasta, "Acomp_SV01.xlsm"),
    os.path.join(caminho_pasta, "Acomp_SV02.xlsm"),
    os.path.join(caminho_pasta, "Acomp_SV03.xlsm"),
    os.path.join(caminho_pasta, "Acomp_SV04.xlsm")
]

# Processo para abrir, atualizar, salvar e fechar cada arquivo
for arquivo in arquivos_excel:
    abrir_excel(arquivo)  
    clicar_atualizar()    
    salvar_fechar_excel() 
