import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
from domotica_interfaces.msg import Accesos, Ambiente, EstadoCasa

class Agregador(Node):
    def __init__(self):
        super().__init__('nodo_agregador')
        self.create_subscription(Ambiente, "ambiente_topic", self.callback, 10)
        self.create_subscription(Bool, "presencia_topic", self.callback, 10)
        self.create_subscription(Accesos, "accesos_topic", self.callback, 10)

        self.pub = self.create_publisher(EstadoCasa, "estado_casa_topic", 10)

    def callback(self, msg):
        self.get_logger().info(f"Recibido: {msg}")

def main():
    rclpy.init()
    rclpy.spin(Agregador())
    rclpy.shutdown()
