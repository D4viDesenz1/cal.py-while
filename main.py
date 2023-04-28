resposta = input("você quer conhece a minha calculadora ? (s/n)")
while resposta != "s" and resposta != "n":
    reposta = input("tem que ser (s/n)")

if resposta == "n":
    print("ent vai tomar no seu cu, otário")
else:
    while True:
        opcao = input(" o que vc quer fazer? soma, subtração, divisão ou multiplicação? ")
        while opcao != "soma" and opcao != "subtração" and opcao != "divisão" and opcao != "multiplicação":
            opcao = input("tem que ser soma, subtração, divisão ou multiplicação: ")

        num1 = input("diga o primeiro número: ")
        while not num1.isnumeric():
            num1 = input("tem que ser inteiro: ")
        num1 = int(num1)

        num2 = input("diga o segundo número: ")
        while not num2.isnumeric():
            num2 = input("tem que ser inteiro: ")
        num2 = int(num2)

        if opcao == "soma":
            resultado = num1 + num2
        elif opcao == "divisão":
            resultado = num1 / num2
        elif opcao == "multiplicação":
            resultado = num1 * num2
        else:
            resultado = num1 - num2
        print(f"A {opcao} entre {num1} e {num2} é {resultado}")

        novamente = input("você quer fazer mais alguma conta? (s/n)")
        while novamente != "s" and novamente != "n":
            novamente = input("você quer fazer mais alguma conta? (s/n)")

        if novamente == "s":
            continue
        else:
            break

