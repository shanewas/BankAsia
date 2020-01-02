# -*- coding: utf-8 -*-
"""AIW Base Framework

-*- config.py -*-

This module includes configurable settings that may differ from bot-to-bot or
from environment-to-environment e.g. settings that the developer may have to
change if they were working on Ubuntu as compared to working on Windows.

Example:
    
    The example below is what the contents of this file are expected to look like
    As aforementioned, only CONFIGURABLES may be added here (to be 
    used throughout the program)::

        $ WEBDRIVER_PATH = "/usr/lib64/chromium/chromedriver"

Creators:
    Names: Ehfaz & Shane
    Date of last edit: 23/10/2019

"""
#Code starts from here
#Edit below variables according to requirements

# Imports
from selenium import webdriver
from datetime import date
import os



# Uncomment below block if using remote webdriver

# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

APP_NAME = 'Bank_Asia_Account_Verification'
CLIENT_NAME = 'Bank Asia'


#defining driver properties
DIRPATH = os.getcwd()
BASE_DIR = DIRPATH
TODAY_DATE = str(date.today())
path = BASE_DIR + '/' + TODAY_DATE
options = webdriver.ChromeOptions()
prefs = {"download.default_directory": path}
options.add_experimental_option("prefs", prefs)
options.headless = False
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

options.add_argument("--window-size=1325x4000")




# In case of using local webdriver
# WEBDRIVER_PATH = '/usr/lib64/chromium/chromedriver'
WEBDRIVER_PATH = r'/home/tawhid/Desktop/first_page/chromedriver'





BROWSER = webdriver.Chrome(chrome_options=options,executable_path=WEBDRIVER_PATH)
# BROWSER_NID = webdriver.Chrome(chrome_options=options,executable_path=WEBDRIVER_PATH)

# Uncomment below block if using remote webdriver

# SELENIUM_GRID_URL = "http://198.0.0.1:4444/wd/hub"
# CAPABILITIES = DesiredCapabilities.CHROME.copy()
# BROWSER = webdriver.Remote(desired_capabilities=CAPABILITIES,
#                           command_executor=SELENIUM_GRID_URL)

# If more browser instances are required, please add below here
# Make sure to declare new variable for that instance i.e. BROWSER_TWO = ...

AWS_ACCESS_TOKEN = ''
NUMBER_OF_ENTRIES = ''

LOGGING_SERVER_URL = 'wss://localhost:8765'


