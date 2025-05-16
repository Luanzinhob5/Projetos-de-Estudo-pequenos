import customtkinter as ctk
from tratamento_arquivo import EnviarArquivo

class Interface:
    def __init__(self, envio):
        self.envio = envio 
        #Configuracao da cor da aparencia
        ctk.set_appearance_mode("dark")

        #janela do app principal
        self.app = ctk.CTk()
        self.app.title("Automatizador de Financas")
        self.app.geometry("400x500")
        self.valor()
        self.gasto()
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


    #Funcao do gasto
    def gasto(self):
        #label do gasto
        self.label_nome_gasto = ctk.CTkLabel(self.app, text="Nome do gasto:")
        self.label_nome_gasto.place(x=130,y=120)
        #Entry do gasto
        self.entry_nome_gasto = ctk.CTkEntry(self.app)
        self.entry_nome_gasto.place(x=130,y=150)
    #Funcao do Scrollable Frame
    def scrollableframe(self):
        #Criacao do scrollableframe
        self.frame_categoria = ctk.CTkScrollableFrame(self.app, width=150, height=150, label_text="Enviar para Categoria")
        self.frame_categoria.place(x=115,y=200)

        #Button do Scrollable Frame
        self.button_entrada_de_saldo = ctk.CTkButton(self.frame_categoria, text="Ganho").pack(pady=5)
        self.button_custos_fixos = ctk.CTkButton(self.frame_categoria, text="Custos Fixos").pack(pady=5)
        self.button_conforto = ctk.CTkButton(self.frame_categoria, text="Conforto").pack(pady=5)
        self.button_prazeres = ctk.CTkButton(self.frame_categoria, text="Prazeres").pack(pady=5)
        self.button_metas = ctk.CTkButton(self.frame_categoria, text="Metas").pack(pady=5)
        self.button_conhecimento = ctk.CTkButton(self.frame_categoria, text="Conhecimento").pack(pady=5)
        self.button_liberdade_financeira = ctk.CTkButton(self.frame_categoria, text="Liberdade Financeira",command=self.envio).pack(pady=5)



        