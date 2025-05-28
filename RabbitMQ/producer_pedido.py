import pika
import json

pedido = {
    "id": "PED001",
    "cliente": "Juan Pérez"
}

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='pedidos.direct', exchange_type='direct', durable=True)

channel.basic_publish(
    exchange='pedidos.direct',
    routing_key='pedido.crear',
    body=json.dumps(pedido),
    properties=pika.BasicProperties(content_type='application/json')
)

print("Pedido enviado.")
connection.close()
