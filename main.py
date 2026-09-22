import os
from colorama import Fore, Style, init

import Cadastro_Clientes
import Cadastro_Produtos

init(autoreset=True)

def exibir_menu():
    print(Fore.CYAN + "\n" + "=" * 35)
    print(Fore.CYAN + "      SISTEMA EMPRESA+      ")
    print(Fore.CYAN + "=" * 35)
    print("1 - Cadastrar Cliente")
    print("2 - Cadastrar Produto")
    print("0 - Sair")
    print("=" * 35)

def main():
    while True:
        exibir_menu()
        opcao = input(Fore.YELLOW + "Escolha uma opção: " + Style.RESET_ALL).strip()

        if opcao == "1":
            Cadastro_Clientes.cadastrar()
        elif opcao == "2":
            Cadastro_Produtos.cadastrar_produto()
        elif opcao == "0":
            print(Fore.GREEN + "\nSaindo do sistema...")
            break
        else:
            print(Fore.RED + "\nErro: Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()