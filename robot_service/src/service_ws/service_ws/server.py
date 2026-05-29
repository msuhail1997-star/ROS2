import rclpy
from rclpy.node import Node
from turtlesim.srv import Kill 

class RobotDataServer(Node):
    def __init__(self):
        super().__init__('robot_data_server')
        self.srv = self.create_service(
            Kill, 
            'robot_data', 
            self.callback_function
        )
        self.get_logger().info('Service Is Active')

    def callback_function(self, request, response):
        command = request.name.strip().upper()
        if command == "ON":
            self.get_logger().info("Robot is switched ON")
        elif command == "OFF":
            self.get_logger().info("Robot is switched OFF")
        else:
            self.get_logger().warn(f"Unknown string modifier: {command}")
            
        return response
  
def main(args=None):
    rclpy.init(args=args)
    node = RobotDataServer()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
