def menu():
    print("----Menu-----")
    print("[1] - Horas para minutos")
    print("[2] - Minutos para horas")
    op = int(input("Entre com uma opção: "))
    return op

def verificar_op (op):
    if op == 1 or op == 2:
        return True
    else:
        print("Erro: opção inválida")
        return False

operacao = menu()
if verificar_op(operacao):
    op1 = int(input("Insira os minutos ou horas que deseja converter: "))

    match operacao:
        case 1:
            horas_minutos = op1 * 60 
            print(horas_minutos, "Minutos")
        case 2:
            minutos_horas = op1 // 60
            print(minutos_horas, "Horas")
else:
    print("Erro: Opção inválida.")