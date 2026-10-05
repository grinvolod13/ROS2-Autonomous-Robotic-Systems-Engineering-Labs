# Battery class with fields from https://docs.ros.org/en/humble/p/sensor_msgs/msg/BatteryState.html

class Battery:
    def __init__(self):
        self.voltage = 5.0
        self.temperature = 21.1
        self.current = 1.0
        self.charge = 0.0
        self.capacity = 4000.0
        self.design_capacity = 4200.0
        self.percentage: float = self.charge / self.capacity # initial battery percentage, 0-1
        self.power_supply_status = 3
        self.power_supply_health = 1
        self.power_supply_technology = 0
        self.present = True
        self.cell_voltage = []
        self.cell_temperature = []
        self.location = "slot_0"
        self.serial_number = "test-001"
        
    def change_charge(self, percentage):
        if percentage>0:
            self.power_supply_status = 1
            if self.charge + self.capacity*percentage >= self.capacity:
                self.charge = self.capacity
                self.power_supply_status = 4
            else:
                self.charge += self.capacity*percentage
            
        elif percentage<0:
            self.power_supply_status = 2
            if self.charge + self.capacity*percentage <= 0:
                self.charge = 0.0
                self.power_supply_status = 3
            else:
                self.charge += self.capacity*percentage
        else:
            self.power_supply_status = 3

        self.percentage = self.charge / self.capacity
