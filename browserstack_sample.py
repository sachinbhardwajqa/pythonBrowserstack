from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Options are only available since client version 2.3.0
options = UiAutomator2Options().load_capabilities({
    # Set URL of the application under test
    # "app" : "bs://c700ce60cf13ae8ed97705a55b8e022f13c5827c",
    "app" : "bs://2d98568077ea676dfc84f3c6fca457a0c675e798",
    # Specify device and os_version for testing
    "platformVersion" : "9.0",
    "deviceName" : "Google Pixel 3",
    # Set other BrowserStack capabilities
    'bstack:options' : {
        "projectName" : "Baliston Python project",
        "buildName" : "browserstack-build-11",
        "sessionName" : "Baliston BStack Test",
        # Set your access credentials
        "userName" : "ersachin_hS87en",
        "accessKey" : "tmyn26QYqFZzfy7qRCLh"
    }
})
# Initialize the remote Webdriver using BrowserStack remote URL
# and options defined above
print("Start of Test")
driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)
# Test case for the BrowserStack sample Android app.
# If you have uploaded your app, update the test case here.
skip_element = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "skip_button"))
)
skip_element.click()

# search_input = WebDriverWait(driver, 30).until(
#     EC.element_to_be_clickable(
#         (AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text"))
# )
# search_input.send_keys("BrowserStack")
time.sleep(5)
# search_results = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
# assert (len(search_results) > 0)
# Invoke driver.quit() after the test is done to indicate that the test is completed.

print("End of Test")
driver.quit()
