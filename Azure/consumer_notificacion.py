import os
from dotenv import load_dotenv
from azure.servicebus import ServiceBusClient

# Cargar variables desde .env
load_dotenv()

connection_str = os.getenv("AZURE_SERVICE_BUS_CONNECTION_STR")
queue_name = os.getenv("AZURE_QUEUE_NAME")

with ServiceBusClient.from_connection_string(connection_str) as client:
    receiver = client.get_queue_receiver(queue_name)
    with receiver:
        print("Esperando mensajes...")
        for msg in receiver:
            print(f"Mensaje recibido: {str(msg)}")
            receiver.complete_message(msg)