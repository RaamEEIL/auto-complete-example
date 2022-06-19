from hardware.device_factory import Device
from hardware.device_factory import device_factory

dev: Device = device_factory(11)
dev.do_somethin