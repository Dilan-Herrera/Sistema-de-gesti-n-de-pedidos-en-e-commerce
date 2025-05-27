import pika
import json

def generar_factura(ch, method, properties, body):
    pedido = json.loads(body)
    print(f"Generando factura para el pedido: {pedido['id']} de {pedido['cliente']}")

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='facturacion.direct', exchange_type='direct', durable=True)
channel.queue_declare(queue='cola.facturacion', durable=True)
channel.queue_bind(exchange='facturacion.direct', queue='cola.facturacion', routing_key='factura.generar')

channel.basic_consume(queue='cola.facturacion', on_message_callback=generar_factura, auto_ack=True)

print("Esperando pedidos para facturación...")
channel.start_consuming()
