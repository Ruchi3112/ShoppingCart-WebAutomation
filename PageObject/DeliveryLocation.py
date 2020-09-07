from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class AddressConfirmation:
    def __init__(self,driver):
        self.driver=driver

    def address_confirmtion(self):
        self.driver.find_element_by_id("country").send_keys("Ind")
        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_css_selector("div[class='checkbox checkbox-primary']").click()
        return self.driver.find_element_by_css_selector("input[value='Purchase']")

