def operacao():
    print("-----Menu-----")
    print("[1] - Somar")
    print("[2] - Subtrair")
    print("[3] - Multiplicar")
    print("[4] - Dividir")
    oper = int(input("Escolha uma opção:"))
    return oper

def verificar_oper (oper):
    if 1 <= oper <= 4:
        return True
    else:
        print("Erro: opção inválida")
        return False

oper = operacao()

if verificar_oper(oper):
    op1 = int(input("Entre com um operando: "))
    op2 = int(input("Entre com um operando: "))
    match oper:
        case 1:
            resultado = op1 + op2
            print("Soma =", resultado)
        case 2:
            resultado = op1 - op2
            print("Subtração =", resultado)
        case 3:
            resultado = op1 * op2
            print("Multiplicação =", resultado)
        case 4:
            resultado = op1 / op2
            print("Divisão =", resultado)
else:
    print("Por favor, escolha uma opção válida.")