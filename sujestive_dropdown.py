from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
service_object=Service("C:\ChromeDriver\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_object)
driver.get('https://rahulshettyacademy.com/client')
driver.find_element(By.LINK_TEXT,'Register').click()
#selective dropdown
occupation_option_select=Select(driver.find_element(By.XPATH,"//select[@formcontrolname='occupation']"))
# occupation_option_select.select_by_index(4)   #ae type re bi ame 4 no ta select karipariba
# occupation_option_select.select_by_visible_text('Student')
occupation_option_select.select_by_value('2: Student')


time.sleep(3)
driver.quit()