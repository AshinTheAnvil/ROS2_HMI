import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
from std_srvs.srv import Trigger


class EmergencyButtonNode(Node):
    def __init__(self):
        super().__init__('emergency_button_node')
        self.button_pressed = False  # False means not pressed, True means pressed

        # Publisher for emergency button state
        self.publisher = self.create_publisher(Bool, 'emergency_button_state', 10)
        self.timer = self.create_timer(1.0, self.publish_button_state)

        # Services to press and release the button
        self.srv_press = self.create_service(Trigger, 'press_emergency_button', self.press_button_callback)
        self.srv_release = self.create_service(Trigger, 'release_emergency_button', self.release_button_callback)

        self.get_logger().info("Emergency Button Node has started!")

    def publish_button_state(self):
        """Publishes the current state of the emergency button."""
        msg = Bool()
        msg.data = self.button_pressed
        self.publisher.publish(msg)
        state = "PRESSED" if self.button_pressed else "RELEASED"
        self.get_logger().info(f"Emergency Button State: {state}")

    def press_button_callback(self, request, response):
        """Handles pressing the emergency button."""
        self.button_pressed = True
        self.get_logger().warn("Emergency Button PRESSED!")
        response.success = True
        response.message = "Emergency button is now pressed."
        return response

    def release_button_callback(self, request, response):
        """Handles releasing the emergency button."""
        self.button_pressed = False
        self.get_logger().info("Emergency Button RELEASED!")
        response.success = True
        response.message = "Emergency button is now released."
        return response


def main(args=None):
    rclpy.init(args=args)
    node = EmergencyButtonNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

