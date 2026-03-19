while True:
    salario = float(input("Qual é o seu salário: "))
    cargo = input("Qual é o seu cargo: ").lower()

    if cargo == 'júnior':
        novo_salario = salario * 1.1 + 200.00 if salario == 1000.00 else 0
    elif cargo == 'pleno':
        novo_salario = salario * 1.15
    elif cargo == 'sênior':
        num_filhos = int(input("Quantos filhos você tem? "))
        beneficio_filhos = 500 * num_filhos
        novo_salario = salario * 1.20 + beneficio_filhos
    else:
        print("Cargo não identificado")

    print("Seu novo salário é: R$" ,novo_salario)

    pergunta = input("Deseja buscar novas informações?").lower()
    if pergunta == 'sim':
        continue
    elif pergunta == 'não':
        print("Fim")
        break
    else:
        print("Resposta inválida")
        break


    
