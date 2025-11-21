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
    
restaurantes = ['Pizza', 'churrasco', 'hamburguer']

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_sub_titulo('Finalizando o programa...')
    sys.exit(0)

def escolher_opcao():
    try:
        return int(input('Escolha uma opção: '))
    except ValueError:
        return None
    
def cadastrar_restaurante():
    exibir_sub_titulo('Cadastro de novos restaurantes')
    nome = input('Digite o nome do restaurante: ')
    restaurantes.append(nome)
    print(f'Restaurante "{nome}" cadastrado com sucesso!')
    voltar_ao_menu()

def listar_restaurantes():
    exibir_sub_titulo('Listando Restaurantes\n')

    for restaurante in restaurantes :
        print('-' + restaurante)

    voltar_ao_menu()

def exibir_sub_titulo(texto):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(texto)
    print()

def voltar_ao_menu():
    input('\nDigite uma tecla para voltar ao menu principal! ')
    main()

def continuar():
    input('\nPressione Enter para continuar...')

def main():
    while True:
        exibir_sub_titulo('')
        exibir_nome_do_programa()
        exibir_opcoes()
        opcao = escolher_opcao()

        if opcao == 1:
            cadastrar_restaurante()
        elif opcao == 2:
            listar_restaurantes()
            continuar()
        elif opcao == 3:
            print('Ativar Restaurante')
            continuar()
        elif opcao == 4:
            finalizar_app()
        else:
            print('Opção inválida')
            continuar()

if __name__ == '__main__':
    main()