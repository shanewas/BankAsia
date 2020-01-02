# -*- coding: utf-8 -*-
"""AIW Base Framework

-*- controller.py -*-

This module consists of the actual functions that "do" tasks. The developer
is expected to write all the functions (as modular as possible) in this file
 - including the logging to server and calling all checks etc. This is one of
the few files where the developer has complete control over. However, the 
actual calling of the functions written here are expected to be within the 
bot.py file i.e. the flow and logic required is to be within bot.py 

Example:
    
    The rest of the code in this file can be considered as an example to follow,
    and discarded while coding.       

Creators:
    Names: Ehfaz & Shane
    Date of last edit: 24/10/2019
"""
#Your code starts from here

# Imports

import sys
sys.path.append("...") # Adds higher directory to python modules path.
import traceback
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from PIL import Image
from io import BytesIO
import definitions
import config
from datetime import datetime

class Document_Verification:

    def get_verified_image(self,browser,type_image,directory,xpath):
    # now that we have the preliminary stuff out of the way time to get that image :D
        element = browser.find_element_by_xpath(xpath) # find part of the page you want image of
        location = element.location
        size = element.size
        png = browser.get_screenshot_as_png() # saves screenshot of entire page
        im = Image.open(BytesIO(png)) # uses PIL library to open image in memory
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']
        im = im.crop((left, top, right, bottom)) # defines crop points
        im.save(r"{0}/{1}.png".format(directory, type_image)) # saves new cropped image
        return("image saved")

    def format_date(self,dob):
        date_time_str = str(dob)
        now = datetime.datetime.now()
        max_year = (now.year - 100) // 100
        date_time_str = dob
        date_time_obj = datetime.datetime.strptime(date_time_str, '%d-%b-%y')
        given = date_time_obj.strftime('%y')
        if int(given) < max_year:
        	finalyear = int(given) + 2000
        else:
        	finalyear = int(given) + 1900
        final_date = date_time_obj.strftime('{0}/%b/%d'.format(finalyear))
        return final_date


    def nid_login(self,browser):

        browser.get(definitions.BEC_URL)
        print("going to the nid website")
        #browser.find_element_by_xpath(r'//*[@id="wrapper"]/h3/a').click()
        #username
        browser.find_element_by_xpath(definitions.nid_usser_feild).send_keys(definitions.nid_user)
        #password
        browser.find_element_by_xpath(r'//*[@id="pt1:password::content"]').send_keys(definitions.nid_pass)
        #login button
        browser.find_element_by_xpath(r'//*[@id="pt1:logon"]').click()

    def nid_scraper(self,nid,dob):
        browser= config.BROWSER_NID
        self.nid_login(browser)
        nid_info_dir= (definitions.OUTPUT_FOLDER+"NID")
        if not os.path.exists(nid_info_dir):
            os.mkdir(nid_info_dir)
        try:

            browser.find_element_by_xpath(definitions.nid_number).send_keys(nid.replace("'", ''))
            dob=self.format_date(dob)
            browser.find_element_by_xpath(definitions.nid_dob).send_keys(dob.replace("'", ''))
            browser.find_element_by_xpath(definitions.nid_search_button).click()
            try:
                nid_site_info = browser.find_element_by_xpath('//*[@id="pt1:i5"]')
                src = nid_site_info.get_attribute('src')
                browser.execute_script("window.open('about:blank', 'nid_info');")
                browser.switch_to.window("nid_info")
                browser.get(src)
                time.sleep(1)
                try:
                    self.get_verified_image(browser,"ocr",nid_info_dir,r'/html/body/img')
                    definitions.nid_verification_status[0].append("Verified")
                except Exception as e:
                    definitions.nid_verification_status[0].append("Verification Failed")
                    return "failed"
                browser.close()
                browser.switch_to.window(browser.window_handles[-1])
                try:
                    self.get_verified_image(browser, "nid", nid_info_dir, r'//*[@id="pt1:pgResult"]')
                except Exception as e :
                    return "failed"
            except Exception as e :
                print(traceback.format_exc())
                return e
        except Exception as e :
            print(traceback.format_exc())
            return e
        browser.quit()
        return nid_info_dir

