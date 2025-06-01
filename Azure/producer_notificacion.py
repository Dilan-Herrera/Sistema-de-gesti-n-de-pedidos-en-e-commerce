import os
from dotenv import load_dotenv
from azure.servicebus import ServiceBusClient, ServiceBusMessage

# Cargar variables desde .env
load_dotenv()

connection_str = os.getenv("AZURE_SERVICE_BUS_CONNECTION_STR")
queue_name = os.getenv("AZURE_QUEUE_NAME")

message = ServiceBusMessage("¡Notificación de prueba desde Azure Service Bus!")

with ServiceBusClient.from_connection_string(connection_str) as client:
    sender = client.get_queue_sender(queue_name)
    with sender:
        sender.send_messages(message)
        print("Mensaje enviado a Azure Service Bus.")
