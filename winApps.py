# So since winapps is so damn shitty 
# imma do this myself ;_;
# gosh I hate my life

from pathlib import Path
import os
from difflib import SequenceMatcher

class winapps:

    WinApps = {}
    
    @classmethod
    def getInstalledApps(cls):
        
        mypath = f"{os.getenv('APPDATA')}/Microsoft/Windows/Start Menu/Programs"

        
        for r, d, f in os.walk(mypath):

            for file in f:
                filePath = os.path.join(r, file)
                cls.WinApps[filePath.split('\\')[-1].split('.')[0]] = filePath.replace('\\', '/')
                
        return cls.WinApps

    @classmethod
    def searchForApp(cls, appName):
        winapps.getInstalledApps()

        highest = None
        highesRatio = 0
        
        for app in winapps.WinApps.keys():
            ratio = SequenceMatcher(None, appName, app).ratio()
                        
            if ratio > highesRatio:
                highesRatio = ratio
                highest = app

        return winapps.WinApps[highest]

    @classmethod
    def launch(cls, app): 
        os.chdir('/'.join(app.split('/')[0:-1]))
        os.system(app.split('/')[-1])