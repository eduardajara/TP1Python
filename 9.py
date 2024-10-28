def calc_desconto(val_compra):
    if val_compra > 500:
        desc = 0.25
    elif val_compra > 200:
        desc = 0.15
    elif val_compra > 100:
        desc = 0.10
    else:
        desc = 0.0
    val_final = val_compra * (1 - desc)
    return val_final, desc * 100

val_compra = float(input("Digite o valor total da compra: R$ "))

val_final, per_desconto = calc_desconto(val_compra)

print(f"Valor inicial: R$ {val_compra:.2f}")
print(f"Desconto aplicado: {per_desconto:.0f}%")
print(f"Valor com desconto: R$ {val_final:.2f}")
