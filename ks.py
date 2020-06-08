from selenium import webdriver
from pynput.keyboard import Key, Controller
import time
import random
keyboard = Controller()
#url and drivers

url = 'https://temp-mail.org/en/'
driver = webdriver.Chrome("C:/Users/harsh/Documents/chromedriver.exe")
#driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito') #incognito
driver.get(url)
# task starts

driver.find_element_by_id('mail').click()
time.sleep(random.randint(1,5))
with keyboard.pressed(Key.ctrl):
    keyboard.press('a')
    keyboard.release('a')
with keyboard.pressed(Key.ctrl):
    keyboard.press('c')
    keyboard.release('c')

time.sleep(random.randint(1,3))
#complete entries here


driver.close()
#time.sleep(20)