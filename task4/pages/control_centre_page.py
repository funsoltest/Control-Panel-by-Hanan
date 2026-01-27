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
        self._safe_click(self.CARD, "Card")

    def click_got_it(self):
        self._safe_click(self.GOT_IT_BTN, "Got It")

    def click_cancel(self):
        self._safe_click(self.CANCEL_BTN, "Cancel")

    def click_exit(self):
        self.click(self.EXIT_BTN)
        print("Exit clicked")

  
