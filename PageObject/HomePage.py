class HomePage:
    def __init__(self,driver):
        self.driver=driver

    def shopItem(self):
        return self.driver.find_element_by_link_text("Shop")

    
