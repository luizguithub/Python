# 2. Desenvolva um programa em Python que solicite um número inteiro
# entre 1 e 12, em seguida utilizando uma lista/tupla com os meses
# por extenso, faça a exibição do mês correspondente ao número digitado.

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro",  ]
x = 0


x = int(input("Digite um número de 1 a 12 para descobrir qual o mes referente a ele: "))

print(meses[x-1])