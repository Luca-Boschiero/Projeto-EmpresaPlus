from colorama import Fore, Back, Style, init
init(autoreset=True)

def pergunta(texto_pergunta, cor_pergunta=Fore.CYAN):
    resposta = input(f"{cor_pergunta}{texto_pergunta}{Style.RESET_ALL} ")
    return resposta

def erro(mensagem):
    print(f"{Fore.RED}\n ERRO: {mensagem} \n")

def sucesso(mensagem):
    print(f"{Fore.GREEN}\n {mensagem} \n")

def cadastrar_produto():
    print(f"\n{Back.WHITE}{Fore.BLACK} CADASTRO DE PRODUTO {Style.RESET_ALL}\n")
    
    nome = pergunta("Produto:")
    
    while True:
        try:
            preco = float(pergunta("Preço:").replace(",", "."))
            if preco >= 0:
                break
            erro("Digite um preço válido!")
        except ValueError:
            erro("Digite um valor numérico para o preço!")

    while True:
        try:
            quantidade = int(pergunta("Quantidade:"))
            if quantidade >= 0:
                break
            erro("Digite uma quantidade válida!")
        except ValueError:
            erro("Digite um número inteiro para a quantidade!")

    sucesso(f"O produto {nome} foi cadastrado com sucesso!")

if __name__ == "__main__":
    cadastrar_produto()
