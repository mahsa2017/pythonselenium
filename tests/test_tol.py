
from seleniumbase import BaseCase
tolUrl = "https://www.credem.it/content/credem/it/privati-e-famiglie/conti-servizi-e-carte/servizi_online/trading_online.html"

class TolTest(BaseCase):
    def test_tol(self):
       # open home page
       self.open(tolUrl)

       # assert page title
       self.assert_title("Trading Online: Piattaforma per Investire in Borsa | CREDEM")