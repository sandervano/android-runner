from time import sleep

# noinspection PyUnusedLocal
def main(device, *args, **kwargs):
    device.clear_app_data('com.google.android.apps.maps') #Only on Offline
    sleep(1)

    """INITIAL LOCATION LOCKITO"""
    device.shell('input tap 642 1127')
    #for switching to lockito from google mapss
    # device.shell('input keyevent 187')
    # sleep(0.5)
    # device.shell('input keyevent 187')
    # sleep(1)

    #for selecting the trip we have already created
    device.shell('input tap 230 565')
    sleep(2)

    #for starting the trip
    device.shell('input tap 644 970')
    sleep(1)

    #to switch back to google maps
    # device.shell('input keyevent 187')
    # device.shell('input keyevent 187')
    # sleep(1)
