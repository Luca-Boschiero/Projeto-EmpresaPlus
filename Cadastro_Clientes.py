# Dupla A
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

    if "@" not in email:
        return None

    partes = email.split("@")

    # garante que tem exatamente um @ e que o nome antes dele não está vazio
    if len(partes) != 2 or not partes[0]:
        return None

    dominio = partes[1]

    # garante que o domínio tem ponto e não começa nem termina com ponto (ex: evita "@.", "@gmail.", ".com")
    if "." not in dominio or dominio.startswith(".") or dominio.endswith("."):
        return None

    # garante que existem caracteres validos entre os pontos do domínio
    partes_dominio = dominio.split(".")
    if any(not parte for parte in partes_dominio):
        return None

    return email

# função para validar o telefone
def validar_telefone(telefone_bruto):
    # mantém apenas os números (joga fora espaços traços e parenteses)
    # verifica se todos os caracteres são números
    telefone = "".join([c for c in telefone_bruto if c.isdigit()])
    
    # se o tamanho for 9, 10 ou 11, o telefone está correto e é retornado
    if len(telefone) in [9, 10, 11]:
        return telefone
    
    # se não tiver o tamanho certo retorna none (inválido)
    return None


# funções de formatação para lista
# para formatar o telefone
def formatar_telefone(telefone):
    telefone = str(telefone)
    if len(telefone) == 11:
        return f"({telefone[0:2]}) {telefone[2:7]}-{telefone[7:]}"

    elif len(telefone) == 10:
        return f"({telefone[0:2]}) {telefone[2:6]}-{telefone[6:]}"
    
    elif len(telefone) == 9:
        return f"{telefone[0:5]}-{telefone[5:]}"

    else:
        return telefone


def cadastrar():
    # loop do nome
    while True:
        nome = input("Digite o nome do cliente: ").strip().title()
        if nome:
            break
        warn("Erro: O nome não pode ficar vazio.")

    # loop do e-mail
    while True:
        entrada = input("Digite o e-mail do cliente: ")
        email = validar_email(entrada)

        if not email:
            warn("Erro: Formato de e-mail inválido. Tente novamente.")
            continue

        # verifica duplicidade de e-mail no arquivo
        duplicado = False
        if os.path.exists(arquivo):
            with open(arquivo, "r", encoding="utf-8") as file:
                for linha in file:
                    partes = [p.strip().lower() for p in linha.strip().split(";")]
                    if len(partes) > 1 and partes[1] == email:
                        duplicado = True
                        break

        if duplicado:
            warn("Erro: Este e-mail já pertence a outro cliente cadastrado.")
        else:
            break

    # loop do telefone
    while True:
        entrada_tel = input("Digite o telefone do cliente: ")
        telefone = validar_telefone(entrada_tel)

        if not telefone:
            warn("Erro: O telefone precisa ter 9, 10 ou 11 dígitos.")
            continue

        # verifica duplicidade de telefone no arquivo
        duplicado = False
        if os.path.exists(arquivo):
            with open(arquivo, "r", encoding="utf-8") as file:
                for linha in file:
                    partes = [p.strip() for p in linha.strip().split(";")]
                    if len(partes) > 2:
                        tel_existente = "".join(c for c in partes[2] if c.isdigit())
                        if tel_existente == telefone:
                            duplicado = True
                            break

        if duplicado:
            warn("Erro: Este telefone já pertence a outro cliente cadastrado.")
        else:
            break

    # grava o novo cliente no arquivo
    with open(arquivo, "a", encoding="utf-8") as file:
        file.write(f"{nome};{email};{telefone}\n")

    sucess("Cliente cadastrado com sucesso!")

def listar():
    try:
        with open(arquivo, "r", encoding="utf-8") as file:
            linhas = file.readlines()
    except FileNotFoundError:
        warn("O arquivo de clientes ainda não existe.")
        return

    # remove linhas vazias da contagem
    linhas_validas = [l for l in linhas if l.strip()]

    if not linhas_validas:
        warn("Nenhum cliente cadastrado.")
        return

    print(Fore.CYAN + "\n" + "=" * 60)
    print(Fore.CYAN + "Clientes Cadastrados")
    print(Fore.CYAN + "=" * 60 + Style.RESET_ALL)

    print(f"{'Nome':<20} {'E-mail':<25} {'Telefone'}")
    print("-" * 60)

    for linha in linhas:
        linha_limpa = linha.strip()
        if linha_limpa:
            partes = [p.strip() for p in linha_limpa.split(";")]
            
            nome = partes[0] if len(partes) > 0 else "-"
            email = partes[1] if len(partes) > 1 else "-"
            telefone = partes[2] if len(partes) > 2 else "-"

            print(f"{nome:<20} {email:<25} {formatar_telefone(telefone)}")


def alterar():
    try:
        with open(arquivo, "r", encoding="utf-8") as file:
            linhas = file.readlines()
    except FileNotFoundError:
        warn("O arquivo de clientes ainda não existe.")
        return

    nome_busca = input("Digite o nome do cliente que quer alterar: ").strip().lower()

    if not nome_busca:
        warn("O nome não pode ser vazio.")
        return

    # 1. Filtra as correspondências pelo nome
    coincidencias = []
    for linha in linhas:
        linha_limpa = linha.strip()
        if linha_limpa:
            partes = [p.strip() for p in linha_limpa.split(";")]
            if partes[0].lower() == nome_busca:
                coincidencias.append(partes)

    if len(coincidencias) == 0:
        warn("Cliente não encontrado.")
        return

    email_busca = None
    telefone_busca = None

    # se houver nomes iguais pede o email
    if len(coincidencias) > 1:
        print(f"Foram encontrados {len(coincidencias)} clientes com o nome '{nome_busca}'.")
        email_busca = input("Digite o e-mail do cliente que deseja alterar: ").strip().lower()

        # checa quantos clientes realmente possuem esse nome e email
        coincidencias_email = [
            c for c in coincidencias 
            if len(c) > 1 and c[1].lower() == email_busca
        ]

        # cancela caso não encontre um cliente com o nome e mail
        if len(coincidencias_email) == 0:
            warn("Nenhum cliente com esse nome possui o e-mail informado.")
            return

        # pede o telefone se ainda houver nome email duplicados
        if len(coincidencias_email) > 1:
            print("Ainda existem registros com o mesmo e-mail.")
            tel_entrada = input("Digite apenas os números do telefone: ").strip()
            telefone_busca = "".join(char for char in tel_entrada if char.isdigit())

            # Checa se o telefone digitado bate com algum dos registros
            coincidencias_tel = [
                c for c in coincidencias_email
                if len(c) > 2 and "".join(char for char in c[2] if char.isdigit()) == telefone_busca
            ]

            if len(coincidencias_tel) == 0:
                warn("Nenhum cliente com esse nome e e-mail possui esse telefone.")
                return

    # pede os novos dados do cliente
    print("\n--- Digite os novos dados ---")
    
    # novo Nome
    while True:
        novo_nome = input("Digite o novo nome do cliente: ").strip().title()
        if novo_nome:
            break
        warn("Erro: O nome não pode ficar vazio.")

    # novo email
    while True:
        entrada_email = input("Digite o novo e-mail do cliente: ")
        novo_email = validar_email(entrada_email)
        if novo_email:
            break
        warn("Erro: Formato de e-mail inválido. Tente novamente.")

    # novo Telefone
    while True:
        entrada_tel = input("Digite o novo telefone do cliente: ")
        novo_telefone = validar_telefone(entrada_tel)
        if novo_telefone:
            break
        warn("Erro: O telefone precisa ter 9, 10 ou 11 dígitos.")

    # processa a alteração no arquivo
    novas_linhas = []
    alterado = False

    for linha in linhas:
        linha_limpa = linha.strip()
        if not linha_limpa:
            continue

        partes = [p.strip() for p in linha_limpa.split(";")]
        nome_linha = partes[0].lower()
        email_linha = partes[1].lower() if len(partes) > 1 else ""
        
        telefone_bruto = partes[2] if len(partes) > 2 else ""
        telefone_linha = "".join(char for char in telefone_bruto if char.isdigit())

        # verifica se é a linha correta para alterar
        if not alterado and nome_linha == nome_busca:
            deve_alterar = False

            if telefone_busca:
                if email_linha == email_busca and telefone_linha == telefone_busca:
                    deve_alterar = True
            elif email_busca:
                if email_linha == email_busca:
                    deve_alterar = True
            else:
                deve_alterar = True

            if deve_alterar:
                # Substitui a linha antiga pelos novos dados
                novas_linhas.append(f"{novo_nome};{novo_email};{novo_telefone}\n")
                alterado = True
                continue

        novas_linhas.append(linha)

    # sobreescreve o arquivo
    if alterado:
        with open(arquivo, "w", encoding="utf-8") as file:
            file.writelines(novas_linhas)
        sucess("Dados do cliente alterados com sucesso!")
    else:
        warn("Nenhum cliente foi alterado (dados de confirmação errados).")


def deletar():
    try:
        with open(arquivo, "r", encoding="utf-8") as file:
            linhas = file.readlines()
    except FileNotFoundError:
        warn("O arquivo de clientes ainda não existe.")
        return
    
    nome_busca = input("Digite o nome do cliente que quer apagar: ").strip().lower()

    if not nome_busca:
        warn("O nome não pode ser vazio.")
        return

    # filtra as correspondencias pelo nome
    coincidencias = []
    for linha in linhas:
        linha_limpa = linha.strip()
        if linha_limpa:
            partes = [p.strip() for p in linha_limpa.split(";")]
            if partes[0].lower() == nome_busca:
                coincidencias.append(partes)

    if len(coincidencias) == 0:
        warn("Cliente não encontrado.")
        return

    email_busca = None
    telefone_busca = None

    # se houver nomes iguais pede o e-mail
    if len(coincidencias) > 1:
        print(f"Foram encontrados {len(coincidencias)} clientes com o nome '{nome_busca}'.")
        email_busca = input("Digite o e-mail do cliente que deseja apagar: ").strip().lower()

        coincidencias_email = [
            c for c in coincidencias 
            if len(c) > 1 and c[1].lower() == email_busca
        ]

        if len(coincidencias_email) == 0:
            warn("Nenhum cliente com esse nome possui o e-mail informado.")
            return

        # se ainda houver duplicados pede o telefone
        if len(coincidencias_email) > 1:
            print("Ainda existem registros com o mesmo e-mail.")
            tel_entrada = input("Digite apenas os números do telefone: ").strip()
            telefone_busca = "".join(char for char in tel_entrada if char.isdigit())

            coincidencias_tel = [
                c for c in coincidencias_email
                if len(c) > 2 and "".join(char for char in c[2] if char.isdigit()) == telefone_busca
            ]

            if len(coincidencias_tel) == 0:
                warn("Nenhum cliente com esse nome e e-mail possui esse telefone.")
                return

    # processa a remoção no arquivo
    novas_linhas = []
    quantidade_apagados = 0

    for linha in linhas:
        linha_limpa = linha.strip()
        if not linha_limpa:
            continue

        partes = [p.strip() for p in linha_limpa.split(";")]
        nome_linha = partes[0].lower()
        email_linha = partes[1].lower() if len(partes) > 1 else ""
        
        telefone_bruto = partes[2] if len(partes) > 2 else ""
        telefone_linha = "".join(char for char in telefone_bruto if char.isdigit())

        # apaga o registro correspondente aos critérios
        if nome_linha == nome_busca:
            if telefone_busca:
                if email_linha == email_busca and telefone_linha == telefone_busca:
                    quantidade_apagados += 1
                    continue
            elif email_busca:
                if email_linha == email_busca:
                    quantidade_apagados += 1
                    continue
            else:
                quantidade_apagados += 1
                continue

        novas_linhas.append(linha)

    # sobreescreve o arquivo
    if quantidade_apagados > 0:
        with open(arquivo, "w", encoding="utf-8") as file:
            file.writelines(novas_linhas)
        sucess(f"{quantidade_apagados} clientes excluídos com sucesso!")
    else:
        warn("Nenhum cliente foi excluído (dados de confirmação errados).")