from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
service_object=Service("C:\ChromeDriver\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_object)
driver.get('https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG')
#parent sibling/precding sibling
# click_samsung_checkbox = driver.find_element(By.XPATH,"//div[text()='SAMSUNG']/preceding-sibling::div").click()
#precding sibling mane hauchiki ame samsumg ku click karibaku chahuche and jetebele insepct karuche bahuta godae miluchi
#no miluchi os ama ku samsung ra uparent ku copy karibaku padiba sethipain ame ae code lekhile ta parent ku nele
#folowing -sibling
click_realme_checkbox = driver.find_element(By.XPATH,"//div[@title='realme']/div/label/input/following-sibling::div[1]").click()

time.sleep(3)

driver.quit()