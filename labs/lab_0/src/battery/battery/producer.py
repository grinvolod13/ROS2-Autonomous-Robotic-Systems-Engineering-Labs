import random
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import BatteryState # pyright: ignore[reportMissingImports]

from .battery import Battery



def costruct_dto(obj: Battery)->BatteryState:
    dto = BatteryState()
    
    dto.voltage = obj.voltage
    dto.temperature = obj.temperature
    dto.current = obj.current
    dto.charge = obj.charge
    dto.capacity = obj.capacity
    dto.design_capacity = obj.design_capacity
    dto.percentage = obj.percentage
    dto.power_supply_status = obj.power_supply_status
    dto.power_supply_health = obj.power_supply_health
    dto.power_supply_technology = obj.power_supply_technology
    dto.present = obj.present
    dto.cell_voltage = obj.cell_voltage
    dto.cell_temperature = obj.cell_temperature
    dto.location = obj.location
    dto.serial_number = obj.serial_number

    return dto




class BatteryProducer(Node):
    def __init__(self) -> None:
        super().__init__(node_name="producer")
        self.publisher = self.create_publisher(
            msg_type=BatteryState,
            topic='battery_stats',
            qos_profile=20,
        )
        self.timer = self.create_timer(
            timer_period_sec=0.5,
            callback=self.timer_callback
        )
        self.battery = Battery()
        self.direction = 1
    
    def timer_callback(self) -> None:
        self.battery.change_charge(self.direction * random.uniform(0, 0.05))
        msg = costruct_dto(self.battery)
        print(msg)
        self.publisher.publish(msg)
        if self.battery.power_supply_status==4 or self.battery.power_supply_status==3:
            self.direction*=-1



def main(args=None):
    rclpy.init(args=args)
    
    node = BatteryProducer()
    rclpy.spin(node)
    node.destroy_node()
    
    rclpy.shutdown()
    

if __name__ == '__main__':
    main()
