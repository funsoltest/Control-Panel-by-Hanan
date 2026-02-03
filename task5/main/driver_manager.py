from appium import webdriver
from appium.options.android import UiAutomator2Options

class DriverManager:

    def start_driver(self):
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.automation_name = "UiAutomator2"
        options.device_name = "99161FFAZ000FR"
        options.platform_version = "13"
        options.no_reset = True

        # Installed app
        options.app_package = "com.control.center.ioscontrol"
        options.app_activity = "com.example.controlcenter.ui.activities.MainActivity"

        driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
        driver.implicitly_wait(10)
        return driver