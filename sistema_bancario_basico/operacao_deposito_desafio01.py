import time

saq_de_dinheiro = 0
per_saq_dia = 0
valor_de_saque = 0
valor_deposito = 0
while True:
    print("""
    +++++++++++++++++++++++++++++++
    +         BEM-VINDO           +
    +            AO               +
    +      SISTEMA BANCÁRIO       +
    +++++++++++++++++++++++++++++++
      """
    )
    print("1 - DEPOSITAR | 2 - SACAR | 3 - EXTRATO | 4 - SAIR")
    opc_de_operation = input('Digite uma opção do menu: ')
    try:
        if(int(opc_de_operation) == 1):
            valor_deposito = input('Quanto deseja depositar? R$ ')
            valor_deposito = float(valor_deposito)
        elif(int(opc_de_operation) == 2):
            print(f'Valor disponível ({valor_deposito})')
            print('Você só pode sacar até R$ 500,00 reais')
            if(per_saq_dia > 3):
                print('Você atingiu sua cota de saques diária:')
                print('Sistema sairá automaticamente em 3s')
                time.sleep(3)
                break
            saq_de_dinheiro = input('Você quer sacar quanto da sua conta? R$ ')
            saq_de_dinheiro = float(saq_de_dinheiro)
            if(valor_deposito == 0):
                print('Você não tem sando disponível. Deposite primeiro.')
                pass
            elif(saq_de_dinheiro <=  500):
                valor_de_saque += saq_de_dinheiro
                valor_deposito -= saq_de_dinheiro
            elif(saq_de_dinheiro > 500):
                print('Você tem tou sacar um valor maior que R$ 500,00')
                pass
        elif(int(opc_de_operation) == 3):
            while True:
                print(f"""
                    +++++++++++++++++++++++++++++++
        
                    +           EXTRATO           +
                
                    VALOR ATUAL: R$ {valor_deposito}
                    VALOR SACADO: R$ {valor_de_saque} 
                    
                    +++++++++++++++++++++++++++++++
                    """)
                opc_extrato = input("Digite [sair] para siar do extrato. ").lower()
                if(opc_extrato == 'sair'):
                    break
        elif(int(opc_de_operation) == 4):
            print('Sistema sairá automaticamente em 3s')
            time.sleep(3)
            break
    except:
        pass
    
    per_saq_dia +=1
print("""
      OBRIGADO POR USAR O SISTEMA
      VOLTE SEMPRE!!!
      """)
