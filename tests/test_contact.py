from seleniumbase import BaseCase
from seleniumbase.common.exceptions import TextNotVisibleException

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
        try:
            self.assert_text("Thanks for contacting us! We will be in touch with you shortly", "div[role=alert]")
        except TextNotVisibleException:
            self.assert_text("We were unable to process your form, please try again.", "div[role=alert]")
