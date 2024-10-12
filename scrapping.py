import selenium.webdriver as driver
import selenium.webdriver.chrome.service as srv
import time

def scrape_website(url):
    
    path = "./chromedriver.exe"

    options = driver.ChromeOptions()
    
    chrome_service = srv.Service(executable_path=path)
    
    drv = driver.Chrome(service=chrome_service, options=options)

    try :
       
        drv.get(url)

        time.sleep(15)

        codedSite = drv.page_source

        return codedSite

    except Exception as e :

        print(f"Some error occurred: {e}")

    finally :

        drv.quit()

from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection

SBR_WEBDRIVER = 'https://brd-customer-hl_a101e284-zone-scrapesmart:uz47tjb0bcem@brd.superproxy.io:9515'


def main():
    print('Connecting to Scraping Browser...')
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        print('Connected! Navigating to https://example.com...')
        driver.get('https://example.com')

        print('Waiting captcha to solve...')
        solve_res = driver.execute('executeCdpCommand', {
            'cmd': 'Captcha.waitForSolve',
            'params': {'detectTimeout': 10000},
        })
        print('Captcha solve status:', solve_res['value']['status'])
        print('Navigated! Scraping page content...')
        html = driver.page_source
        print(html)


if __name__ == '__main__':
    main()