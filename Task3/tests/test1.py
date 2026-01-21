import time
from pages.control_center_page import ControlCenterPage

def test_control_center_flow(drivpyteer):
    pages = ControlCenterPage(drivpyteer)

    time.sleep(5)

    pages.click_card()
    pages.click_got_it()
    pages.click_cancel()
    pages.click_ios_widgets_nav()
    pages.click_clock_widget()
    pages.click_use_this_widget()
    pages.press_device_back()
    pages.click_exit()

    print("🎉 Test Completed Successfully")

