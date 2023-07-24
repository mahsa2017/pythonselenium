
from seleniumbase import BaseCase
tolUrl = "https://www.credem.it/content/credem/it/privati-e-famiglie/conti-servizi-e-carte/servizi_online/trading_online.html"
footerText = "© 2017 Gruppo Bancario Credito Emiliano - Credem | P.IVA CredemBanca: 02823390352"

class TolTest(BaseCase):
    def test_tol(self):
       # open home page
       self.open(tolUrl)

       # assert page title
       self.assert_title("Trading Online: Piattaforma per Investire in Borsa | CREDEM")



       # scroll to bottom and asset the copyright text
       self.scroll_to_bottom()
       print(self.get_text(".footer-sm-copy"))
       self.assert_text(footerText, ".footer-sm-copy")
