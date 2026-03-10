import random


#FUNÇÃO DE VALIDAÇÃO DE ENTRADA DO USUÁRIO.
def get_input():
    while True:
        try:
            numero_usuario = int(input("Digite um número entre 1 e 10: "))
            if 1 <= numero_usuario <= 10:
                return numero_usuario
            else:
                print("Por favor, digite um número entre 1 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

#FUNÇÃO DE VERIFICAÇÃO DO NÚMERO DIGITADO PELO USUÁRIO COM O NÚMERO SORTEADO.
def check_numbers(usuario, sorteio):
        if usuario == sorteio:
            print("Parabéns, você acertou o número!")
            return True
    
        elif usuario > sorteio:
            print("O número sorteado é menor do que o número digitado.")
            return False
        
        else:
            print("O número sorteado é maior do que o número digitado.")
            return False
        
        
numero_sorteio = random.randint(1,10)


for i in range(3):
    numero_usuario = get_input()
    if check_numbers(usuario=numero_usuario, sorteio=numero_sorteio):
        break



else:
       print("Suas tentativas acabaram!")
