import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    #def press_back(self):
        #self.driver.execute_script("mobile: pressKey", {"keycode": 4})
    
    def _safe_click(self, locator, name):
        try:
            element = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located(locator)
            )
            element.click()
            print(f"{name} clicked")
        except TimeoutException:
            print(f"{name} not found — skipping")

    def press_device_back(self, times):
        for _ in range(times):
            time.sleep(1)
            self.driver.back()
            print(" Device back pressed")
