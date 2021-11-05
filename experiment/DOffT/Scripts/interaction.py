from time import sleep

# noinspection PyUnusedLocal
def main(device, *args, **kwargs):
    ################################################################################
    """Start run"""
    #for clicking the terms box
    print("========== PRessing ==========")
    # sleep(1)
    device.shell('input tap 357 1242')
    print("========== Pressed  ==========")
    # print('=INTERACTION=')
    # print((device.id))
    # print((device.current_activity()))
