i = 1
while i <= 100:
    print(i)
    print(i**2)
    i += 1

while True: #true cria um loop infinito
    print("Estou preso no loop infinito!")
    sair = input("Deseja sair? ").lower() #transforma tudo em caixa baixa para não ter problemas de verificação
    if sair == "sim":
        print("Bye!")
        break #break sai completamente do programa
    elif sair == "não":
        continue #manda o código continuar, sai apenas do loop atual