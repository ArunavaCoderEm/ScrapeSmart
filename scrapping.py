from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection

from bs4 import BeautifulSoup

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


def remove_unnecessery (htmlcode):
    
    bs = BeautifulSoup(htmlcode, "html.parser")
    body = bs.body
    
    if (body) :
         return str(body)
     
    else : 
        return ""
    
def clean_from_body(body):
    
    bs = BeautifulSoup(body, "html.parser")
    
    for i in bs(["style", "script"]):
        
        i.extract()
        
    cleaned = bs.get_text(separator="\n")
    
    cleaned_content = "\n".join(
        line.strip() for line in cleaned.splitlines() if line.strip()
    )
    
    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]