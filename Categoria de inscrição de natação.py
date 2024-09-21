# 1. Desenvolva um programa em Python que receba a idade de um nadador
# e em seguida faça a impressão da categoria conforme tabela a seguir:

idade = float (input("Digite a idade do nadador para saber a categoria:"))

if idade >= 5 and idade <= 7:
    print('Categoria Infantil A')
    
elif idade >= 8 and idade <=10:
    print('Categoria infantil B')
    
elif idade >= 11 and idade <=13:
    print('Categoria Juvenil A')

elif idade >= 14 and idade <=17:
    print('Categoria Juvenil B')
    
elif idade >=18:
    print('Categoria Sênior')
    