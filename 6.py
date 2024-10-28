import random

def adivinhar_numero():
    numero = random.randint(1,10)
    tentativas = 0
    
    print("Tente adivinhar o número que estou pensando, de um palpite de 1 a 10!")
    
    
    while True:
        palpite = int(input("Qual o seu palpite?"))
        tentativas +=1
        
        if palpite < numero:
            print("Muito baixo")
        elif palpite > numero:
            print("Muito alto")
        else:
            print(f"Você adivinhou o número {numero}")
            break

adivinhar_numero()