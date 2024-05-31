# Class File to define Browser instances for the test that is to be performed !
class BrowserConfig:

    # Initialization
    def __init__(self, browser_name):
        self.browser_name = browser_name.lower()

    # Gets the Browser Driver based on user input
    def get_webdriver(self):
        if self.browser_name == "chrome":
            from selenium.webdriver import Chrome
            return Chrome()
        elif self.browser_name == "firefox":
            from selenium.webdriver import Firefox
            return Firefox()
        elif self.browser_name == "edge":
            from selenium.webdriver import Edge
            return Edge()
        # Add more browsers as needed in future
        else:
            raise ValueError(f"Browser '{self.browser_name}' is not supported.")
