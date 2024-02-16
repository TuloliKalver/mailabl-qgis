import webbrowser
import requests

class loadWebpage:
# maa-ameti kodulehe avamine
    @staticmethod
    def Open_MaaAmet_webpage(self):
        self.sw_HM_Andmete_laadimine.setCurrentIndex(2)
        self.sw_HM.setCurrentIndex(7)
        self.swWorkSpace.setCurrentIndex(1)
        self.swCadastral_sub_processes.setCurrentIndex(4)

        # Define the web link URL
        web_link = 'https://geoportaal.maaamet.ee/est/Ruumiandmed/Maakatastri-andmed/Katastriuksuste-allalaadimine-p592.html'
        # Make an HTTP GET request with SSL verification disabled
        response = requests.get(web_link, verify=False)
        # Open the response URL with the default browser
        webbrowser.open(response.url)
        
    # Avab Mailabli koduka lingi
    @staticmethod
    def open_Mailabl_homepage():
        # Define the web link URL
        web_link = 'https://mailabl.com'
        # Make an HTTP GET request with SSL verification disabled
        response = requests.get(web_link, verify=False)
        # Open the response URL with the default browser
        webbrowser.open(response.url)