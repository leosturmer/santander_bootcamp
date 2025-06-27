saldo = 0
total_saques = 3
extrato = ''

menu = '''

    # Sistema Bancário #

    Selecione a opção desejada

    1 - Depositar
    2 - Sacar
    3 - Consultar extrato
    4 - Encerrar 

'''

print(menu)

while True:
    opcao_menu = input('Digite a opção desejada: ')

    if opcao_menu == '1':
        valor_deposito = float(input('Digite o valor que você deseja depositar: R$ '))

        if valor_deposito > 0:
            saldo += valor_deposito
            print(f'Você depositou R${valor_deposito:.2f} \n')
            extrato += f'Depósito: R${valor_deposito:.2f} \n'
        else:
            print('Operação falhou! O valor informado é inválido. \n' )
        

    elif opcao_menu == '2':
        
        if total_saques <= 0:
            print(f'Operação falhou! Limite de saques esgotado. \n')

        else:
            valor_saque = float(input('Digite a quantidade que você deseja sacar: R$ '))
        
            if valor_saque > 500:
                print(f'Operação falhou! Saque máximo: R$ 500,00 \n')

            if valor_saque <= 500:
                if valor_saque < saldo:
                    saldo = saldo - valor_saque
                    total_saques -= 1
                    print(f'Saque de R$ {valor_saque:.2f} realizado com sucesso')
                    print(f'Total de saques disponíveis: {(total_saques)} \n')
    
                    extrato += f'Saque: R$ {valor_saque:.2f} \n'

                elif valor_saque > saldo:
                    print(f'Operação falhou! Você não tem saldo suficiente. \n')
            
        


    elif opcao_menu == '3':
        if saldo == 0:
              print('Não foram realizadas transações. \n')

        else:
            print(f'''
----------------- EXTRATO BANCÁRIO ---------------------
{extrato}

Saldo disponível: R$ {saldo:.2f}

--------------------------------------------------------

''')

    elif opcao_menu == '4':
        break


    else:
        print('Operação inválida! Digite uma opção válida. \n')