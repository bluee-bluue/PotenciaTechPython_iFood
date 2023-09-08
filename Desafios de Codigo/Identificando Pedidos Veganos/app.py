def main():
    num_pedidos = int(input())

    pedidos = []
    for i in range(1, num_pedidos + 1):
        prato = input()
        calorias = int(input())
        eh_vegano = input() == "s"
        pedidos.append((i, prato, calorias, eh_vegano))

    for i, pedido in enumerate(pedidos):
        print(f"Pedido {i+1}: {pedido[1]} ({'Vegano' if pedido[3] else 'Nao-vegano'}) - {pedido[2]} calorias")

if __name__ == "__main__":
    main()
