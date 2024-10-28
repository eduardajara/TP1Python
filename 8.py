def verificar_idade():
    idade = int(input("Por favor insira a sua idade: "))
    if idade < 18:
        print("O usuario é menor de idade")
    else:
        print("O usuario é maior de idade")
        
verificar_idade()