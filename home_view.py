import tkinter as tk
import utils as U

class HomePage(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)

        self.rowconfigure([0, 1, 2, 3, 4], weight=1, minsize=50)
        self.columnconfigure([0, 1, 2, 3], weight=1, minsize=75)

        lb_titulo = tk.Label(self, text="Instruções", font=("bold", 16))
        lb_titulo.grid(row=0, column=0, pady=20, padx=20, rowspan=2, columnspan=4, sticky=tk.N)

        text_instrucao = tk.Label(self, text=self.instructions_text, font=(10), wraplength=610, justify=tk.LEFT)
        text_instrucao.grid(row=1, column=0, columnspan=4, rowspan=3, pady=20, padx=20, sticky=tk.N)

    @property
    def instructions_text(self):
        return """Na planilha de base deve conter as colunas CPF/CNPJ, NOME e TELEFONE seguindo este padrão.\n
Caso mais de um telefone, TELEFONE 1, TELEFONE 2, etc.\n
Para captura de contatos, apenas CPF/CNPJ.\n
Para vcard CPF/CNPJ, CLIENTE e TELEFONE.\n
Para envio de mensagem TELEFONE e CPF/CNPJ ou CLIENTE."""

    def create_menubar(self, parent):
        menubar = tk.Menu(parent, bd=3, relief=tk.RAISED, activebackground="#80B9DC")

        menu_ferramentas = tk.Menu(menubar, tearoff=0, relief=tk.RAISED, activebackground="#026AA9")
        menubar.add_cascade(label="Ferramentas", menu=menu_ferramentas)
        menu_ferramentas.add_command(label="Capturar Contatos", command=lambda: parent.show_frame(parent.CapturarContato))
        menu_ferramentas.add_command(label="Gerar Vcard", command=lambda: parent.show_frame(parent.GerarVcard))
        menu_ferramentas.add_command(label="Enviar Mensagem", command=lambda: parent.show_frame(parent.EnviarMensagem))
        menu_ferramentas.add_separator()
        menu_ferramentas.add_command(label="Instruções", command=lambda: parent.show_frame(parent.HomePage))
        menu_ferramentas.add_command(label="Sair", command=parent.quit)

        menu_driver = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Driver", menu=menu_driver)
        menu_driver.add_command(label="Instalar")

        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ajuda", menu=help_menu)
        help_menu.add_command(label="Sobre", command=U.sobre)

        return menubar