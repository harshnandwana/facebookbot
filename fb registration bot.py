from selenium import webdriver
from pynput.keyboard import Key, Controller
import time
import random
import ks
import clipboard
import pswrd
keyboard = Controller()
f = open(r"database.txt", "a+")
#define login credentials
# for infinite or many acccount creation put the further code in loop and take import ks in loop yo.
firstname="hbgskhs"# here oyu can import a text files with name and surname
surname= "fgahjg"
mail= clipboard.paste()
passwrd=pswrd.password
print(passwrd)
day=random.randint(1,30)
day1=str(day)
monthlist=["jan","feb","mar","apr","may","jun","july","aug","sep","oct","no","dec"]
month=random.choice(monthlist)
year=random.randint(1970,2000)
year1=str(year)
f.write(mail+">"+passwrd+">"+day1+":"+month+":"+year1+">"+firstname+">"+surname)
f.close()
#url and drivers

url = 'https://www.facebook.com/'
driver = webdriver.Chrome("C:/Users/harsh/Documents/chromedriver.exe")
#driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito') #incognito
driver.get(url)
# task starts

driver.find_element_by_id('u_0_m').send_keys(firstname)
time.sleep(random.randint(1,5))
driver.find_element_by_id('u_0_o').send_keys(surname)
time.sleep(random.randint(1,5))
driver.find_element_by_id('u_0_r').send_keys(mail)
time.sleep(random.randint(1,5)*.4)
driver.find_element_by_id('u_0_u').send_keys(mail)
time.sleep(random.randint(1,5)*.6)
driver.find_element_by_id('u_0_w').send_keys(passwrd)
time.sleep(random.randint(1,5)*.3)
driver.find_element_by_id('day').send_keys(day)
time.sleep(random.randint(1,5)*.2)
driver.find_element_by_id('month').send_keys(month)
time.sleep(random.randint(1,5)*.5)
driver.find_element_by_id('year').send_keys(year)
time.sleep(random.randint(1,3))
#complete entries here
driver.find_element_by_id('u_0_7').click()
time.sleep(random.randint(1,8))
driver.find_element_by_id('u_0_13').click()

#driver.close()
time.sleep(20)
