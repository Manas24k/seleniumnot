from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
service_object=Service("C:\ChromeDriver\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_object)
driver.get('https://www.naukri.com/')#opening url/heat url

time.sleep(5)
driver.quit()
