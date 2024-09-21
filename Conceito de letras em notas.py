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