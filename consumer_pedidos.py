import pika
import json

def procesar_pedido(ch, method, properties, body):
    pedido = json.loads(body)
    print(f"Pedido recibido: {pedido}")

    # Enviar pedido a facturación
    ch.basic_publish(
        exchange='facturacion.direct',
        routing_key='factura.generar',
        body=json.dumps(pedido),
        properties=pika.BasicProperties(content_type='application/json')
    )

    # Notificación al cliente
    mensaje = {
        "cliente": pedido['cliente'],
        "mensaje": f"Su pedido {pedido['id']} ha sido procesado."
    }

    channel.basic_publish(
        exchange='notificaciones.fanout',
        routing_key='',
        body=json.dumps(mensaje),
        properties=pika.BasicProperties(content_type='application/json')
    )
    # Log
    log = {
        "evento": "pedido procesado",
        "detalle": f"Pedido {pedido['id']} procesado correctamente."
    }

    channel.basic_publish(
        exchange='logs.topic',
        routing_key='log.pedidos',
        body=json.dumps(log),
        properties=pika.BasicProperties(content_type='application/json')
    )
print("Pedido procesado.")

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='pedidos.direct', exchange_type='direct', durable=True)
channel.exchange_declare(exchange='facturacion.direct', exchange_type='direct', durable=True)
channel.exchange_declare(exchange='notificaciones.fanout', exchange_type='fanout', durable=True)
channel.exchange_declare(exchange='logs.topic', exchange_type='topic', durable=True)

channel.queue_declare(queue='cola.pedidos', durable=True)
channel.queue_bind(exchange='pedidos.direct', queue='cola.pedidos', routing_key='pedido.crear')

channel.basic_consume(queue='cola.pedidos', on_message_callback=procesar_pedido, auto_ack=True)

print("Esperando pedidos...")
channel.start_consuming()