def inicio():
    print("Você está em uma floresta escura durante a noite. Você pode seguir por dois caminhos.")
    print("1 - Seguir o caminho à esquerda.")
    print("2 - Seguir o caminho à direita.")
    
    escolha = input("Digite o número da sua escolha: ")
    if escolha == "1":
        caminho_esquerda()
    elif escolha == "2":
        caminho_direita()
    else:
        print("Escolha inválida. Por favor, tente novamente.")
        inicio()

def caminho_esquerda():
    print("\nVocê escolheu o caminho à esquerda e encontra uma cabana abandonada.")
    print("1 - Entrar na cabana.")
    print("2 - Continuar andando pela floresta.")
    
    escolha = input("Digite o número da sua escolha: ")
    if escolha == "1":
        cabana()
    elif escolha == "2":
        floresta()
    else:
        print("Escolha inválida. Por favor, tente novamente.")
        caminho_esquerda()

def caminho_direita():
    print("\nVocê escolheu o caminho à direita e encontra um lago brilhante sob o luar.")
    print("1 - Beber a água do lago.")
    print("2 - Descansar à beira do lago.")
    
    escolha = input("Digite o número da sua escolha: ")
    if escolha == "1":
        lago()
    elif escolha == "2":
        descanso()
    else:
        print("Escolha inválida. Por favor, tente novamente.")
        caminho_direita()

def cabana():
    print("\nVocê entra na cabana e encontra um baú cheio de ouro!")
    print("Parabéns, você encontrou um tesouro escondido e ficou rico!")
    print("Fim da história.")

def floresta():
    print("\nVocê continua andando pela floresta e encontra uma saída.")
    print("Parabéns, você encontrou o caminho de volta para casa em segurança.")
    print("Fim da história.")

def lago():
    print("\nAo beber a água do lago, você sente uma estranha transformação.")
    print("Você se torna parte do lago, guardando-o para sempre.")
    print("Fim da história.")

def descanso():
    print("\nVocê decide descansar e acaba dormindo profundamente.")
    print("Ao acordar, percebe que o dia amanheceu, e encontra facilmente o caminho de volta.")
    print("Fim da história.")

inicio()
