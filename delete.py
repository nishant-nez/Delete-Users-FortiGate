from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep
import pandas as pd

import configparser

config = configparser.ConfigParser()
config.read('credentials.ini')

fortiLink = config.get('firewall', 'link')
fortiUsername = config.get('firewall', 'username')
fortiPassword = config.get('firewall', 'password')

data = pd.read_excel('data.xlsx')
print(data)

def findXpath(xpath):
    count = 0
    while(1):
        if count > 20:
            print('error...exiting')
            exit()
        try:
            el = driver.find_element(by=By.XPATH, value=xpath)
            if count > 0:
                print('found')
            return el
        except:
            print('error...waiting')
            count += 1
            sleep(2)


chrome_options = Options()
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_options.allow_insecure_localhost = True
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()

driver.get(fortiLink)

try:
    details = driver.find_element(by=By.ID, value="details-button")
    details.click()
    insecure = driver.find_element(by=By.ID, value="proceed-link")
    insecure.click()
except:
    pass

sleep(3)
try:
    username = driver.find_element(by=By.ID, value="username")
    username.send_keys(fortiUsername)
    password = driver.find_element(by=By.ID, value="secretkey")
    password.send_keys(fortiPassword)
    loginBtn = driver.find_element(by=By.ID, value="login_button")
    loginBtn.click()
except:
    print("Wrong values enterd in credentials!")
    sleep(10)
    exit()
sleep(7)



for i in range(len(data)):
    driver.get(f'{fortiLink}/ng/user/local')
    sleep(5)
    fltrBtn = findXpath('//*[@id="navbar-view-section"]/div/div/f-local-user-list/f-mutable/div/div[2]/div/div/div[1]/div/div[1]/div[1]/button')
    fltrBtn.click()
    sleep(1)
    try:
        removeBtn = driver.find_element(by=By.XPATH, value='/html/body/div[147]/div/div[1]/div/div/div[4]/button')
        removeBtn.click()
        fltrBtn.click()
    except:
        pass
    txtBox = findXpath('/html/body/div[147]/div/div[1]/div/div/div[4]/div[2]/input')
    txtBox.send_keys(data['username'][i])
    txtBox.send_keys(Keys.ENTER)
    sleep(2)
    usr = driver.find_element(by=By.CSS_SELECTOR, value='div[column-id="name"]')
    sleep(2)
    usr.click()

    edit = findXpath('//*[@id="navbar-view-section"]/div/div/f-local-user-list/f-mutable/div/div[1]/div[2]/div/f-mutable-menu-transclude/f-local-user-list-menu/div[1]/div[2]/div/button')
    edit.click()

    ugrp = findXpath('//*[@id="ng-base"]/form/div[2]/div[1]/div[2]/dialog-content/section/div[5]/label[1]/span/label')
    ugrp.click()

    okBtn = findXpath('//*[@id="submit_ok"]')
    okBtn.click()
    sleep(3)

    usr = findXpath('//*[@id="navbar-view-section"]/div/div/f-local-user-list/f-mutable/div/div[2]/div/div/div[2]/div[2]/div[2]')
    usr.click()
    sleep(2)

    dltBtn = findXpath('//*[@id="navbar-view-section"]/div/div/f-local-user-list/f-mutable/div/div[1]/div[2]/div/f-mutable-menu-transclude/f-local-user-list-menu/div[1]/div[4]/div/button')
    dltBtn.click()
    # print(dltBtn.text)
    sleep(2)
    okBtn = findXpath('//*[@id="navbar-view-section"]/div/div[3]/div/div[2]/div[3]/button[1]')
    okBtn.click()
    sleep(5)

    print(f'{data["username"][i]} deleted successfully!')

print('\nAll data deleted successfully!')
sleep(20)
driver.close()
