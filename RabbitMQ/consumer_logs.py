import pika
import json

def registrar_log(ch, method, properties, body):
    log = json.loads(body)
    print(f"[LOG] Evento: {log['evento']} - {log['detalle']}")

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs.topic', exchange_type='topic', durable=True)
channel.queue_declare(queue='cola.logs', durable=True)
channel.queue_bind(exchange='logs.topic', queue='cola.logs', routing_key='log.#')

channel.basic_consume(queue='cola.logs', on_message_callback=registrar_log, auto_ack=True)

print("Esperando logs...")
channel.start_consuming()
