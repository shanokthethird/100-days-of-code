from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests

FORMS_URL = 'https://forms.gle/D7rGuGuNUy9xhhxm9'
ZILLOW_URL = 'https://appbrewery.github.io/Zillow-Clone/'

class FormFiller:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.response = requests.get(ZILLOW_URL)
    def scrapezillow(self):
        self.zillow = BeautifulSoup(self.response.text, 'html.parser')
        self.prices = self.zillow.find_all('span', class_='PropertyCardWrapper__StyledPriceLine')
        self.links = self.zillow.find_all('a', class_='StyledPropertyCardDataArea-anchor')
        self.addresses = self.zillow.find_all('address')

    def fillform(self):
        self.driver.get(FORMS_URL)
        time.sleep(3)
        for x in range(len(self.prices)-1):
            first_box = self.driver.find_element(By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            first_box.send_keys(self.addresses[x].text.strip())
            second_box = self.driver.find_element(By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            second_box.send_keys(self.prices[x].text[:6])
            third_box = self.driver.find_element(By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            third_box.send_keys(self.links[x]['href'])
            send_button = self.driver.find_element(By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span')
            send_button.click()
            time.sleep(2)
            new_answer_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
            new_answer_button.click()
            time.sleep(2)

formfiller = FormFiller()
formfiller.scrapezillow()
formfiller.fillform()
