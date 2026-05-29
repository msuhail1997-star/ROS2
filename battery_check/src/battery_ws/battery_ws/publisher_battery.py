import rclpy
from rclpy.node import Node
from std_msgs.msg import String  

class BatteryPublisher(Node):  
    def __init__(self):
        super().__init__('battery_publisher')
        self.publisher = self.create_publisher(String, '/battery', 10)
        self.battery_percentage = 100
        self.timer = self.create_timer(1.0, self.callback_function)
        
    def callback_function(self):
        if self.battery_percentage < 0:
            self.timer.cancel()
            return

        msg = String()
        msg.data = f"Battery = {self.battery_percentage}%"
        self.publisher.publish(msg)
        self.get_logger().info(f"Publishing battery percentage - {self.battery_percentage}%")  
        self.battery_percentage -= 5

    
def main(args=None):
    rclpy.init(args=args)  
    node = BatteryPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()
