from hardware.v10.device import Device as DeviceV10


class Device(DeviceV10):
    def __init__(self):
        pass

    def do_something_v9(self, override_v9: bool = True):
        print('V 11 - 9')

    def do_something_v10(self, override_v10: bool = True):
        print('V 11 - 10')

    def do_something_v11(self):
        print('V 11')

    def do_something(self):
        print('V 11')