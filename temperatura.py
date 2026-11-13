def converter_temperatura():
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    
    opcao = input("Escolha a opção (1 ou 2): ")
    
    if opcao == "1":
        c = float(input("Digite a temperatura em Celsius: "))
        f = (c * 1.8) + 32
        print(f"{c}°C = {f:.2f}°F")
    elif opcao == "2":
        f = float(input("Digite a temperatura em Fahrenheit: "))
        c = (f - 32) / 1.8
        print(f"{f}°F = {c:.2f}°C")
    else:
        print("Opção inválida!")

converter_temperatura()
