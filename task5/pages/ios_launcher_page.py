from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class IosLauncherPage(BasePage):
    IOS_LAUNCHER_NAV = (
        AppiumBy.ANDROID_UIAUTOMATOR,"new UiSelector().text(\"IOS Launcher\")"
    )
    EMPTY_CARD = (
        AppiumBy.CLASS_NAME,"android.widget.ScrollView"
    )
    TOGGLE = (
        AppiumBy.ID,"com.control.center.ioscontrol:id/on_off_switch"
    )
    LAUNCHER_SELECT = (
        AppiumBy.ANDROID_UIAUTOMATOR,"new UiSelector().resourceId(\"android:id/checkbox\").instance(0)"
    )

    def click_ios_launcher_nav(self):
        self.click(self.IOS_LAUNCHER_NAV)
        print("IOS Launcher Navigation clicked")

    def click_empty_card(self):
        self.click(self.EMPTY_CARD)
        print("Empty card clicked")

    def click_toggle_on_off(self):
        self.click(self.TOGGLE)
        print("Toggle clicked")
        
    def click_apply_launcher(self):
        self.click(self.LAUNCHER_SELECT)
        print("IOS Launcher applied")