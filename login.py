from selenium import webdriver
from pynput.keyboard import Key, Controller
import time
keyboard = Controller()
#define login credentials
#import text file and extract email and pass from it
username = ''
password = ''
#url and drivers

url = 'https://www.facebook.com/'
driver = webdriver.Chrome("C:/Users/harsh/Documents/chromedriver.exe")
#driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito') #incognito
driver.get(url)
# task starts
driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id('pass').send_keys(password)
#complete entries here
driver.find_element_by_id('loginbutton').click()
#driver.close()
time.sleep(20)
for i in range(0,3,1):
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    time.sleep(1)
keyboard.type("person to search")
keyboard.press(Key.down)
keyboard.release(Key.down)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
