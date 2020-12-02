import time
import pychromecast
import os
import json

def check():
    while True:
        try: 
            services, browser = pychromecast.discovery.discover_chromecasts()
            with open('./temp/chromecast.txt', 'w+') as f:
                devnames = []
                for service in services:
                    devnames.append(service[3])
                for name in devnames:
                    f.writelines(name+'\n')
                f.close()
                    
            pychromecast.discovery.stop_discovery(browser)
            time.sleep(10)
        except FileNotFoundError: 
            os.mkdir("cache")
            with open('./temp/chromecast.txt', 'w+') as f:
                devnames = []
                for service in services:
                    devnames.append(service[3])
                for name in devnames:
                    f.writelines(name+'\n')
                f.close()
            pychromecast.discovery.stop_discovery(browser)
            time.sleep(10)
    return

if __name__ == "__main__":
    check()