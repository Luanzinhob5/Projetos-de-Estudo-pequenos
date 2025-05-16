import pandas as pd


tabela_zerada = {"Gastos":
        {"Custos Fixos":0,
         "Conforto":0,
         "Metas":0,
         "Prazeres":0,
         "Liberdade Financeira":0,
         "Conhecimento":0,
         },
         "Valor":{},
        }

class EnviarArquivo:
    def __init__(self):
        pass

    def create_csv(self):
        try:
            self.data = pd.read_csv("financas.csv")
        except:
            pd.DataFrame(tabela_zerada).to_csv("financas.csv")

    def add_conteudo(self, categoria, tipo, valor):
        if tipo in self.data[categoria]:
            self.data.loc[self.data['Categoria'] == categoria, 'Valor'] += valor

            