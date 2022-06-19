from hardware.v9.device import Device as DeviceV9


class Device(DeviceV9):
    def __init__(self):
        pass

    def do_something_v10(self):
        print('V 10')

    def do_something(self):
        print('V 10')