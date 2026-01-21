import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy

class ControlCenterPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)

    def click_card(self):
        el = self.wait.until(
            EC.presence_of_element_located(
                (AppiumBy.ID, "com.control.center.ioscontrol:id/resize_empty_card")
            )
        )
        el.click()
        print("Card clicked")

    def click_got_it(self):
        el = self.wait.until(
            EC.presence_of_element_located(
                (AppiumBy.ID, "com.control.center.ioscontrol:id/got_it_btn")
            )
        )
        el.click()
        print("Got It clicked")

    def click_cancel(self):
        el = self.wait.until(
            EC.presence_of_element_located(
                (AppiumBy.ID, "com.control.center.ioscontrol:id/cancel_button")
            )
        )
        el.click()
        print("Cancel clicked")

    def click_ios_widgets_nav(self):
        el = self.wait.until(
                EC.presence_of_element_located(
                 (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId(\"com.control.center.ioscontrol:id/navigation_bar_item_icon_view\").instance(2)")
            )
        )
        el.click()
        print("Ios Widgets Navigation clicked")

    def click_clock_widget(self):
        el = self.wait.until(
                EC.presence_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId(\"com.control.center.ioscontrol:id/image_view_holder\").instance(0)")
            )
        )
        el.click()
        print("Widget is selected")

    def click_use_this_widget(self):
        el = self.wait.until(
                EC.presence_of_element_located(
                (AppiumBy.ID, "com.control.center.ioscontrol:id/add_widget_layout")
            )
        )
        el.click()
        print("add widget button clicked")

    def click_add_to_home_screen(self):
        el = self.wait.until(
                EC.presence_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Add to home screen\")")
            )
        )
        el.click()
        print("widget added to home")

    def press_device_back(self, times=4):
        for _ in range(times):
            time.sleep(1)
            self.driver.back()
            print("Device back button pressed")

    def click_exit(self):
        el = self.wait.until(
            EC.presence_of_element_located(
                (AppiumBy.ID, "com.control.center.ioscontrol:id/exit_dialog_cancel")
            )
        )
        el.click()
        print("exit app")