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

