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
import os
sys.path.append("...") # Adds higher directory to python modules path.

import config
import definitions
import utils.utils
import time
import traceback

class abs:

    def logging_to_abs(self, browser,username,password,captcha):
        inputXPath = definitions.input_captcha_XPath
        browser.find_element_by_xpath(definitions.log_in_user).send_keys(str(username))
        browser.find_element_by_xpath(definitions.log_in_psw).send_keys(str(password))
        browser.find_element_by_xpath(inputXPath).send_keys(str(captcha))
        browser.save_screenshot("login.png")
        login=browser.find_element_by_xpath(definitions.login_button)
        browser.execute_script("arguments[0].click();", login)

    def login_process(self, browser):
        browser = utils.driver()
        try:
            browser.get(definitions.abs_url)
            browser.maximize_window()
            log_in_user = definitions.log_in_user
            log_in_psw = definitions.log_in_psw
            captcha = ''
            SITE_ROOT = os.path.dirname(os.path.realpath(__name__))
            captchaFile = os.path.join(SITE_ROOT, "bank_asia_bots/captcha.txt")
            if os.path.exists(captchaFile):
                with open(captchaFile, 'r') as f:
                    captcha = f.read()
                    captcha_txt=captcha.split("\n")[0]
                    username_txt=captcha.split("\n")[1]
                    password_txt=captcha.split("\n")[2]
                    print(captcha_txt,'   ',username_txt,'  ',password_txt)
                    f.close()
                self.logging_to_abs(browser,username_txt,password_txt,captcha_txt)
                time.sleep(3)
                dirname = os.path.dirname(__file__)
                CUSTOM_DIR_NAME = 'captcha'
                captcha_dir= os.path.join(dirname, CUSTOM_DIR_NAME)
                utils.getScreenshot(browser, "checkPOST", captcha_dir)
                os.remove(captchaFile)
                print(captcha)
            else:
                raise Exception('captcha not found!!')
        except Exception as inst:
            print(traceback.format_exc())
            time.sleep(1)
        return browser

        
    def goingto_verification_page(self, browser):
        try:
            cards=browser.find_element_by_xpath(definitions.agent_banking_card)
            browser.execute_script("arguments[0].click();", cards)
        except Exception as e:
            print(traceback.format_exc())
        try:
            jqmenu=browser.find_element_by_xpath(definitions.top_menu)
            browser.execute_script("arguments[0].click();", jqmenu)
            time.sleep(1)
        except:
            print(traceback.format_exc())
        account_aproval = definitions.account_aproval
        verification = definitions.verification
        try:
            utils.hovering_to_options(account_aproval,browser)
            utils.hovering_to_options(verification,browser)
        except Exception as e:
            print(traceback.format_exc())
        return browser

    def run(self, browser):
        try:
            while True:
                acnt_no = ' '
                try:
                    if browser.find_element_by_xpath(definitions.no_more_entries):
                        print ("Element exists")
                        browser.quit()
                        break
                except:
                    print(traceback.format_exc())
                try:
                    res=get_info(number_of_entries, browser, path)
                    if res == None:
                        continue
                    df = res['df']
                    acnt_no = res['acnt_no']
                    print(df)
                    checks_browser=doings_checks(df, browser)
                    dispatch(checks_browser, number_of_entries)
                    print(i, "iiiiiiiiiiiiiiiiiiiiii")
                except:
                    print(traceback.format_exc())
                    continue
            raise Exception('Closing browser')
        except Exception as e:
            print(traceback.format_exc())
            # gettinglogs("Something went wrong please check", False)
            browser.quit()

    def get_docnumber_from_table(self, browser, xpath):
        # gets document number from the table , will only take NID number
        try:
            table_id = browser.find_element(By.XPATH, xpath)
            rows = table_id.find_elements(By.TAG_NAME, "tr")
            for row in rows:       
                attr = row.find_elements(By.TAG_NAME, "td")[0]
                document_number = row.find_elements(By.TAG_NAME, "td")[1]
                attr_type = attr.get_attribute('innerHTML')
                doc_image=row.find_elements(By.TAG_NAME, "img")[0]
                print(doc_image)
                doc_image= doc_image.get_attribute("src")
                print("doc_imdoc_imagedoc_imagedoc_imagedoc_imagedoc_imagedoc_imageagedoc_image",doc_image)


                if"national" in attr_type.lower():
                    print("if", attr_type)

                    context = {"type": attr_type, "number": document_number.get_attribute('innerHTML'),"doc_image":doc_image}
                    print(context)
                    return context
                else:
                    print("else",attr_type)
        except Exception as e:
            print(traceback.format_exc())
            return None
