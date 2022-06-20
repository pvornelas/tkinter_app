import tkinter as tk
from home_view import HomePage
from gerar_vcard_view import GerarVcard
from enviar_mensagem_view import EnviarMensagem
from capturar_contato_view import CapturarContato

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("SEV Araraquara ToolKit")
        self.geometry("640x480")
        self.resizable(True, True)
        self.iconphoto(False, tk.PhotoImage(file="assets/Toolkit (1).png"))

        container = tk.Frame(self, bg="#8AA7A9")
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.HomePage = HomePage
        self.CapturarContato = CapturarContato
        self.GerarVcard = GerarVcard
        self.EnviarMensagem = EnviarMensagem

        for F in {HomePage, CapturarContato, GerarVcard, EnviarMensagem}:
            frame = F(self, container)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        menubar = frame.create_menubar(self)
        self.configure(menu=menubar)
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()