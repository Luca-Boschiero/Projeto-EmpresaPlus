from colorama import Fore, Style, init
init(autoreset=True)

def pergunta(texto_pergunta, cor_pergunta=Fore.CYAN):
    resposta = input(f"{cor_pergunta}{texto_pergunta}{Style.RESET_ALL} ")
    return resposta
