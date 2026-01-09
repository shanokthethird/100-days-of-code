from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# constants
URL = ('https://www.linkedin.com/jobs/search/?currentJobId=4043063301&f_LF=f_AL&geoId=102257491&keywords=python'
       '%20developer&location=London%2C%20England%2C%20United%20Kingdom')
SECS = 2

# keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
# webdriver setup
driver = webdriver.Chrome(chrome_options)

# get URL
driver.get(URL)
sleep(SECS)
try:
    print('TRYING DIRECTLY')
    enter_btn = driver.find_element(By.XPATH, 'html/body/div[1]/header/nav/div/a[2]')
    enter_btn.click()
except:
    try:
        print('TRYING FIRST TYPE')
        enter_btn = driver.find_element(By.XPATH, 'html/body/div[4]/div/div/section/div/div/div/div[2]/button')
        enter_btn.click()
        login_fld = driver.find_element(By.XPATH, 'html/body/div[4]/div/div/section/div/div/form/div[1]/div[1]/div/div/input')
        login_fld.send_keys('matheuspvds@gmail.com')

        pass_fld = driver.find_element(By.XPATH, 'html/body/div[4]/div/div/section/div/div/form/div[1]/div[2]/div/div/input')
        pass_fld.send_keys('maranata987456')

        enter_btn = driver.find_element(By.XPATH, 'html/body/div[4]/div/div/section/div/div/form/div[2]/button')
        enter_btn.click()
    except:
        print('TRYING SECOND TYPE')
        login_fld = driver.find_element(By.XPATH, 'html/body/div/main/div/form/section/div[2]/div[1]/input')
        login_fld.send_keys('matheuspvds@gmail.com')

        pass_fld = driver.find_element(By.ID, 'password')
        pass_fld.send_keys('maranata987456')

        enter_btn = driver.find_element(By.XPATH, 'html/body/div/main/div/form/section/button')
        enter_btn.click()
