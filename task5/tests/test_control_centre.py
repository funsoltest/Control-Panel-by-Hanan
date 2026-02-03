import time
from pages.control_centre_page import ControlCentrePage
from pages.ios_launcher_page import IosLauncherPage
from pages.ios_widget_page import IosWidgetPage

def test_control_centre_flow(driver):

    control = ControlCentrePage(driver)
    ios_launcher = IosLauncherPage(driver)
    ios_widget = IosWidgetPage(driver)

    time.sleep(5)
    
    control.click_card()
    control.click_got_it()
    control.click_cancel()

    ios_widget.click_ios_widgets_nav()
    ios_widget.click_clock_widget()
    ios_widget.click_use_this_widget()
    ios_widget.click_add_to_home_screen()
    ios_widget.press_device_back(1)

    ios_launcher.click_ios_launcher_nav()
    ios_launcher.click_empty_card()
    ios_launcher.click_toggle_on_off()
    ios_launcher.click_apply_launcher()

    #control.press_device_back(2)
    #control.click_exit()

    print("Test Completed Successfully")