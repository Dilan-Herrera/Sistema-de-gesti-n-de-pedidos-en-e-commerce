# Sistema de Pedidos con RabbitMQ

Este proyecto simula el procesamiento de pedidos en una tienda en línea usando RabbitMQ. El sistema separa responsabilidades entre módulos de pedidos, facturación, notificaciones y auditoría.

## Estructura

- `producer_pedido.py`: Simula el envío de un pedido nuevo.
- `consumer_pedidos.py`: Procesa el pedido y comunica con otros módulos.
- `consumer_facturacion.py`: Recibe pedidos para facturación.
- `consumer_notificaciones.py`: Recibe notificaciones para enviar al cliente.
- `consumer_logs.py`: Registra eventos del sistema.

## Requisitos

- Python 3.8+
- RabbitMQ local (puerto 5672)
- Instalar dependencias:

```bash
pip install -r requirements.txt
