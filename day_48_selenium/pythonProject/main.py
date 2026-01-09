# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# #keep browser open
# # chrome_options = webdriver.ChromeOptions()
# # chrome_options.add_experimental_option('detach', True)
# MINUTES = 0.1
# driver = webdriver.Chrome()
#
# driver.get('http://orteil.dashnet.org/experiments/cookie/')
# cookie_button = driver.find_element(By.ID, "cookie")
# # cursor_button = driver.find_element(By.ID, 'buyCursor')
# # grandma_button = driver.find_element(By.ID, 'buyGrandma')
# # factory_button = driver.find_element(By.ID, 'buyFactory')
# # mine_button = driver.find_element(By.ID, 'buyMine')
# # shipment_button = driver.find_element(By.ID, 'buyShipment')
# # lab_button = driver.find_element(By.ID, 'buyAlchemy lab')
# # portal_button = driver.find_element(By.ID, 'buyPortal')
# # time_button = driver.find_element(By.ID, 'buyTime machine')
# # money = int(driver.find_element(By.ID, 'money').text)
# timeout = time.time() + 60 * MINUTES
# timeout_start = time.time()
#
#
# def click_buttons(list2):
#     money = int(driver.find_element(By.ID, 'money').text)
#     print('money you have:', money, 'money you need for cursor', list2[0])
#     if money > list2[0]:
#         cursor_button = driver.find_element(By.ID, 'buyCursor')
#         cursor_button.click()
#         money = int(driver.find_element(By.ID, 'money').text)
#         print('money after buying cursor:',money, 'how much it cost:', list2[0])
#     print('moneey before grandma',money, 'money you need for grandma', list2[1])
#     if money > list2[1]:
#         grandma_button = driver.find_element(By.ID, 'buyGrandma')
#         print(grandma_button.text, list2[1])
#         grandma_button.click()
#     if money > list2[2]:
#         factory_button = driver.find_element(By.ID, 'buyFactory')
#         factory_button.click()
#         money = int(driver.find_element(By.ID, 'money').text)
#     if money > list2[3]:
#         mine_button = driver.find_element(By.ID, 'buyMine')
#         mine_button.click()
#         money = int(driver.find_element(By.ID, 'money').text)
#     if money > list2[4]:
#         shipment_button = driver.find_element(By.ID, 'buyShipment')
#         shipment_button.click()
#         money = int(driver.find_element(By.ID, 'money').text)
#     if money > list2[5]:
#         lab_button = driver.find_element(By.ID, 'buyAlchemy lab')
#         lab_button.click()
#         money = int(driver.find_element(By.ID, 'money').text)
#     if money > list2[6]:
#         portal_button = driver.find_element(By.ID, 'buyPortal')
#         portal_button.click()
#         money = int(driver.find_element(By.ID, 'money').text)
#     if money > list2[7]:
#         time_button = driver.find_element(By.ID, 'buyTime machine')
#         time_button.click()
#
#
# def cookie_clicker():
#     cookie_button.click()
#
#
# while True:
#     while time.time() < timeout:
#         cookie_clicker()
#     cost_list = driver.find_elements(By.CSS_SELECTOR, 'div b')
#     cost_list2 = [int(item.text.split('-')[1].strip().replace(',', '')) for item in cost_list[10:18]]
#     for costs in cost_list2:
#         print(costs)
#     click_buttons(cost_list2)



from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Get cookie to click on.
cookie = driver.find_element(by=By.ID, value="cookie")

# Get upgrade item ids.
items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60*5  # 5 minutes

while True:
    cookie.click()

    # Every 5 seconds:
    if time.time() > timeout:

        # Get all upgrade <b> tags
        all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
        item_prices = []

        # Convert <b> text into an integer price.
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # Get current cookie count
        money_element = driver.find_element(by=By.ID, value="money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(by=By.ID, value=to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5


# driver.get('https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/?th=1')
# driver.get('https://www.python.org?')

# price_dollar = driver.find_element(By.CLASS_NAME, value='a-price-whole').text
# price_cents = driver.find_element(By.CLASS_NAME, value='a-price-fraction').text
#
# print(f'This price is {price_dollar}.{price_cents}')
# stuff_dict = {}
# events_times_list = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
# events_names_list = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')
# events = {}
# for n in range(len(events_names_list)):
#     events[n] = {
#         "time": events_times_list[n].text,
#         "names": events_names_list[n].text
#     }
# print(events)
# # driver.close()
# driver.quit()
