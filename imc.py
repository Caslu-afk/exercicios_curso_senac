# calculadora de ICM - Formula (peso / altura x altura )

# função para calcular o IMC
def calcular(peso, altura):
    calculo = peso / (altura * altura) 
    return calculo

def classificacao(calculo): # função para realizar a verificação do peso
    if calculo < 18: # se o resultado do peso for menor que 18, imprima a mensagem
        print("Baixo peso - Magreza")
    elif calculo >= 18 and calculo <= 25:
        print("Peso normal - Adequado")
    elif calculo > 25 and calculo <= 30:
        print("Sobrepeso - pré-obesidade")
    elif calculo > 30 and calculo <= 35:
        print("Obesidade grau I")
    else:
        print("Procure um médico o mais rápido!!")
    

while True: # laço de repetição para o sistema continuar rodando 
    peso = float(input("Digite o seu peso: "))
    altura = float(input("Digite sua altura: "))

    resultado_final = calcular(peso, altura) # variável nova que recebe o resultado do usuario que esta armazenada na função calcular()

    print(f"Seu IMC é: {resultado_final:.2f}")

    classificacao(resultado_final) # variável de chamada da função de classificação sobre o peso do usuário 

    continuar = input("Deseja realizar outro cálculo? (s/n): ") # variável que recebe o input do cliente para perguntar se deseja continuar 

    if continuar.lower() == "n": # Uma condição para o sistema continuar ou encerrar de acordo com o desejo do cliente
        # .lower(). função do python que serve para transformar todas as letras de uma string em letras minúsculas.
        print("Calculadora encerrada!")
        break # Encerramento do sistema

   

