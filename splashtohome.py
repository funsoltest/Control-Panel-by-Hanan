from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# --------------------
# Desired Capabilities
# --------------------
options = UiAutomator2Options()
options.platform_name = "Android"
options.automation_name = "UiAutomator2"
options.device_name = "24021JEGR00133"
options.platform_version = "16"
options.app = r"C:\Users\hannan\Documents\AndroidAutomation\ControlPanelPlus.apk"
# Already installed app
#options.app_package = "com.controlpanel.app"
#options.app_activity = "com.controlpanel.app.MainActivity"

options.disable_hidden_api_policy = True
options.no_reset = True  # do not reinstall app

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
wait = WebDriverWait(driver, 30)

# --------------------
# 1️⃣ Wait for app loading complete / home screen
# --------------------
print("Waiting for app to load...")
time.sleep(15)

# --------------------
# 2️⃣ Tap on screen (center tap)
# --------------------
print("Tapping on screen...")
size = driver.get_window_size()
x = size["width"] // 2
y = size["height"] // 2
driver.tap([(x, y)], 300)

# --------------------
# 3️⃣ Wait for Accessibility bottom sheet
# --------------------
print("Waiting for Got It button...")
got_it_btn = wait.until(
    EC.presence_of_element_located(
        (AppiumBy.ANDROID_UIAUTOMATOR,
         'new UiSelector().textContains("Got")')
    )
)
got_it_btn.click()
print("Clicked Got It")

# --------------------
# 4️⃣ Wait for second permission bottom sheet
# --------------------
print("Waiting for Cancel button...")
cancel_btn = wait.until(
    EC.presence_of_element_located(
        (AppiumBy.ANDROID_UIAUTOMATOR,
         'new UiSelector().textContains("Cancel")')
    )
)
cancel_btn.click()
print("Clicked Cancel")

# --------------------
# Done
# --------------------
print("Automation completed successfully ✅")
time.sleep(3)
driver.quit()