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
