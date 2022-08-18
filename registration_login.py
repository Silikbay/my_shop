import time
from selenium import webdriver
driver = webdriver.Chrome('C:\chromedriver.exe')
time.sleep(5)
driver.get("http://practice.automationtesting.in/")
Account = driver.find_element_by_id('menu-item-50')
Account.click()
address = driver.find_element_by_id('reg_mail')
address.send_keys('Derrik123@bk.ru')
password = driver.find_element_by_id('reg_password')
password.send_keys('Derr1k589')
reg_button = driver.find_element_bY_name('register')
reg_button.click()
driver.quit()



import time
from selenium import webdriver
driver = webdriver.Chrome('C:\chromedriver.exe')
time.sleep(5)
driver.get("http://practice.automationtesting.in/")
Account = driver.find_element_by_id('menu-item-50')
Account.click()
address = driver.find_element_by_id('username')
address.send_keys('Derrik123@bk.ru')
password = driver.find_element_by_id('password')
password.send_keys('Derr1k589')
log_button = driver.find_element_bY_name('login')
log_button.click()
driver.getPageSourse().conains('Logout')
driver.quit()
