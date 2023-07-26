from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)


class RecorderTest(BaseCase):
    def test_recording(self):
        self.open("https://www.saucedemo.com/")
        self.type("input#user-name", "standard_user")
        self.type("input#password", "password")
        self.click("div.login_credentials_wrap-inner div:nth-of-type(2)")
        self.type("input#password", "secret_sauce")
        self.click("input#login-button")
        self.click("button#add-to-cart-sauce-labs-bike-light")
        self.click("div#shopping_cart_container a")
        self.click("button#checkout")
        self.type("input#first-name", "aaa")
        self.type("input#last-name", "bbb")
        self.type("input#postal-code", "12345")
        self.click("input#continue")
        self.click("button#finish")
        self.assert_element('img[alt="Pony Express"]')
