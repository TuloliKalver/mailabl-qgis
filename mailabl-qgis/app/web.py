import requests
import webbrowser

class WebLinks:
    def __init__(self):
        self.page_maa_amet = 'https://geoportaal.maaamet.ee/est/Ruumiandmed/Maakatastri-andmed/Katastriuksuste-allalaadimine-p592.html'
        self.page_mailabl_home = 'https://mailabl.com'
        self.page_mailabl_terms_of_use = 'https://mailabl.com/terms-of-use/'
        self.page_privacy_policy = 'https://mailabl.com/privacy-policy/'

class loadWebpage:
# maa-ameti kodulehe avamine


    @staticmethod
    def open_maa_amet_webpage_new():
        loadWebpage.open_webpage(WebLinks().page_maa_amet)



    @staticmethod
    def open_webpage(page_address):
        # Define the web link URL
        web_link = page_address
        # Make an HTTP GET request with SSL verification disabled
        
        try:
            response = requests.get(web_link, verify=False, timeout=10)
            # Open the response URL with the default browser
            
            webbrowser.open(response.url)
        except requests.exceptions.Timeout:
            print("Request timed out")
        