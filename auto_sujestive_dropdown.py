from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
service_object=Service("C:\ChromeDriver\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_object)
driver.get('https://rahulshettyacademy.com/dropdownsPractise/')
input_data = driver.find_element(By.ID,"autosuggest").send_keys('Ind')
time.sleep(2)
countruies=driver.find_elements(By.XPATH,"//li[@role='presentation']/a")
for i in countruies:
    print(i.text)
    if i.text=='India':
        i.click()
time.sleep(3)
driver.quit()