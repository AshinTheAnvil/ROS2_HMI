import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
from std_srvs.srv import Trigger  # Service to toggle door state

class DoorHandle(Node):
    def __init__(self):
        super().__init__('door_handle_node')
        self.door_closed = True  # Start with door closed
        self.publisher = self.create_publisher(Bool, 'door_state', 10)
        self.timer = self.create_timer(1.0, self.publish_door_state)  # Publish every second
        self.service = self.create_service(Trigger, 'toggle_door', self.toggle_door_service)

    def publish_door_state(self):
        msg = Bool()
        msg.data = self.door_closed
        self.publisher.publish(msg)
        state_str = "CLOSED" if self.door_closed else "OPEN"
        self.get_logger().info(f'Door is {state_str}')

    def toggle_door_service(self, request, response):
        self.door_closed = not self.door_closed  # Toggle state
        response.success = True
        response.message = f'Door state changed to {"CLOSED" if self.door_closed else "OPEN"}'
        self.get_logger().info(response.message)
        return response

def main(args=None):
    rclpy.init(args=args)
    node = DoorHandle()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
