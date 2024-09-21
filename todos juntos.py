# Exercicios
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
    
    
    
# 2. Desenvolva um programa em Python que solicite um número inteiro
# entre 1 e 12, em seguida utilizando uma lista/tupla com os meses
# por extenso, faça a exibição do mês correspondente ao número digitado.

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro",  ]
x = 0


x = int(input("Digite um número de 1 a 12 para descobrir qual o mes referente a ele: "))

print(meses[x-1])

# 3. Crie um programa em Python que solicite ao usuário a inserção das notas de 5 alunos em
# uma lista. Para cada nota, atribua um conceito de acordo com a tabela abaixo:

notas = [0]*5
letras = [0]*5

for i in range(len(notas)):
    notas[i] = float(input(f"Qual a nota do {i + 1}º aluno: "))
    if notas[i] >=9:
        letras[i]= "A"
        
    elif notas[i] >= 7 and notas[i]<9:
        letras[i] = "B"
        
    elif notas[i] >= 5 and notas[i] < 7:
        letras[i] = "c"
        
    else:
        letras[i] = "D"
        
for i in range(len(notas)):
    print(f"{i+1}º aluno \nNota: {notas[i]} - Letra: {letras[i]}")


# 4. Elabore um programa em Python que solicite ao usuário que insira 10 números inteiros e os armazene
# em uma lista, em seguida verifique quais números da lista são primos e faça a exibição da quantidade 
# encontrada e de todos os números primos
contagem_primos = 0
primos= []
numeros= []
n = []
todos = []   

def PRIMO(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for i in range(10):
    numeros = int(input(f"Digite o {i+1}º número: "))
    todos.append(numeros)
    if PRIMO(numeros):
        contagem_primos = contagem_primos + 1
        primos.append(numeros)
    else:
        continue


print(f"Todos os numeros: {todos}")
print(f"Números primos: {primos}")
print(f"Quantidade de números primos: {contagem_primos}")





   

