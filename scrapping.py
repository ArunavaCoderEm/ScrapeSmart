import selenium.webdriver as driver
import selenium.webdriver.chrome.service as srv
import time

def scrape_website (url):
    
    path = "./chromedriver"
    options = driver.ChromeOptions()
    
    drv = driver.Chrome(service = srv(path), options = options)
    
    try :
        
        drv.get(url)
        codedSite = drv.page_source
        time.sleep(15)
        
        return codedSite
        
    except :
        
        print("Some error occured")
        
    finally :
        
        drv.quit()