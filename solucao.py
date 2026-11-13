
capacidade = 5 # Capacidade maxima de veiculos = 5
estacionados = 0 # total de veiculos estacionados 


def entrada(): # funcao de entrada de veiculos
    global estacionados  # global = Permite que o valor da variavel criada fora da funçao seja alterada

    if estacionados < capacidade: # condicao se estacionados for menor que a capacidade suportada 
        estacionados = estacionados + 1 # se o veiculo entrar, soma + 1
        return True # retorna verdadeiro = veiculo estacionado 
    else:
        return False # retorna falso = veiculo nao pode entrar por estar cheio 


def saida(): # funcao de saida de veiculos
    global estacionados

    if estacionados > 0: # condicao se estacionados for maior que 0 subtraia - 1
        estacionados = estacionados - 1
        return True
    else:
        return False


def total_vagas(): # funcao para retornar o total de vagas 
    global vagas_livres
    vagas_livres = capacidade - estacionados
    


while True: # laço de repetição para o programa continuar rodando ate o usuario encerrar manualmente 
    vagas_livres = capacidade - estacionados # Assim que executar o programa e conforme for usando e atualizando as informações, apareça para o usuario
    
    print("\n===== ESTACIONAMENTO =====")
    print(f"Veículos estacionados: {estacionados}")
    print(f"Vagas disponíveis: {vagas_livres}")
    
    opc = input("""
    1 - Entrada
    2 - Saída
    3 - Vagas
    4 - Encerrar

    Escolha uma opção: """)

    if opc == "1":
        if entrada():
            print("Entrada autorizada!")
        else:
            print("Estacionamento cheio!")
    elif opc == "2":
        if saida():
            print("Saída autorizada!")
        else:
            print("Estacionamento vazio!")
    elif opc == "3":
        total_vagas()
    elif opc == "4":
        print("Sistema Encerrado!")
        break
    else:
        print("Digite uma opção válida")
