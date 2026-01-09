import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


PROMISED_DOWN = 100
PROMISED_UO = 10
CHROME_DRIVER_PATH = ''
TWITTER_LOG = '@matheuspvds'
TWITTER_PASS = 'Ma!@978465'
INTERNET_SPEED_SITE = 'https://www.speedtest.net'
TWITTER_SITE = 'https://x.com/i/flow/login'


class InternetSpeedTwitterBot:
    def __init__(self,driver_path):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.up = 0
        self.down = 0
    def getinternetspeed(self):
        site = self.driver.get(INTERNET_SPEED_SITE)
        time.sleep(1)
        go_button = self.driver.find_element('xpath', '/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]/a/span[4]')
        go_button.click()
        time.sleep(40)
        self.down = self.driver.find_element('xpath', '/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element('xpath', '/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

    def tweetatprovider(self):
        self.driver.get(TWITTER_SITE)
        time.sleep(2)
        # enteraccount_button = self.driver.find_element('xpath','/html/body/div/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a')
        # enteraccount_button.click()
        loginbox = self.driver.find_element('xpath','/html/body/div/div/div/div[1]/div/div/div/div/div/div/div['
                                                    '2]/div[2]/div/div/div[2]/div[2]/div/div/div/div['
                                                    '4]/label/div/div[2]/div/input')
        loginbox.send_keys(TWITTER_LOG)
        next_button = self.driver.find_element('xpath', '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div['
                                                        '2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')
        next_button.click()
        time.sleep(2)
        passwordbox = self.driver.find_element('xpath', '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div['
                                                        '2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div['
                                                        '3]/div/label/div/div[2]/div[1]/input')
        passwordbox.send_keys(TWITTER_PASS)
        enter_button = self.driver.find_element('xpath', '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div['
                                                         '2]/div[2]/div/div/div[2]/div[2]/div['
                                                         '2]/div/div/div/div/button')
        enter_button.click()
        time.sleep(5)

        tweeting_box = self.driver.find_element('xpath','/html/body/div[1]/div/div/div['
                                                        '2]/main/div/div/div/div/div/div[3]/div/div[2]/div['
                                                        '1]/div/div/div/div[2]/div['
                                                        '1]/div/div/div/div/div/div/div/div/div/div/div/div['
                                                        '1]/div/div/div/div/div/div[2]/div')
        time.sleep(2)
        tweet = f'\nHey internet provider, why is my internet at {self.up}mgbps UP/{self.down}mgbps DOWN when i pay for 10mgbps UP / 100mgbps DOWN'
        tweeting_box.send_keys(tweet)
        time.sleep(3)
        post_button = self.driver.find_element('xpath', '/html/body/div[1]/div/div/div[2]/main/div/div/div/div['
                                                        '1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div['
                                                        '2]/div[2]/div/div/div/button')
        post_button.click()
        time.sleep(3)
bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
# bot.getinternetspeed()
bot.tweetatprovider()
