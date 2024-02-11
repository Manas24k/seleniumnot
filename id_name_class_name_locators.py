from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
service_object=Service("C:\ChromeDriver\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_object)
driver.get('https://en-gb.facebook.com/')#opening url/heat url
# id pain
email=driver.find_element(By.ID,'email').send_keys('manas@4436gmail.com')
# email=driver.find_element(By.CSS_SELECTOR,'#email').send_keys('manasrout')
#Name psin
# email=driver.find_element(By.NAME,'email').send_keys('manas@1234')
#class name pain
# email=driver.find_element(By.CLASS_NAME,'inputtext').send_keys('manas@1234')
# #pasword pain classname re ame use karuche
password=driver.find_element(By.CLASS_NAME,'_9npi').send_keys('rout')

time.sleep(5)
driver.quit()