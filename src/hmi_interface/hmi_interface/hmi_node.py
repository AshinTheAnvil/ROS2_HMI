import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool, Int8
from flask import Flask, render_template
import threading

app = Flask(__name__)

class HMIInterfaceNode(Node):
    def __init__(self):
        super().__init__('hmi_interface_node')

        # Information state variables
        self.pick_info = {"pickId": None, "quantity": None}
        self.response_info = {"pickId": None, "pickSuccessful": None, "itemBarcode": None}
        self.door_state = True  # True means door is closed
        self.emergency_state = False  # False means e-button not pressed
        self.stack_light_state = 0  # 0 = operational, 1 = paused, -1 = emergency

        # ROS 2 subscribers
        self.create_subscription(Bool, 'door_state', self.door_callback, 10)
        self.create_subscription(Bool, 'emergency_button_state', self.emergency_callback, 10)
        self.create_subscription(Int8, 'stack_light_state', self.stack_light_callback, 10)

        # Start Flask in a separate thread
        flask_thread = threading.Thread(target=self.run_flask_app, daemon=True)
        flask_thread.start()

    def door_callback(self, msg):
        self.door_state = msg.data

    def emergency_callback(self, msg):
        self.emergency_state = msg.data

    def stack_light_callback(self, msg):
        self.stack_light_state = msg.data

    def run_flask_app(self):
        @app.route('/')
        def index():
            return render_template('index.html', pick_info=self.pick_info, 
                                   response_info=self.response_info,
                                   door_state=self.door_state,
                                   emergency_state=self.emergency_state,
                                   stack_light_state=self.stack_light_state)

        app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)


def main(args=None):
    rclpy.init(args=args)
    node = HMIInterfaceNode()
    try:
        rclpy.spin(node)  # Now ROS 2 can handle updates
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

