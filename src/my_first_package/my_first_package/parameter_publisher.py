#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ParameterPublisher(Node):
    def __init__(self):
        super().__init__('parameter_publisher')
        
        # Declare parameter
        self.declare_parameter('greeting', 'Hello ROS 2!')
        self.greeting = self.get_parameter('greeting').value
        
        self.publisher_ = self.create_publisher(String, 'chatter', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.i = 0
        self.get_logger().info(f'Publisher started with greeting: {self.greeting}')

    def timer_callback(self):
        msg = String()
        msg.data = f'{self.greeting} - Count: {self.i}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    node = ParameterPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
