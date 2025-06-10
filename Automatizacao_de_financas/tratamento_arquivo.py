import pandas as pd
from openpyxl.workbook import Workbook

tabela_zerada = {
    "Gastos":["Ganhos","","Essenciais","Casa","Prazeres","Investimentos","Conhecimento","Bet"],
    "Valor":[0,"",0, 0, 0, 0, 0, 0]
    }

class TratarArquivo:
    def __init__(self):
        try:
            self.data = pd.read_excel("financas_maio.xlsx")
        except:
            self.data = pd.DataFrame(tabela_zerada)
            self.data.to_excel("financas_maio.xlsx", index=False)

    def add_conteudo(self, categoria, valor):
        if int(valor) <= 0:
            print("ola")
        elif categoria in self.data["Gastos"].values:
           self.data.loc[self.data["Gastos"] == categoria, 'Valor'] += int(valor)
           
        self.data.to_excel("financas_maio.xlsx", index=False)

