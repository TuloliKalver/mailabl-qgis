import webbrowser      

        self.pbAvaMaaAmet.clicked.connect(self.AvaMaaAmet)
            
        #maa-ameti kodulehe avamine
    def AvaMaaAmet(self):
        # Define the web link URL
        web_link = 'https://geoportaal.maaamet.ee/est/Ruumiandmed/Maakatastri-andmed/Katastriuksuste-allalaadimine-p592.html'
        
        # Open the web link with the default browser
        webbrowser.open(web_link)
