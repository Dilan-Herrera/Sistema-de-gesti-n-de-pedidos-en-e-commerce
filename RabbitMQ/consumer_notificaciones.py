import pika
import json

def enviar_notificacion(ch, method, properties, body):
    notif = json.loads(body)
    print(f"Notificación enviada a {notif['cliente']}: {notif['mensaje']}")

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='notificaciones.fanout', exchange_type='fanout', durable=True)
channel.queue_declare(queue='cola.notificaciones', durable=True)
channel.queue_bind(exchange='notificaciones.fanout', queue='cola.notificaciones')

channel.basic_consume(queue='cola.notificaciones', on_message_callback=enviar_notificacion, auto_ack=True)

print("Esperando notificaciones...")
channel.start_consuming()
