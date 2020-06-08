
import random 
import array 
import string
import datetime

MAX_LEN = 18
a=list()
b=list()
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']   
LOCASE_CHARACTERS = string.ascii_lowercase 
for cahr in LOCASE_CHARACTERS:
    a.append(cahr)  
UPCASE_CHARACTERS = LOCASE_CHARACTERS.upper() 
for cahr1 in UPCASE_CHARACTERS:
    b.append(cahr1)  
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')'] 
COMBINED_LIST = DIGITS + b + a + SYMBOLS 
rand_digit = random.choice(DIGITS) 
rand_upper = random.choice(UPCASE_CHARACTERS) 
rand_lower = random.choice(LOCASE_CHARACTERS) 
rand_symbol = random.choice(SYMBOLS) 
temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol 
for x in range(MAX_LEN - 4): 
    temp_pass = temp_pass + random.choice(COMBINED_LIST) 
date = datetime.datetime.now()
date=str(date)
date.split("-")
date=date[9]
password=temp_pass+date
print(password)

