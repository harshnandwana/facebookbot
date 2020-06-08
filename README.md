# facebookbot
 facebook registration and login bot that generates a temp mail and create a  new account
This is a facebook bot that can read the data from tempmail.org, and use that data to create a new account and that account is when registered can be used by next bot to login.
the data of all the registered mail goes directly into a text file so can be referred when in need.
to make this works we need several packages such as
```
pip install selenium
pip install pynput
pip install clipboard
```
. download chrome drivers for selenium.

all you have to do is first run "fb registration bot" then use "login.py"

sequence is such that the file named ks is the file used to generate the temp mail ids and copy those to clipboard. then this data is used in fb registration bot where the data is used to create a registration. pswrd is used to generate a strong password used to login and at last these all data is append in a file so as it can be used further to login and perform task.
