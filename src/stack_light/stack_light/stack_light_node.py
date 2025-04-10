import rclpy
from rclpy.node import Node
from std_msgs.msg import Int8
from std_msgs.msg import Bool


class StackLightNode(Node):
    def __init__(self):
        super().__init__('stack_light_node')

        # Current state of the stack light (0 = operational, 1 = paused, -1 = emergency)
        self.stack_light_state = 0  

        # Publisher for stack light state
        self.publisher = self.create_publisher(Int8, 'stack_light_state', 10)
        self.timer = self.create_timer(1.0, self.publish_stack_light_state)

        # Subscribers to door and emergency button states
        self.door_subscriber = self.create_subscription(Bool, 'door_handle_state', self.door_callback, 10)
        self.emergency_subscriber = self.create_subscription(Bool, 'emergency_button_state', self.emergency_callback, 10)

        self.door_closed = True  # True means door is closed
        self.emergency_pressed = False  # False means no emergency

        self.get_logger().info("Stack-Light Node has started!")

    def publish_stack_light_state(self):
        """Publishes the current state of the stack light."""
        if self.emergency_pressed:
            self.stack_light_state = -1  # Emergency state
        elif not self.door_closed:
            self.stack_light_state = 1  # Paused state
        else:
            self.stack_light_state = 0  # Operational state

        msg = Int8()
        msg.data = self.stack_light_state
        self.publisher.publish(msg)

        state_str = {0: "OPERATIONAL", 1: "PAUSED", -1: "EMERGENCY"}[self.stack_light_state]
        self.get_logger().info(f"Stack-Light State: {state_str}")

    def door_callback(self, msg):
        """Updates the door state based on the door_handle_state topic."""
        self.door_closed = msg.data  # True means door closed, False means open
        self.get_logger().info(f"Received Door State: {'Closed' if self.door_closed else 'Open'}")

    def emergency_callback(self, msg):
        """Updates the emergency state based on the emergency_button_state topic."""
        self.emergency_pressed = msg.data  # True means emergency activated
        self.get_logger().warn(f"Received Emergency State: {'PRESSED' if self.emergency_pressed else 'RELEASED'}")


def main(args=None):
    rclpy.init(args=args)
    node = StackLightNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

