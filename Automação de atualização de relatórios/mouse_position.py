import tkinter as tk
import pyautogui

# Função para atualizar as coordenadas do mouse
def update_coordinates():
    # Captura as coordenadas do mouse
    x, y = pyautogui.position()
    label.config(text=f"Coordenadas: x={x}, y={y}")
    # Atualiza a cada 10ms (ajuste esse valor conforme necessário)
    root.after(10, update_coordinates)

# Configuração da interface gráfica com tkinter
root = tk.Tk()
root.title("Coordenadas do Mouse")

# Criando o label para exibir as coordenadas
label = tk.Label(root, text="Coordenadas: x=0, y=0", font=("Arial", 14))
label.pack(padx=10, pady=10)

# Inicia o loop de atualização das coordenadas
update_coordinates()

# Rodando o loop da interface gráfica
root.mainloop()
