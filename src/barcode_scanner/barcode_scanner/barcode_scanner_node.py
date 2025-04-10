import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_srvs.srv import Trigger  # Correct service type
import random

class BarcodeScanner(Node):
    def __init__(self):
        super().__init__('barcode_scanner_node')
        self.barcode_publisher = self.create_publisher(String, 'scanned_barcode', 10)
        self.timer = self.create_timer(1.0, self.publish_barcode)
        self.latest_barcode = ''
        self.barcode_service = self.create_service(Trigger, 'get_last_scanned_barcode', self.get_last_scanned_barcode)

    def publish_barcode(self):
        barcode = str(random.randint(10000, 99999))
        self.latest_barcode = barcode
        msg = String()
        msg.data = barcode
        self.barcode_publisher.publish(msg)
        self.get_logger().info(f'Published barcode: {barcode}')
        
    def get_last_scanned_barcode(self, request, response):
        response.success = True
        response.message = self.latest_barcode  # Use 'message' instead of 'data'
        self.get_logger().info(f'Retrieved last scanned barcode: {self.latest_barcode}')
        return response

def main(args=None):
    rclpy.init(args=args)
    barcode_scanner = BarcodeScanner()
    rclpy.spin(barcode_scanner)
    barcode_scanner.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

