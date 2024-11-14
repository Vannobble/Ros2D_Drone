#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import String
     
class GUI_Status_Node(Node): 
    def __init__(self):
        super().__init__("GUI_Status") 
        self.subscriber_ = self.create_subscription(String, "detected_img", self.callback_robot_news, 10)
        self.subscriber_ = self.create_subscription(String, "cmd_vel", self.callback_robot_news, 10)
        self.subscriber_ = self.create_subscription(String, "status_pwr", self.callback_robot_news, 10)
        self.subscriber_ = self.create_subscription(String, "sensor_data", self.callback_robot_news, 10)
        self.get_logger().info("GUI_Status has been started")

    def callback_robot_news(self, msg):
        self.get_logger().info(msg.data)
    
def main(args=None):
    rclpy.init(args=args)
    node = GUI_Status_Node()
    rclpy.spin(node)
    rclpy.shutdown()
     
if __name__ == "__main__":
    main()