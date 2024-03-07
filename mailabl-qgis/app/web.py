import requests

class WebLinks:
    def __init__(self):
        self.page_maa_amet = 'https://geoportaal.maaamet.ee/est/Ruumiandmed/Maakatastri-andmed/Katastriuksuste-allalaadimine-p592.html'
        self.page_mailabl_home = 'https://mailabl.com'
        self.page_mailabl_terms_of_use = 'https://mailabl.com/terms-of-use/'
        self.page_privacy_policy = 'https://mailabl.com/privacy-policy/'

class loadWebpage:
# maa-ameti kodulehe avamine
    @staticmethod
    def Open_MaaAmet_webpage(self):
        self.sw_HM_Andmete_laadimine.setCurrentIndex(2)
        self.sw_HM.setCurrentIndex(7)
        self.swWorkSpace.setCurrentIndex(1)
        self.swCadastral_sub_processes.setCurrentIndex(4)
        loadWebpage.open_webpage(WebLinks().page_maa_amet)
        
    # Avab Mailabli koduka lingi
    @staticmethod
    def open_Mailabl_homepage():
        # Define the web link URL
        web_link = 'https://mailabl.com'
        # Make an HTTP GET request with SSL verification disabled
        response = requests.get(web_link, verify=False)
        # Open the response URL with the default browser
        import webbrowser
        webbrowser.open(response.url)
        
    @staticmethod
    def open_webpage(page_address):
        # Define the web link URL
        web_link = page_address
        # Make an HTTP GET request with SSL verification disabled
        response = requests.get(web_link, verify=False)
        # Open the response URL with the default browser
        import webbrowser
        webbrowser.open(response.url)
        