from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
service_object=Service("C:\ChromeDriver\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_object)
driver.get('https://rahulshettyacademy.com/AutomationPractice/')#opening url/heat url

name=driver.find_element(By.ID,'name').send_keys('manas')

click_conform_button=driver.find_element(By.ID,'confirmbtn').click()
alert_switch=driver.switch_to.alert

# alert_switch.accept()
alert_switch.dismiss()

time.sleep(3)
driver.quit()