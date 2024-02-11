from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
service_object=Service("C:\ChromeDriver\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_object)
driver.get('https://www.naukri.com/registration/createAccount?othersrcp=22636')

fullname=driver.find_element(By.ID,'name').send_keys('manasranjan rout')
email=driver.find_element(By.NAME,'email').send_keys('routm4436@gmial.com')
password=driver.find_element(By.ID,'password').send_keys('12345')
Mobailenumber=driver.find_element(By.ID,'mobile').send_keys('9337073242')

time.sleep(5)
driver.quit()