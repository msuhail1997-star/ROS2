import rclpy
from rclpy.node import Node
from std_msgs.msg import String  

class BatterySubscriber(Node):
    def __init__(self): 
        super().__init__('battery_subscriber')
        self.subscriber = self.create_subscription(
            String,
            '/battery',
            self.callback_function,
            10
        )

    def callback_function(self, msg): 
        battery_text = msg.data     
        
        self.get_logger().info(f"Received: {battery_text}")   
        if battery_text in ["Battery = 10%", "Battery = 5%", "Battery = 15%"]:
            self.get_logger().warn("Low Battery")
        elif battery_text == "Battery = 0%":
            self.get_logger().warn("Battery empty")
        elif battery_text == "Battery = 100%":
            self.get_logger().warn("Battery status Full")

    
def main(args=None):
    rclpy.init(args=args) 
    node = BatterySubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()
