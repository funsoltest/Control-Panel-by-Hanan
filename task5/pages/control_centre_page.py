from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class ControlCentrePage(BasePage):

    # ---------- Locators ----------
    CARD = (AppiumBy.ID, "com.control.center.ioscontrol:id/resize_empty_card")
    GOT_IT_BTN = (AppiumBy.ID, "com.control.center.ioscontrol:id/got_it_btn")
    CANCEL_BTN = (AppiumBy.ID, "com.control.center.ioscontrol:id/cancel_button")


    EXIT_BTN = (AppiumBy.ID, "com.control.center.ioscontrol:id/exit_dialog_cancel")

    # ---------- Actions ----------
    def click_card(self):
        self.safe_click(self.CARD, "Card")
        print("Empty card clicked")

    def click_got_it(self):
        self.safe_click(self.GOT_IT_BTN, "Got It")
        print("Got it button clicked")

    def click_cancel(self):
        self.safe_click(self.CANCEL_BTN, "Cancel")
        print("Cancel button clicked")

    def click_exit(self):
        self.click(self.EXIT_BTN)
        print("Exit clicked")