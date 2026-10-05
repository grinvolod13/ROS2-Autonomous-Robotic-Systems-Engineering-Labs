import tqdm
import math
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import BatteryState



class BatteryConsumer(Node):
    def __init__(self)->None:
        super().__init__(node_name="consumer")
        self.consumer = self.create_subscription(
            msg_type=BatteryState,
            topic='battery_stats',
            callback=self.print_info,
            qos_profile=10,
        )
        self.bar = tqdm.tqdm(desc="Battery charge: ", total=100, unit="%", ncols=100)
        self.percentage = 0.0
        
    def print_info(self, msg: BatteryState)->None:
        # self.bar.update(-100 *)
        update =(float(msg.percentage) - self.percentage)*100
        self.bar.update(update)
        self.bar.refresh()
        self.percentage = float(msg.percentage)




def main(args=None):
    rclpy.init(args=args)
    
    node = BatteryConsumer()
    rclpy.spin(node)
    node.destroy_node()
    
    rclpy.shutdown()
    

if __name__ == '__main__':
    main()