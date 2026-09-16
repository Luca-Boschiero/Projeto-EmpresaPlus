#Dupla A
import os # para criar arquivos no computador
from colorama import Fore, Style, init # colorama

init()  # inicia o colorama

arquivo = "clientes.txt"  # arquivo de texto dos clientes

# função de aviso
def warn(texto):
    print(Fore.RED + texto + Style.RESET_ALL)

# função de sucesso
def sucess(texto):
    print(Fore.GREEN + texto + Style.RESET_ALL)






# funções de validação
# função para validar o e-mail
def validar_email(email_bruto):
    email = email_bruto.strip().lower()

    if "@" in email and "." in email.split("@")[-1]: # se tiver @ e após tiver um . valida o email
        return email
    else:
        return None 

# função para validar o telefone
def validar_telefone(telefone_bruto):
    # mantém apenas os números (joga fora espaços traços e parenteses)
    # verifica se todos os caracteres são números
    telefone = "".join([c for c in telefone_bruto if c.isdigit()])
    
    # se o tamanho for 9, 10 ou 11, o telefone está correto e é retornado
    if len(telefone) in [9, 10, 11]:
        return telefone
    
    # se não tiver o tamanho certo, retorna None (inválido)
    return None