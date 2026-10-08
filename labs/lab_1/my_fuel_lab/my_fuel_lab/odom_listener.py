
import rclpy
from rclpy.node import Node
# from sensor_msgs.msg import 
from nav_msgs.msg import Odometry # pyright: ignore[reportMissingImports]


class OdomListener(Node):
    def __init__(self)->None:
        super().__init__("odom_listener")
        self.subscriber = self.create_subscription(Odometry, "/odom", self.odom_callback, 1)
        
    def odom_callback(self, msg: Odometry)->None:
        position = msg.pose.pose.position
        x = position.x
        y = position.y
        z = position.z
        twist = msg.twist.twist.linear
        vx = twist.x
        vy = twist.y
        vz = twist.z
        speed = (vx**2 + vy**2 + vz**2)**0.5
        print(f"Position: x={x:.2f}, y={y:.2f}, z={z:.2f}, Speed: {speed:.2f}")
        



def main(args=None)->None:
    rclpy.init(args=args)
    node = OdomListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
        


