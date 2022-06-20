import os
import utils as U
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfile

class EnviarMensagem(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)
        self.rowconfigure([0, 1, 2, 3, 4, 5, 6], weight=1, minsize=50)
        self.columnconfigure([0, 1, 2, 3], weight=1, minsize=75)
        self.enviar_nome = tk.BooleanVar(value=True)
        self.planilha_base = tk.StringVar()
        self.anexo = tk.StringVar()

        lbl_titulo = tk.Label(self, text="Enviar Mensagem", font=("bold", 16))
        lbl_titulo.grid(row=0, column=0, columnspan=4, pady=20, sticky=tk.NSEW)

        text_area = ScrolledText(self, height=8, wrap=tk.WORD, font=(11))
        text_area.grid(row=1, column=0, padx=20, columnspan=4, sticky=tk.EW)
        text_area.focus()
        text_area.insert(tk.END, U.texto())

        btn_browse_sw = tk.Button(self, text="Planilha de base", command=self.ask_caminho_base)
        btn_browse_sw.grid(row=2, column=0, padx=20, columnspan=2)

        self.lb_base = tk.Label(self, justify=tk.LEFT, text=self.planilha_base.get())
        self.lb_base.grid(row=2, column=2, columnspan=2, sticky=tk.EW)

        btn_browse_sw = tk.Button(self, text="Incluir anexo", command=self.ask_caminho_anexo)
        btn_browse_sw.grid(row=3, column=0, padx=20, columnspan=2)

        self.lb_anexo = tk.Label(self, justify=tk.LEFT, text=self.anexo.get())
        self.lb_anexo.grid(row=3, column=2, columnspan=2, sticky=tk.EW)

        incluir_nome = tk.Checkbutton(self, text='Mensagem com nome', variable=self.enviar_nome, onvalue=True, offvalue=False, anchor=tk.W)
        incluir_nome.grid(row=4, column=0, columnspan=2, padx=20)

        btn_enviar = tk.Button(self, text="Enviar")
        btn_enviar.grid(row=5, column=1, columnspan=2)

    def ask_caminho_base(self):
        file = askopenfile(mode='r', filetypes=[('Arquivo Excel', '*.xlsx')])
        if file:
            filename = os.path.abspath(file.name)
            self.planilha_base.set(filename)
            formated_filename = filename if len(filename) <= 30 else f"...{filename[-30:]}"
            self.lb_base.config(text=formated_filename)


    def ask_caminho_anexo(self):
        ##TODO
        ## MUDAR O FILETYPES PARA ACEITAR JPG, JPEG, PNG, GIF, PDF.
        file = askopenfile(mode='r', filetypes=[('Arquivo Excel', '*.xlsx')])
        if file:
            filename = os.path.abspath(file.name)
            self.anexo.set(filename)
            formated_filename = filename if len(filename) <= 30 else f"...{filename[-30:]}"
            self.lb_anexo.config(text=formated_filename)

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