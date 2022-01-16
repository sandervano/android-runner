# noinspection PyUnusedLocal
def main(device, *args, **kwargs):
    device.shell('input tap 600 1000')  # Prevent the device from sleeping
    device.clear_app_data('com.google.android.apps.maps')
    pass
