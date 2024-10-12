from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection

SBR_WEBDRIVER = 'https://brd-customer-hl_a101e284-zone-scrapesmart:uz47tjb0bcem@brd.superproxy.io:9515'

def scrape_website(url):
    
    try:
        
        print("Connecting to Scraping Browser...")
        sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, "goog", "chrome")
        with Remote(sbr_connection, options=ChromeOptions()) as driver:
            driver.get(url)
            print("Waiting captcha to solve...")
            solve_res = driver.execute(
                "executeCdpCommand",
                {
                    "cmd": "Captcha.waitForSolve",
                    "params": {"detectTimeout": 10000},
                },
            )
            print("Captcha solve status:", solve_res["value"]["status"])
            print("Navigated! Scraping page content...")
            html = driver.page_source
            return html

    except Exception as e:
        print(f"Error occurred: {e}")
        
    finally :
        
        print("Scrapping done most probably")
