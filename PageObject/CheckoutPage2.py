class Checkout:

    def __init__(self,driver):
        self.driver = driver


    def CheckoutConfirmation(self):
        return self.driver.find_element_by_css_selector("button[class='btn btn-success']")