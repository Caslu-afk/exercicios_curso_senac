'''
contador = 1

while contador <= 5:
    print(contador)
    contador += 1 
'''

tentativas = 0 # variavel recebe valor 0 de tentativas
senha_correta = "python123" # senha para liberar

while tentativas < 3: # enquanto o numero de tentativas for menor que 3 
    senha = input("Digite a senha: ")
    
    if senha == senha_correta: # Se a senha for igual a senha correta
        print("Acesso autorizado!")
        break # para de executar o programa 
    else:
        tentativas += 1 # se a senha não for a correta, adiciona mais 1 chance / se terminar as 3 tentativas o programa encerra e bloqueia o acesso
        print("Acesso negado!")
    
print("Fim do processo") 
