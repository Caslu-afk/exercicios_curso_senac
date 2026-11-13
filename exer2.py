# Desenvolver uma logica que leia os valores de A, B e C de uma equação de segundo grau
# e mostre o valor de Delta

A = int(input("digite o primeiro valor: "))
B = int(input("digite o segundo valor: "))
C = int(input("digite o terceiro valor: "))


def calculo (A, B, C):
    delta = (B ** 2) - (4 * A * C )
    return delta

final = calculo(A, B, C)

if final > 0:
    print("duas raízes reais diferentes.")
elif final == 0:
    print("duas raízes reais iguais.")
elif final < 0:
    print("não existem raízes reais.")
else:
    print("Digite um valor aceitável!")
    

print("O valor de Delta é:", final)

