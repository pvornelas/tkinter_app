from tkinter import messagebox

def sobre():
    messagebox.showinfo(title="Sobre", message="Ferramentas de apoio às unidades da SEV Araraquara.\nDesenvolvido por Paulo V. Ornelas - c147712.")

def texto():
    return """Olá {cliente}, tudo bem?
Caso escolher enviar a mensagem com o nome do cliente, a mensagem deverá conter a palavra cliente entre chaves para que o programa substitua pelo nome contido na planilha de base."""