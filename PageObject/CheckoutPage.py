class CheckOut:

    def __init__(self, driver):
        self.driver = driver

    def ShopPhone(self):
        products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
        for product in products:
            productName = product.find_element_by_xpath("div/h4/a").text
            if productName == "iphone X":
                self.driver.find_element_by_css_selector("button[class='btn btn-info']").click()
        return self.driver.find_element_by_css_selector("a[class='nav-link btn btn-primary']")

