#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import String    
     

class Sensor_Driver_Node(Node):
    def __init__(self):
        super().__init__("sensor_driver") 
        self.robot_name_ ="Sensor"
        self.publisher_ = self.create_publisher(String, "sensor_data", 10)
        self.timer_ = self.create_timer(0.5, self.publish_news)
        self.get_logger().info("Sensor_Driver has been started")
    
    def publish_news(self):
        msg = String()
        msg.data = "Hi, this is " + str(self.robot_name_) + " from robot news station"
        self.publisher_.publish(msg)

    def callback_robot_news(self, msg):
        self.get_logger().info(msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = Sensor_Driver_Node()
    rclpy.spin(node)
    rclpy.shutdown()
     
     
if __name__ == "__main__":
    main()