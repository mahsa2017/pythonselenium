from seleniumbase import BaseCase
class HomePage(BaseCase):
    logo_icon = '.custom-logo'
    get_started_btn = '#get-started'
    heading_text='h1'
    copyright_text = '.zak-footer-bar__1'
    menu_links = "//ul[@id='primary-menu'] //*[starts-with(@id,'menu-item')]"
    username = "#username"


    def open_page(self):
        # open home page
        self.open("http://practice.automationbro.com")

    def login(self):
        # Login commented out to fix it
        self.open("https://practice.automationbro.com/my-account")
        self.add_text(self.username, "testuser")
        self.add_text("#password", "PracticeSite123!!")
        self.click("button[name=login]")
        self.assert_text("Log out", ".woocommerce-MyAccount-content")

    def logout(self):
        self.open("https://practice.automationbro.com/my-account")
        self.click(".woocommerce-MyAccount-content a[href*=logout]")
        self.assert_element_visible("button[name=login]")