# Definir la lista de productos
productos = [
    {"id": 1, "nombre": "Camiseta", "precio": 19.99, "stock": 50},
    {"id": 2, "nombre": "Zapatos", "precio": 59.99, "stock": 30},
    {"id": 3, "nombre": "Gorra", "precio": 14.99, "stock": 40}
]

# Definir la lista de pedidos
pedidos = [
    {"id_pedido": 101, "cliente": "juan@example.com", "productos": [1, 2], "estado": "En proceso"},
    {"id_pedido": 102, "cliente": "ana@example.com", "productos": [3], "estado": "Pendiente"}
]

# Definir la lista de clientes
clientes = [
    {"nombre": "Juan Pérez", "email": "juan@example.com", "direccion": "Calle 123"},
    {"nombre": "Ana Gómez", "email": "ana@example.com", "direccion": "Avenida 456"}
]

# Agregar un nuevo producto
nuevo_producto = {"id": 4, "nombre": "Pantalón", "precio": 39.99, "stock": 75}
productos.append(nuevo_producto)

# Cambiar el estado del pedido 101 a "Entregado"
for pedido in pedidos:
    if pedido["id_pedido"] == 101:
        pedido["estado"] = "Entregado"

# Buscar pedidos por email
def buscar_pedidos_por_email(email):
    resultado = [pedido for pedido in pedidos if pedido["cliente"] == email]
    return resultado

# Mostrar los datos actualizados
print("\nLista de productos:")
for producto in productos:
    print(f"- {producto['nombre']} (${producto['precio']}) - Stock: {producto['stock']}")

print("\nLista de pedidos actualizada:")
for pedido in pedidos:
    print(f"Pedido {pedido['id_pedido']} - Cliente: {pedido['cliente']} - Estado: {pedido['estado']}")

# Buscar pedidos de un cliente específico
email_cliente = "juan@example.com"
pedidos_cliente = buscar_pedidos_por_email(email_cliente)

print(f"\nPedidos del cliente {email_cliente}:")
for pedido in pedidos_cliente:
    print(f"- Pedido {pedido['id_pedido']} - Estado: {pedido['estado']}")
