from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package="domotica",
             executable="agregador_nodo",
             output="screen"),
        Node(package="domotica",
             executable="controlador_nodo",
             output="screen")
    ])
