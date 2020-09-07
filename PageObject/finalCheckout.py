class FinalCheckout:
    def __init__(self, driver):
        self.driver=driver

    def alertSuccess(self):
        self.driver.get_screenshot_as_file("Screen.png")
        return self.driver.find_element_by_css_selector("div[class='alert alert-success alert-dismissible']")


