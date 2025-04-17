import random
from art import logo

# Funcao geradora de senha digitos
def geradordesenha():
    #Variaveis
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    senha_lista = []

    #Entrada de dados
    print(logo)
    qtde_letras = int(input("Digite o numero de letras:\n"))
    qtde_simbolos = int(input('Digite o numero de caracteres especiais:\n'))
    qtde_numeros = int(input('Digite o numero de numeros:\n'))

    #Processos
    for numero in range(0, qtde_letras):
        senha_lista.append(random.choice(letras))
    
    for numero in range(0, qtde_simbolos):
        senha_lista.append(random.choice(simbolos))

    for numero in range(0, qtde_numeros):
        senha_lista.append(random.choice(numeros))

    
    random.shuffle(senha_lista)
    senha = ''.join(senha_lista)
    print(f'Sua senha é:\n{senha}\n\n')



geradordesenha()