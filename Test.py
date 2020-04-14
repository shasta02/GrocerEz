from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome(executable_path=r'C:\Users\NARAVENK\Downloads\chromedriver_win32 (1)\chromedriver.exe')
driver.get('http://safeway.com/')

userZip = '95123'
userProduct = 'banana'

time.sleep(7)
changeZip = driver.find_element_by_id('openFulfillmentModalButton')
time.sleep(5)
changeZip.click()
newZip = driver.find_element_by_xpath('//*[@id="storeFulfillmentModal"]/div/div/div[2]/input')
time.sleep(5)
newZip.clear()
newZip.click()
newZip.send_keys(userZip)
newZip.send_keys(Keys.ENTER)
selectZip = driver.find_element_by_xpath('//*[@id="fulfilmentInStore"]/div/div/div[1]/store-card/div[2]/div/a').click()
driver.find_element_by_id("skip-main-content").click()
driver.find_element_by_id("skip-main-content").clear()
driver.find_element_by_id("skip-main-content").send_keys(userProduct)
driver.find_element_by_name("search-form").submit()
driver.find_element_by_xpath("//img[@alt='Banana - Each']").click()

