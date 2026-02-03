import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    DEFAULT_TIMEOUT= 40

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(
            driver,
            timeout=self.DEFAULT_TIMEOUT
            )
        
            # ---------Wait ----------

    def wait_for_visible(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    # ---------- actions ----------

    def click(self, locator):
        element= self.wait_for_clickable(locator)
        element.click()

    def get_text(self, locator):
       return self.wait_for_visible(locator).text
    
    def safe_click(self, locator, name="Element"):
        try:
            self.click(locator)
            print(f"{name} clicked")
        except TimeoutException:
            print(f"{name} not found — skipping")

    def press_device_back(self, times):
        for _ in range(times):
            time.sleep(1)
            self.driver.back()
            print(" Device back pressed")