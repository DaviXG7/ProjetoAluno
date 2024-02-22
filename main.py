from tkinter import VERTICAL

import Janelas
import tkinter as tk


# Criar a janela principal
janela_principal = tk.Tk()

Janelas.tela_inicial()

tk.Label(janela_principal, text="Janela principal, infelizmente não da para fechar! Sou iniciante com tkinter").grid(row=0, column=0)

janela_principal.mainloop()
