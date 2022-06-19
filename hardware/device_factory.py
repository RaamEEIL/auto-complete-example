from hardware.v9.device import Device as DeviceV9
from hardware.v10.device import Device as DeviceV10
from hardware.v11.device import Device as DeviceV11

# try:
#     from hardware.auto_generated_typing import Device
# except ModuleNotFoundError as mnfe:
#     from v9.device import Device as Device

try:
    from hardware.auto_generated_typing import Device
except ModuleNotFoundError as mnfe:
    try:
        from v9.device import Device
    except ModuleNotFoundError as mnfe:
        from hardware.auto_generated_typing import Device


def device_factory(version: int) -> Device:
    if version == 9:
        return DeviceV9()
    elif version == 10:
        return DeviceV10()
    elif version == 11:
        return DeviceV11()
    else:
        raise ValueError(f'No such version: {version}')
