from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
service_object=Service("C:\ChromeDriver\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_object)
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
time.sleep(2)

driver.execute_script('window.scrollBy(0,300)')

driver.get_screenshot_as_file('screenshot1.png')
time.sleep(2)
driver.quit()