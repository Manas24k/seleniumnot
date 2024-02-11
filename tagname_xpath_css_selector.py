from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
service_object=Service("C:\ChromeDriver\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_object)
driver.get('https://www.facebook.com/campaign/landing.php?campaign_id=14884913640&extra_1=s%7Cc%7C550525805964%7Cb%7Cfb%20sign%20up%7C&placement=&creative=550525805964&keyword=fb%20sign%20up&partner_id=googlesem&extra_2=campaignid%3D14884913640%26adgroupid%3D128696221832%26matchtype%3Db%26network%3Dg%26source%3Dnotmobile%26search_or_content%3Ds%26device%3Dc%26devicemodel%3D%26adposition%3D%26target%3D%26targetid%3Dkwd-294779041346%26loc_physical_ms%3D9061993%26loc_interest_ms%3D%26feeditemid%3D%26param1%3D%26param2%3D&gclid=Cj0KCQiAnfmsBhDfARIsAM7MKi0CF2QGLQlAdirOMYkXfR_O1cuj1l1sCu32NVOQR3jeIpEGSXSOctYaAocEEALw_wcB')#opening url/heat url
#jadi ame janibalu chahuche ki kau jinisa ta amara kau tag then we use this type
# my_tag=driver.find_element(By.NAME,'firstname')
# print(my_tag.tag_name)
#xpath(absolute path and relatble path)
#absolute path
# First_name=driver.find_element(By.XPATH,'//div/div/div/div/form/div/div/div/div/div/div/input').send_keys('manas')
'''Relatble path'''
'''//tagname[@atribute=value]'''
# first_name=driver.find_element(By.XPATH,"//input[@name='firstname']").send_keys('manasr')
'''CSS selector'''
'''tagname[atribute='value']'''
'''#value'''
'''.value'''
Radio_button=driver.find_element(By.CSS_SELECTOR,"input[class='_8esa']").click()




time.sleep(5)
driver.quit()