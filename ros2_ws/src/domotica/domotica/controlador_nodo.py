import rclpy
from rclpy.node import Node
from domotica_interfaces.msg import EstadoCasa

class Controlador(Node):
    def __init__(self):
        super().__init__('nodo_controlador')
        self.create_subscription(EstadoCasa, "estado_casa_topic", self.callback, 10)

    def callback(self, msg):
        self.get_logger().info(f"Recibido: {msg}")

def main():
    rclpy.init()
    rclpy.spin(Controlador())
    rclpy.shutdown()
