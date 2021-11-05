from time import sleep

# noinspection PyUnusedLocal
def main(device, *args, **kwargs):
    """LOCKITO(After run)"""
    #switch back to lockito
    device.shell('input keyevent 187')
    device.shell('input keyevent 187')
    sleep(1)

    #stopping the mock for initial location
    device.shell('input tap 48 86')
    sleep(1)

    #confirm stopping
    device.shell('input tap 595 743')
    sleep(1)

    #for switching back to google maps
    device.shell('input keyevent 187')
    device.shell('input keyevent 187')
    sleep(1)
