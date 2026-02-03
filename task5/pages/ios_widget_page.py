from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class IosWidgetPage(BasePage):
    IOS_WIDGET_NAV = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.control.center.ioscontrol:id/navigation_bar_item_icon_view").instance(2)'
    )

    CLOCK_WIDGET = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.control.center.ioscontrol:id/image_view_holder").instance(0)'
    )

    ADD_WIDGET_BTN = (AppiumBy.ID, "com.control.center.ioscontrol:id/add_widget_layout")

    ADD_HOME_SCREEN = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Add to home screen")'
    )

      # ---------- Actions ----------

    def click_ios_widgets_nav(self):
        self.click(self.IOS_WIDGET_NAV)
        print("IOS Widgets Navigation clicked")

    def click_clock_widget(self):
        self.click(self.CLOCK_WIDGET)
        print(" Clock Widget selected")

    def click_use_this_widget(self):
        self.click(self.ADD_WIDGET_BTN)
        print("Add widget clicked")

    def click_add_to_home_screen(self):
        self.click(self.ADD_HOME_SCREEN)
        print("Widget added to home")