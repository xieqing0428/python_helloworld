# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: 9-9.py
@time: 2019-01-12 20:56

9-9 电瓶升级：
在本节最后一个electric_car.py版本中，给Battery类添加一个名为upgrade_battery()的方法。
这个方法检查电瓶容量，如果它不是85，就将它设置为85。
创建一辆电瓶容量为默认值的电动汽车，调用方法get_range()，
然后对电瓶进行升级，并再次调用get_range()。
你会看到这辆汽车的续航里程增加了。

"""


class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        range_mile = 200
        if self.battery_size == 70:
            range_mile = 240
        elif self.battery_size == 85:
            range_mile = 270

        message = "This car can go approximately " + str(range_mile)
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类的属性，再初始化电动汽车特有的属性"""
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()

