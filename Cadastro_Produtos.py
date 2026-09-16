from colorama import Fore, Back, Style, init
init(autoreset=True)

def pergunta(texto_pergunta, cor_pergunta=Fore.CYAN):
    resposta = input(f"{cor_pergunta}{texto_pergunta}{Style.RESET_ALL} ")
    return resposta

def cadastrar_produto():
    print(f"\n{Back.WHITE}{Fore.BLACK} CADASTRO DE PRODUTO {Style.RESET_ALL}\n")
    
    nome = pergunta("Produto:")
    
    while True:
        try:
            preco = float(pergunta("Preço:").replace(",", "."))
            if preco >= 0:
                break
            print(f"{Fore.RED}\n ERRO: Digite um preço válido! \n")
        except ValueError:
            print(f"{Fore.RED}\n ERRO: Digite um valor numérico para o preço! \n")

    while True:
        try:
            quantidade = int(pergunta("Quantidade:"))
            if quantidade >= 0:
                break
            print(f"{Fore.RED}\n ERRO: Digite uma quantidade válida! \n")
        except ValueError:
            print(f"{Fore.RED}\n ERRO: Digite um número inteiro para a quantidade! \n")

    print(f"\n{Fore.GREEN} O produto {nome} foi cadastrado com sucesso! ")

if __name__ == "__main__":
    cadastrar_produto()