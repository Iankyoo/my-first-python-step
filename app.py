import os
import sys

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Finalizando app')
    sys.exit(0)

def escolher_opcao():
    try:
        return int(input('Escolha uma opção: '))
    except ValueError:
        return None

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        exibir_nome_do_programa()
        exibir_opcoes()
        opcao = escolher_opcao()

        if opcao == 1:
            print('Cadastrar Restaurante')
            input('\nPressione Enter para continuar...')
        elif opcao == 2:
            print('Listar Restaurantes')
            input('\nPressione Enter para continuar...')
        elif opcao == 3:
            print('Ativar Restaurante')
            input('\nPressione Enter para continuar...')
        elif opcao == 4:
            finalizar_app()
        else:
            print('Opção inválida')
            input('\nPressione Enter para continuar...')

if __name__ == '__main__':
    main()