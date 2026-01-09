from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://secure-retreat-92358.herokuapp.com')
form1 = driver.find_element(By.NAME, 'fName')
form1.send_keys('asdff')
form2 = driver.find_element(By.NAME, 'lName')
form2.send_keys('asdf')
form3 = driver.find_element(By.NAME, 'email')
form3.send_keys('asdf@adsf.sd')
butt = driver.find_element(By.CSS_SELECTOR, 'button')
butt.click()