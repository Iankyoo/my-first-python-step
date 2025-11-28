import os
import sys

restaurantes = [{'nome':'Reiwa', 'categoria':'japonês', 'ativo': False},
                {'nome':'Taipu in house', 'categoria':'pizza', 'ativo': True}]

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")

def menu():
    print('1 - Cadastrar um novo restaurante')
    print('2 - Listar restaurantes cadastrados')
    print('3 - Ativar restaurante')
    print('4 - Encerrar o programa\n')

def exibir_sub_titulo(texto):
    os.system('cls' if os.name == 'nt' else 'clear')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()

def voltar_ao_menu():
    input('\nDigite uma tecla para voltar ao menu')
    
def escolher():
    try:
        escolha = int(input('Escolha uma das opções:\n'))
        if escolha == 1:
            cadastrar()
        elif escolha == 2:
            listar()
        elif escolha == 3:
            ativar()
        elif escolha == 4:
            encerrar()
        else:
            print('Escolha inválida')
    except ValueError: 
        print('Escolha inválida')
        menu()

def cadastrar():
    exibir_sub_titulo('Cadastro de restaurante')
    nome = input('Digite o nome do restaurante: ')
    categoria = input('Digite a categoria do restaurante: ')
    novo_restaurante = {'nome':nome, 'categoria':categoria, 'ativo': False}
    restaurantes.append(novo_restaurante)
    voltar_ao_menu()

def listar():
    
    exibir_sub_titulo('Lista de restaurantes')
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for r in restaurantes:
        nome = r['nome']
        categoria = r['categoria']
        ativo = 'Ativado' if r['ativo'] else 'Desativado'
        print(f'- {nome.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu()

def ativar():
    exibir_sub_titulo('Restaurantes inativos')
    
    for r in restaurantes:
        if not r['ativo']:
            print(r['nome'])

    nome = input('\nDigite o nome do restaurante que deseja ativar/desativar: ')

    for r in restaurantes:
        if r['nome'].lower() == nome.lower():
            r['ativo'] = not r['ativo']
            print(f"O restaurante {r['nome']} agora está {'ativo' if r['ativo'] else 'inativo'}.")
            break
    else:
        print("Restaurante não encontrado.")

    voltar_ao_menu()

def encerrar():
    exibir_sub_titulo('Encerrando a aplicação')
    sys.exit(0)
    
def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        exibir_nome_do_programa()
        menu()
        escolher()

if __name__ == '__main__':
    main()    