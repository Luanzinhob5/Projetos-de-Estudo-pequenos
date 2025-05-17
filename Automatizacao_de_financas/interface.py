import customtkinter as ctk
from tratamento_arquivo import TratarArquivo

class Interface:
    def __init__(self):
        self.enviar_arquivo = TratarArquivo()
        #Configuracao da cor da aparencia
        ctk.set_appearance_mode("dark")

        #janela do app principal
        self.app = ctk.CTk()
        self.app.title("Automatizador de Financas")
        self.app.geometry("400x500")
        self.valor()
        self.scrollableframe()
        self.app.mainloop()

    #Funcao do Valor
    def valor(self):
        #Label do valor
        self.label_valor = ctk.CTkLabel(self.app, text="Valor:")
        self.label_valor.place(x=130,y=60)
        #Entry do valor
        self.entry_valor = ctk.CTkEntry(self.app)
        self.entry_valor.place(x=130,y=90)
        
    #Funcao do Scrollable Frame
    def scrollableframe(self):
        #Criacao do scrollableframe
        self.frame_categoria = ctk.CTkScrollableFrame(self.app, width=150, height=150, label_text="Enviar para Categoria")
        self.frame_categoria.place(x=115,y=200)

        #Button do Scrollable Frame
        self.button_ganhos= ctk.CTkButton(self.frame_categoria, text="Ganhos",command=self.entrada_ganhos).pack(pady=5)
        self.button_essenciais = ctk.CTkButton(self.frame_categoria, text="Essenciais",command=self.entrada_essenciais).pack(pady=5)
        self.button_casa = ctk.CTkButton(self.frame_categoria, text="Casa",command=self.entrada_casa).pack(pady=5)
        self.button_prazeres = ctk.CTkButton(self.frame_categoria, text="Prazeres",command=self.entrada_prazeres).pack(pady=5)
        self.button_investimento = ctk.CTkButton(self.frame_categoria, text="Investimento",command=self.entrada_investimento).pack(pady=5)
        self.button_conhecimento = ctk.CTkButton(self.frame_categoria, text="Conhecimento",command=self.entrada_conhecimento).pack(pady=5)
        self.button_bet = ctk.CTkButton(self.frame_categoria, text="Bet",command=self.entrada_bet).pack(pady=5)

    def entrada_ganhos(self):
            self.valor = self.entry_valor.get()
            categoria = "Ganhos"
            self.enviar_arquivo.add_conteudo(categoria,self.valor)

    def entrada_essenciais(self):
            self.valor = self.entry_valor.get()
            categoria = "Essenciais"
            self.enviar_arquivo.add_conteudo(categoria,self.valor)

    def entrada_casa(self):
            self.valor = self.entry_valor.get()
            categoria = "Casa"
            self.enviar_arquivo.add_conteudo(categoria,self.valor)

    def entrada_prazeres(self):
            self.valor = self.entry_valor.get()
            categoria = "Prazeres"
            self.enviar_arquivo.add_conteudo(categoria,self.valor)

    def entrada_investimento(self):
            self.valor = self.entry_valor.get()
            categoria = "Investimento"
            self.enviar_arquivo.add_conteudo(categoria,self.valor)
        
    def entrada_conhecimento(self):
            self.valor = self.entry_valor.get()
            categoria = "Conhecimento"
            self.enviar_arquivo.add_conteudo(categoria,self.valor)

    def entrada_bet(self):
            self.valor = self.entry_valor.get()
            categoria = "Bet"
            self.enviar_arquivo.add_conteudo(categoria,self.valor)


        