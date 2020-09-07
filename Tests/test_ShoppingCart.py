from PageObject.CheckoutPage2 import Checkout
from PageObject.DeliveryLocation import AddressConfirmation
from PageObject.HomePage import HomePage
from PageObject.finalCheckout import FinalCheckout
from utilities.BaseClass import BaseClass
from PageObject.CheckoutPage import CheckOut


class TestOne(BaseClass):

    def test_shoppingCart(self):
        homepage = HomePage(self.driver)
        homepage.shopItem().click()
        log= self.getLogger()
        log.info("Clicking on shop Button :")

        checkout = CheckOut(self.driver)
        checkout.ShopPhone().click()
        log.info("Clicking on the product to be purchased ")
        Product_text = self.driver.find_element_by_link_text("iphone X").text
        assert "iphone X" == Product_text
        log.info("The product selected is : "+Product_text)

        confirm_CheckOut = Checkout(self.driver)
        confirm_CheckOut.CheckoutConfirmation().click()
        log.info("Final Checkout is done :")

        confirm_address = AddressConfirmation(self.driver)
        confirm_address.address_confirmtion().click()

        successMsg = FinalCheckout(self.driver)
        successText = successMsg.alertSuccess().text
        assert "Success! Thank you!" in successText
        log.info("Alert received after successful placement of order : "+successText)













