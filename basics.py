import time

from YourStore.configuration.bowser_config import BrowserConfig

browser_name = "chrome"
browser_config = BrowserConfig(browser_name)
driver = browser_config.get_webdriver()

time.sleep(3)

driver.quit()