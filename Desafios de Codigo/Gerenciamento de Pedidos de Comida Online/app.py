def main():
    n = int(input())

    pedidos = []
    for i in range(1, n + 1):
        pedido = input().split(" ")
        nome = pedido[0]
        valor = float(pedido[1])
        pedidos.append((nome, valor))

    desconto = input()
    if desconto == "10%":
        desconto = 0.1
    elif desconto == "20%":
        desconto = 0.2
    else:
        raise ValueError("Cupom de desconto inválido.")

    valor_total = 0
    for nome, valor in pedidos:
        valor_total += valor * (1 - desconto)

    print("Valor total: {:.2f}".format(valor_total))

if __name__ == "__main__":
    main()

