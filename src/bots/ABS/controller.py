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
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import config
import definitions
import .utils as utils
import shutil
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
# Customer document info 
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


    def get_customer_info(self,xpath,browser):
        table_id = browser.find_element(By.XPATH, xpath)
        rows = table_id.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            try:
                customer_name_feild = row.find_elements(By.TAG_NAME, "td")[1]
                definitions.customer_name_arr[0].append(customer_name_feild.get_attribute('innerHTML'))
            except:
                definitions.customer_name_arr[0].append("None")
            try:
                customer_id_feild = row.find_elements(By.TAG_NAME, "td")[0]
                definitions.customer_id_arr[0].append(customer_id_feild.get_attribute('innerHTML'))
            except:
                definitions.customer_id_arr[0].append("None")
            try:
                customer_dob_feild = row.find_elements(By.TAG_NAME, "td")[2]
                definitions.customer_dob_arr[0].append(customer_dob_feild.get_attribute('innerHTML'))
            except:
                definitions.customer_dob_arr[0].append("None")
            
            try:
                customer_url_feild = row.find_elements(By.TAG_NAME, "td")[3]
                url_str=customer_url_feild.get_attribute('innerHTML')
                url_str=url_str.split(" ")
                definitions.customer_url_arr[0].append((url_str[1].split('"')[1]))
            except:
                definitions.customer_url_arr[0].append("None")



    def insert_joined_info_to_arr(self,browser,doc_type_arr,doc_number_arr,abs_doc_image_arr,doc_type_xpath):
        try:
            document_type_str = self.get_docnumber_from_table(browser, doc_type_xpath)
            if document_type_str != None:
                try:
                    definitions.document_type_arr[0].append(document_type_str["type"])
                except:
                    definitions.document_type_arr[0].append("None")
                try:
                    document_no_arr[0].append(document_type_str["number"])
                except:
                    definitions.document_no_arr[0].append("None")
                try:
                    document_image_arr[0].append(document_type_str["doc_image"])
                    
                except:
                    definitions.document_image_arr[0].append('None')
            else:
                raise Exception("None type in nid number")
        except Exception as e:
            print(traceback.format_exc())







    def insert_text_to_array(self,browser,field_arr,field_name,field_xpath):
        field_str = 'field name not found'
        try:
            field = browser.find_element_by_xpath(field_xpath)
            field_str=field.text
            print(field_str)
            if len(field_str.replace(" ", "")) != 0:
                field_arr.append(field_str)
                print(field_arr)
            else:
                field_arr.append("None")
                print(field_arr)
                raise Exception("{0} is not given".format(field_name))
        except Exception as e:
            print(traceback.format_exc())
            print(field_arr)
            field_arr.append("None ")
        return field_str


    def get_joined_acnt_info(self,browser,main_account_doc_table,sec_account_doc_table,cutomer_url_arr):
        count=0
        for items in cutomer_url_arr:
            browser.get(items)
            browser.save_screenshot("{0}.png".format(count))
            count+=1
            try:
                browser.find_element_by_xpath(main_account_doc_table)
                self.get_docnumdber_from_table(browser, main_account_doc_table)
            except:
                self.get_docnumber_from_table(browser, sec_account_doc_table)
            try:
                submit = browser.find_element_by_xpath(definitions.bacKbutton)
                browser.execute_script("arguments[0].click();", submit)
            except:
                continue



    def download_doc_img(self,browser,path, image_array, image_field, dirname, directory, account_number,src):
        try:
            browser.get(str(src))
            time.sleep(1)
            exists = False
            while exists == False:
                if os.path.exists(path + '/download'):
                    shutil.move(path + "/download",
                                os.path.join(dirname, directory.format(account_number)))
                    exists = True
            image_array.append(os.path.join(dirname, directory.format(account_number)))
        except Exception as e:
            print(traceback.format_exc())
            image_array.append("No {0}".format(image_field))


    def get_image_data(self,browser,path, image_array, image_field, dirname, directory, account_number, image_xpath):
        try:
            image = browser.find_element_by_xpath(image_xpath)
            if image:
                src = image.get_attribute('src')
                browser.get(src)
                time.sleep(1)
                exists = False
                while exists == False:
                    if os.path.exists(path + '/download'):
                        shutil.move(path + "/download",
                                    os.path.join(dirname, directory.format(account_number)))
                        exists = True
                image_array.append(os.path.join(dirname, directory.format(account_number)))
        except Exception as e:
            print(traceback.format_exc())
            image_array.append("No {0}".format(image_field))



    def get_detail_info(self,number_of_entries, browser, path):
        browser.switch_to.window(browser.window_handles[0])

        try:
            default_url = browser.current_url
            browser.get(default_url)
        except:
            print(traceback.format_exc())


        dirname=definitions.TEMP_FOLDER

        if os.path.exists(os.path.join(dirname, "temp_data")):
            shutil.rmtree(os.path.join(dirname, "temp_data"))

        utils.creating_folders(dirname)

        table_id = browser.find_element(By.XPATH,definitions.verification_list_table)
        rows = table_id.find_elements(By.TAG_NAME, "tr")  # get all of the rows in the table
        url_count=0

        for row in rows:
            try:
                attr = row.find_elements(By.TAG_NAME, "td")[9]
                # print(attr)# account type column index
                accnt_type = attr.get_attribute('innerHTML')
                print(accnt_type)
                if (accnt_type == "Individual") or (accnt_type == "UDC"):
                    col = row.find_elements(By.TAG_NAME, "td")[-1]  # note: index start from 0, 1 is col 2
                    link = col.get_attribute('innerHTML')
                    link = link.split('"')[1]
                    definitions.urls.append(link)
                    url_count += 1 # take only 5 entries
                #TODO add institution check, add remarks, need change, submit
                elif (accnt_type != "Individual") and (accnt_type != "UDC"):
                    remarks_field = browser.find_element_by_xpath(definitions.remarks_field)
                    remarks_field.send_keys(f'{accnt_type}. Bot will not check it')
                    need_change = browser.find_element_by_xpath(definitions.need_change)
                    browser.execute_script("arguments[0].click();", need_change)
                    submit = browser.find_element_by_xpath(definitions.submit)
                    browser.execute_script("arguments[0].click();", submit)
                if url_count == (number_of_entries+1):
                    break
            except Exception as e:
                print(traceback.format_exc())
        browser.execute_script("window.open('about:blank', 'details');")
        browser.switch_to.window("details")
        for item in definitions.urls:
            browser.get(definitions.domain + item)
            account_type_str=self.insert_text_to_array(browser, definitions.acnt_type_arr, 'account_type', definitions.account_type)
            print("account type str ",account_type_str)
            print("reached here")
            if ("Joint" not in account_type_str) and ("Single" not in account_type_str):
                print("in if")
                try:
                    browser.switch_to.window(browser.window_handles[0])
                    remarks_field = browser.find_element_by_xpath('//*[@id="f02_0001"]')
                    remarks_field.send_keys(f'{account_type_str}. Bot will not check it')
                    need_change = browser.find_element_by_xpath(r'//*[@id="f03_0001_0001"]')
                    browser.execute_script("arguments[0].click();", need_change)
                    submit = browser.find_element_by_xpath(r'//*[@id="B35815888295108623"]/span')
                    browser.execute_script("arguments[0].click();", submit)
                    return None   
                except:
                    print(traceback.format_exc())
            else:
                print("in else")
                acnt_no_str=self.insert_text_to_array(browser, definitions.acnt_no_arr,definitions.acnt_no)

                self.get_customer_info(definitions.customer_table_xpath,browser)

                self.insert_text_to_array(browser, definitions.acnt_title_arr, 'acnt_title', definitions.acnt_title)


                self.insert_text_to_array(browser, definitions.agent_boothname_arr, 'agent_boothname', definitions.agent_boothname)


                self.insert_text_to_array(browser, definitions.sector_code_arr, 'sector_code', definitions.sector_code)

                self.insert_text_to_array(browser, definitions.aml_status_arr, 'aml_status', definitions.aml_status)

                # personal Info
                self.insert_text_to_array(browser, definitions.name_arr, 'name', definitions.name)

                self.insert_text_to_array(browser, definitions.gender_arr, 'gender', definitions.gender)

                self.insert_text_to_array(browser, definitions.occupation_arr, 'occupation',definitions.occupation)

                self.insert_text_to_array(browser, definitions.father_name_arr, 'father_name', definitions.father_name)


                self.insert_text_to_array(browser, definitions.mother_name_arr, 'mother_name', definitions.mother_name)

                self.insert_text_to_array(browser, definitions.maritual_status_arr, 'maritual_status', definitions.maritual_status)

                self.insert_text_to_array(browser, definitions.spouse_name_arr, 'spouse_name', definitions.spouse_name)


                # Contact Info

                self.insert_text_to_array(browser, definitions.mobile_no_arr, 'mobile_no', definitions.mobile_no)

                self.insert_text_to_array(browser, definitions.mail_id_arr, 'mail_id', definitions.mail_id)

                #document_ Info
                self.get_joined_acnt_info(definitions.customer_main_doc_table,definitions.customer_sec_doc_table)



                self.insert_text_to_array(browser, definitions.perm_district_arr, 'perm_district',definitions.perm_district)

                self.insert_text_to_array(browser, definitions.perm_upazila_arr, 'perm_upazila',definitions.perm_upazila)

                self.insert_text_to_array(browser, definitions.perm_union_arr, 'perm_union',definitions.perm_union)


                self.insert_text_to_array(browser, definitions.perm_village_arr, 'perm_village',definitions.perm_village)


                self.insert_text_to_array(browser, definitions.pres_district_arr, 'pres_district',definitions.pres_district)



                self.insert_text_to_array(browser, definitions.pres_upazila_arr, 'pres_upazila',definitions.pres_upazila)

                self.insert_text_to_array(browser, definitions.pres_union_arr, 'pres_union',definitions.pres_union)


                self.insert_text_to_array(browser, definitions.pres_village_arr, 'pres_village',definitions.pres_village)


                # Nominee Info

                self.insert_text_to_array(browser, definitions.nom_name_arr, 'nom_name',definitions.nom_name)

                self.insert_text_to_array(browser, definitions.nom_father_arr, 'nom_father',definitions.nom_father)

                self.insert_text_to_array(browser, definitions.nom_mother_arr, 'nom_mother',definitions.nom_mother)


                self.insert_text_to_array(browser, definitions.nom_dob_arr, 'nom_dob',definitions.nom_dob)

                self.insert_text_to_array(browser, definitions.nom_rel_arr, 'nom_rel',definitions.nom_rel)

                self.insert_text_to_array(browser, definitions.nom_percent_arr, 'nom_percent',definitions.nom_percent)


                self.insert_text_to_array(browser, definitions.nom_doc_type_arr, 'nom_doc_type',definitions.nom_doc_type)

                self.insert_text_to_array(browser, definitions.nom_doc_no_arr, 'nom_doc_no',definitions.nom_doc_no)


                try:
                    nom_img = browser.find_element_by_xpath(definitions.nom_front_pic)
                    # check if nominee image is present or not
                    if nom_img:
                        definitions.nom_img_arr.append("present")       

                    nom_frnt = browser.find_element_by_xpath(definitions.nom_doc_frnt)
                    if nom_frnt:
                        definitions.nom_frnt_arr.append("present")

                    nom_bck = browser.find_element_by_xpath(definitions.nom_doc_bck)
                    if nom_bck:
                        definitions.nom_bck_arr.append("present")

                except:
                    definitions.nom_img_arr.append("not_present")
                    definitions.nom_frnt_arr.append("not_present")
                    definitions.nom_bck_arr.append("not_present")


#fix download folder
                self.get_image_data(browser, path, definitions.live_pic_path, "live picture", dirname, r"temp_data/live_pic/{0}live_pic_test.jpg",
                        acnt_no_str, definitions.live_picture)

                self.get_image_data(browser, path, definitions.signcard_pic_path, "Sign picture", dirname, r"temp_data/sign_Card/{0}sign_pic.jpg",
                        acnt_no_str, definitions.Sign_picture)
                self.get_image_data(browser, path, definitions.nom_image_path, "Nominee pic", dirname,  r"temp_data/nom_img/{0}nom_img.jpg",
                        acnt_no_str, definitions.nom_front_pic)


                

