

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
shop = driver.find_element_by_xpath('//a[contains(text(), "Shop")]')
shop.click()
book = driver.find_element_by_class('attachment-shop_catalog size-shop_catalog wp-post-image')
book.click()
element = driver.find_element_by_class('product_title entry-title')
element_get_text = element.text
assert element_get_text == "HTML5 Forms"
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
shop = driver.find_element_by_xpath('//a[contains(text(), "Shop")]')
shop.click()
product = driver.find_element_by_xpath('//a[contains(text(), "HTML")] ')
product.click()
element = driver.find_element_by_css_selector('woocommerce_product_categories-2 .span:nth-child(2)')
element_get_text = element.text
assert element_get_text == "(3)"
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
shop = driver.find_element_by_xpath('//a[contains(text(), "Shop")]')
shop.click()
from selenium.webdriver.support.select import Select
element = driver.find_element_by_cclass("orderby")
select = Select(element)
select.select_by_visible_text("Default sorting")
select.select_by_value("menu_order")
print('Default sorting')
sel = driver.find_element_by_tag_name("orderby").click()
high_low = driver.find_element_by_css_selector("option:nth-child(6)").click()
element = driver.find_element_by_cclass("orderby")
from selenium.webdriver.support.select import Select
el = driver.find_element_by_cclass("orderby")
select = Select(el)
select.select_by_visible_text("Sort by price: low to high")
select.select_by_value("price")
print('low to high')
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
shop = driver.find_element_by_xpath('//a[contains(text(), "Shop")]')
shop.click()
time.sleep(3)
book = driver.find_element_by_css_selector('content a:nth-child(1)')
book.click()
book_old_price = driver.find_element_by_css_selector(".price > del > span")
book_old_price_text = book_old_price.text
assert book_old_price_text == "₹600.00"
book_new_price = driver.find_element_by_css_selector(".price > ins > span")
book_new_price_text = book_old_price.text
assert book_old_price_text == "₹450.00"
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
some_element = driver.find_element_by_class("woocommerce-main-image zoom").click()
element_check = WebDriverWait(driver, 10 ).until(
    EC.element_to_be_selected(some_element))
close_el = driver.find_element_by_class("pp_close").click()
ele_check = WebDriverWait(driver, 10 ).until(
    EC.element_to_be_selected(close_el))
driver.quit()


import time
from selenium import webdriver
driver = webdriver.Chrome('C:\chromedriver.exe')
time.sleep(5)
driver.get("http://practice.automationtesting.in/")
shop = driver.find_element_by_xpath('//a[contains(text(), "Shop")]')
shop.click()
book = driver.find_element_by_css_selector('content li:nth-child(4)>a:nth-child(2)')
book.click()
element = driver.find_element_by_class("cartcontents")
element_get_text = element.text
assert element_get_text == "1 item"
element = driver.find_element_by_class("wpmenucartli .amount")
element_get_text = element.text
assert element_get_text == "180"
basket = driver.find_element_by_class('wpmenucart-icon-shopping-cart-0')
basket.click()
driver.find_element_by_css_selector('div tbody .cart-subtotal:nth-child(1)')
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
some_element = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.div .tbody .cart-subtotal:nth-child(1)'), "180"))
some_element = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.div .strong .span:nth-child(1)'), "183.60"))
driver.quit()


import time
from selenium import webdriver
driver = webdriver.Chrome('C:\chromedriver.exe')
time.sleep(5)
driver.get("http://practice.automationtesting.in/")
shop = driver.find_element_by_xpath('//a[contains(text(), "Shop")]')
shop.click()
driver.execute_script("window.scrollBy(0, 600);")
book = driver.find_element_by_css_selector('content li:nth-child(4)>a:nth-child(2)')
book.click()
time.sleep(5)
book2 = driver.find_element_by_css_selector('content li:nth-child(5)>a:nth-child(2)')
book2.click()
basket = driver.find_element_by_class('wpmenucart-icon-shopping-cart-0')
basket.click()
time.sleep(3)
delete = driver.find_element_by_css_selector('div tbody tr >td:nth-child(1)>a:nth-child(1)')
delete.click()
cancel = driver.find_element_by_xpaht('//a[contains(text(), "Undo?")]')
cancel.click()
field = driver.find_element_by_name('cart[045117b0e0a11a242b9765e79cbf113f][qty]').clear()
field.send_kays('3')
update = driver.find_element_by_name('update_cart')
update.click()
element = driver.find_element_by_css_selector(".tbody .tr.td:nth-child(5)>div:nth-child(1)")
element_check = element.get_attribute("value")
assert element_check == "3"
time.sleep(3)
app = driver.find_element_by_name('apply_coupon')
app.click()
element = driver.find_element_by_css_selector("page-34 li:nth-child(1)")
element_get_text = element.text
assert element_get_text == "Please enter a coupon code"
driver.quit()



from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
driver = webdriver.Chrome('C:\chromedriver.exe')
time.sleep(5)
driver.get("http://practice.automationtesting.in/")
shop = driver.find_element_by_xpath('//a[contains(text(), "Shop")]')
shop.click()
driver.execute_script("window.scrollBy(0, 300);")
book = driver.find_element_by_css_selector('content li:nth-child(4)>a:nth-child(2)')
book.click()
basket = driver.find_element_by_class('wpmenucart-icon-shopping-cart-0')
basket.click()
save_changes_btn = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, ("//a[contains(text(), 'Proceed to Checkout')]"))))
link_check = WebDriverWait(driver, 10).until(
    EC.url_to_be("https://practice.automationtesting.in/checkout/"))
name = driver.find_element_by_id('billing_first_name')
name.send_keys('Derrik')
name_last = driver.find_element_by_id('billing_last_name')
name_last.send_keys('derrikovich')
mail = driver.find_element_by_id("billing_email")
mail.send_keys('Derrik231@bk.ru')
driver.find_element_by_id("select2-drop-mask").click()
sel = driver.find_element_by_class('select2-input')
sel.send_keys('iceland')
btn = driver.find_element_by_id('select2-chosen-1')
btn.click()
phone = driver.find_element_by_id('billing_phone')
phone.send_keys('89004445643')
zip = driver.find_element_by_id('billing_postcode')
zip.send_keys('567')
town = driver.find_element_by_id('billing_city')
town.send_keys('tnbnhh')
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(5)
pay = driver.find_element_by_id('payment_method_cheque')
pay.click()
btn2 = driver.find_element_by_id(' place_order')
btn2.click()
some_element= WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CLASS, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
some_element= WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "page-35 li:nth-child(4)>strong"), "Check Payments"))
driver.quit()
