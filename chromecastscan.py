import time
import pychromecast

def check():
    while True:
        services, browser = pychromecast.discovery.discover_chromecasts()
        with open('./cache/chromecast.txt', 'w+') as f:
            f.writelines(str(services))
            f.close()
        pychromecast.discovery.stop_discovery(browser)
        time.sleep(10)
    return