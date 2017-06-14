from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\python\selenium\webdriver\chromedriver.exe') # Here is where you point to the chromedriver
driver.set_page_load_timeout(30)

#Navigate to hard coded website
driver.get('https://www.personableinsurance.com/index.html#/404/') 
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element_by_name('username').send_keys('agencyadmin')
driver.find_element_by_name('password').send_keys('')
driver.find_element_by_name('username').send_keys(Keys.RETURN)
driver.implicitly_wait(10)
