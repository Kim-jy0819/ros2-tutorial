#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.srv import TeleportAbsolute


class TurtlesimAbsoluteClient(Node):
    def __init__(self):
        super().__init__('turtlesim_abs_client')

        self.client = self.create_client(TeleportAbsolute, '/turtle1/teleport_absolute')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.request = TeleportAbsolute.Request()

    def send_request(self, x_position: float, y_position: float, theta: float):
        """Send a request to the TeleportAbsolute service."""
        self.request.x = x_position
        self.request.y = y_position
        self.request.theta = theta

        self.future = self.client.call_async(self.request)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()


def main(args=None):
    rclpy.init(args=args)

    client = TurtlesimAbsoluteClient()
    client.send_request(10.0, 10.0, 1.0)

    client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()