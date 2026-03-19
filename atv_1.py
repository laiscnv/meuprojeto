numeros = []
num = int(input("Digite o número que deseja:"))
soma = 0
while num != 0:
    numeros.append(num)
    soma += num
    print(soma)
    print(numeros)
    num = int(input("Digite o número que deseja:"))