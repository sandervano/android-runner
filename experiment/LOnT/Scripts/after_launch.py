from time import sleep
# noinspection PyUnusedLocal,PyUnusedLocal
def main(device, *args, **kwargs):
    sleep(10)


    ################################################################################
    """THEME SELECTION:"""
    #for opening google menu
    device.shell('input tap 653 92')
    sleep(1)

    #for opening settings
    device.shell('input tap 197 776') #Depends on deleting data
    sleep(1)

    #For swiping to bottom of settings
    device.shell('input swipe 401 1155 401 201')
    sleep(1)

    #for opening navigation settings
    device.shell('input tap 355 658')
    sleep(1)

    #Mute sound settings
    device.shell('input tap 135 354')
    sleep(1)

    #For swiping to lower end of nav settings
    device.shell('input swipe 401 1222 401 212')
    sleep(1)

    #Enter theme.
    device.shell('input tap 357 579') #Day: 357 579, Night:565 579                     <------- Treatment
    sleep(1)

    #for going back to map screen
    device.shell('input keyevent 4')
    # sleep(0.5)
    device.shell('input keyevent 4')
    sleep(1)


    ################################################################################
    """MAP TYPE SELECTION:"""
    #for opening the window
    device.shell('input tap 240 1234')
    sleep(1)

    device.shell('input tap 662 226')
    sleep(1)

    #for selecting default mode
    device.shell('input tap 355 395') #normal: 355, 395. #Sat: 488, 388                 <-------- Treatment
    sleep(1)

    #for going back to map screen
    device.shell('input keyevent 4')
    sleep(1)


    ################################################################################
    """FOR ENTERING ADDRESS AND STARTING NAVIGATION"""
    #for tapping search bar
    device.shell('input tap 200 106')
    sleep(1)

    #for entering Apple Amsterdam in the search window. %s is for space
    device.shell('input text "Veendam"')
    sleep(1)

    #for clicking the correct location
    device.shell('input tap 216 217')
    sleep(2)

    #610 1112

    #for tapping start button
    device.shell('input tap 362 1052')
    sleep(1)


    ################################################################################
    """LOCKITO(during the run)"""
    #switch back to lockito
    device.shell('input keyevent 187')
    device.shell('input keyevent 187')
    sleep(1)

    #stopping the mock for initial location
    device.shell('input tap 48 86')
    sleep(0.5)

    #confirm stopping
    device.shell('input tap 595 743')
    sleep(1)

    #for selecting the trip
    device.shell('input tap 288 298')
    sleep(1)

    #for starting the trip on lockito
    device.shell('input tap 643 942') #Might need adjusting with map icon in the way.
    sleep(1)

    #for switching back to google maps
    device.shell('input keyevent 187')
    device.shell('input keyevent 187')
    sleep(1)
