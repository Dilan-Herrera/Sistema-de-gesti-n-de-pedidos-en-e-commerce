import pika

mensaje = "Hola, este es un mensaje inicial."

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='pedidos.direct', exchange_type='direct', durable=True)

channel.basic_publish(
    exchange='pedidos.direct',
    routing_key='pedido.crear',
    body=mensaje.encode()
)

print("Mensaje enviado.")
connection.close()
