from seleniumbase import BaseCase

class ContactTest(BaseCase):
    def test_contact_page(self):
        # open page
        self.open("http://practice.automationbro.com/contact")

        # fill in all the fields
        self.send_keys('.contact-name input', 'Test Nome')
        self.send_keys('.contact-email input', 'Test@gmail.com')
        self.send_keys('.contact-phone input', '123456')
        self.send_keys('.contact-message textarea', 'This is a test')

        #click the submit button
        self.click("#evf-submit-277")

        #verify submit message
        self.assert_text("We were unable to process your form, please try again.", "div[role=alert]")