# Auto User Deletion From ForiGate Firewall


A Python Project based on Selenium package that deletes users from givel excel sheet containing the usernames to be deleted from the FortiGate 100F firewall.

## Contents
 - __main.py__: The main python file that runs the selenium code.
 - __data.xlsx__: Excel sheet containing the usernames present in the firewall to be deleted.
 - __credentials.ini__: A ini file containing the username, password and IP address to open the firewall page.
 

## Installation
Selenium package is required to run this Program.

Install the dependencies if not exists

```sh
pip install selenium
```

 ## How to Run
  - Open data.xlsx and fill the **username** column with username in firewall to be deleted.
  - Open credentials.ini and replace the values of link, username and password with correct value.
  - Run main.py
