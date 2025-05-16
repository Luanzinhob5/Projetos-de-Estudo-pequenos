from interface import Interface
from tratamento_arquivo import EnviarArquivo

enviar_arquivo = EnviarArquivo()
envio = enviar_arquivo.create_csv()
aplicativo = Interface(envio=envio)



