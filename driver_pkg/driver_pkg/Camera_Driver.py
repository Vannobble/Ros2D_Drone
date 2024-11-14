#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import String    
     

class Camera_Driver_Node(Node):
    def __init__(self):
        super().__init__("camera_driver") 

        self.robot_name_ ="Camera"
        self.image_publisher = self.create_publisher(String, "image_raw", 10)
        self.timer_ = self.create_timer(0.5, self.publish_news)
        self.get_logger().info("Camera_Driver has been started")
    
    def publish_news(self):
        msg = String()
        msg.data = "Hi, this is " + str(self.robot_name_) + " from robot news station"
        self.image_publisher.publish(msg)

    def callback_robot_news(self, msg):
        self.get_logger().info(msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = Camera_Driver_Node()
    rclpy.spin(node)
    rclpy.shutdown()
     
     
if __name__ == "__main__":
    main()