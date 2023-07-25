from seleniumbase import BaseCase
from page_objects.home_page import HomePage

class HomeTest(HomePage):

   def setUp(self):
      super().setUp()
      print("Running before each test")
      # Login
      # self.login()

      # open home page
      self.open_page()

   def tearDown(self):
      print("Running after each test")
      # Logout
      # self.logout()

      super().tearDown()

   def test_home_page(self):

       # assert page title
       self.assert_title("Practice E-Commerce Site – Automation Bro")

       # assert logo
       self.assert_element(HomePage.logo_icon)

       # take a screen shot at this point
       self.save_screenshot("home_page", "custom_Screenshot")

       # click on the get started button and assert the url
       self.click(HomePage.get_started_btn)
       get_Started_url = self.get_current_url()
       self.assert_equal(get_Started_url, "https://practice.automationbro.com/#get-started" )
       self.assert_true("get-started" in get_Started_url)

       # get the text of the header and assert the value
       self.assert_text("Think different. Make different.", "h1" )

       # scroll to bottom and asset the copyright text
       self.scroll_to_bottom()
       print(self.get_text(".zak-footer-bar__1"))
       self.assert_text("Copyright © 2020 Automation Bro", HomePage.copyright_text)

   def test_menu_links(self):
       expectedlinks = [ 'Home','About','Shop','Blog', 'Contact','My account']

       #find menu links elements
       menu_links_el = self.find_elements(HomePage.menu_links)

       #loop through our menu links
       for idx, link_el in enumerate(menu_links_el):
          print(idx, link_el.text)
          self.assertEqual(expectedlinks[idx], link_el.text)






