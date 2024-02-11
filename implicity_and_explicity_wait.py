from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait #kete time wait karibaku aeta lekhajae
from selenium.webdriver.support import expected_conditions as EC #condition deba pain use karajae
import time

service_object = Service("C:\ChromeDriver\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_object)

driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.implicitly_wait(5)
serch_bar=driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys('ber')
time.sleep(2)
click_add_to_cart=driver.find_elements(By.XPATH,"//div[@class='products']/div")

for i in  click_add_to_cart:
    i.find_element(By.XPATH,"div/button").click()

driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys('kjskj')
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()

# result=driver.find_element(By.CSS_SELECTOR,".promoInfo").text
# print(result)#aethe amara red ra jau invlid code ase sethipain lekhajae

#explicity wait
wait = WebDriverWait(driver,15)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
#explicity wait gote conditional wait sethipain taku import karibaku padiba





time.sleep(5)
driver.quit()
