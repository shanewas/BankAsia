# -*- coding: utf-8 -*-
"""AIW Base Framework

-*- definitions.py -*-

This module includes variable definitions for XPath Selectors and 
arrays to be used throughout the bot.

Example:
    
    The example below is what the contents of this file are expected to look like
    As aforementioned, only XPath Selectors, arrays and other static variables (to be 
    used throughout the program)::

        $ variable_name = browser.find_element_by_xpath(r'//*[@id="P826_variable_name"]')
        $ array_name = []

Creators:
    Names: Ehfaz & Shane
    Date of last edit: 23/10/2019
"""
#Your code starts from here

#Dummy XPath selectors for test run

#Login page 

import os

number_of_entries = 0


abs_url = r'http://10.88.1.174:8888/emob/f?p=106'
domain = r'http://10.88.1.174:8888/emob/'
BEC_URL = r'https://192.168.249.10/partner/'

# 

base_dir=os.getcwd()
OUTPUT_FOLDER=(base_dir,"/storage")
TEMP_FOLDER = (base_dir+"/storage")



log_in_user = r'//*[@id="P101_USERNAME"]'
log_in_psw = r'//*[@id="P101_PASS"]'
input_captcha_XPath = r'//*[@id="P101_CAPTCHA"]'
login_button= r'/html/body/form/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/table/tbody/tr/td[2]/button[1]'


#Captcha
captcha_div=r'/html/body/form/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/div[4]/div[2]/div/span'

captchaXPath = r'//*[@id="P101_CAPTCHA_CONTAINER"]/div[2]/div/span'

#Cards_page

agent_banking_card=r'//*[@id="R72507117000906705_cards"]/li[1]/div/a'

#Dropdown menu page

top_menu = r'/html/body/form/div[1]/header/a[1]'
account_aproval = r"/html/body/div[2]/div/ul/li/a"
verification = r"/html/body/div[2]/div/ul/li/ul/li[2]/a"

#Account verification List

no_more_entries = r'/html/body/form/section[2]/div[2]/span'
next_page = r'//*[@id="report_R44001444593139622"]/tbody[3]/tr/td/table/tbody/tr/td[3]/span/a[1]'



customer_table_xpath=r'//*[@id="report_R62497158322150695"]/tbody[2]/tr/td/table/tbody'

verification_list_table = r'//*[@id="report_R44001444593139622"]/tbody[2]/tr/td/table/tbody'
need_change = r'//*[@id="f03_0001_0001"]'
submit = r'//*[@id="B35815888295108623"]/span'
remarks_field= r'//*[@id="f02_0001"]'

#temp folders list
folders = ['output',"temp_data", "temp_data/cropped", "temp_data/full", "temp_data/live_pic", "temp_data/nid_back", "temp_data/nid_front", "temp_data/nom_img",'temp_data/customer2_nid_front',
        "temp_data/sign_Card", "temp_data/thresh" ]


#Details page
#_Account Info

account_type= r'//*[@id="P826_AC_NATURE"]'
acnt_no= r'//*[@id="P826_AC_NO"]'

acnt_title= r'//*[@id="P826_ACC_TITLE"]'


agent_boothname= r'//*[@id="P826_AGENT_BOOTH_NAME"]'


sector_code= r'//*[@id="P826_SECTOR_CODE"]'

aml_status= r'//*[@id="P826_AML_DISPLAY"]'

# _personal Info
name= r'//*[@id="P826_FIRST_NAME"]'

gender= r'//*[@id="P826_GENDER"]'

d_o_b= r'//*[@id="P826_CUST_DOB"]'

occupation= r'//*[@id="P826_OCCUPATION_CODE"]'

father_name= r'//*[@id="P826_FATHER_NAME"]'


mother_name= r'//*[@id="P826_MOTHER_NAME"]'

maritual_status= r'//*[@id="P826_MARITUAL_STATUS"]'

spouse_name= r'//*[@id="P826_SPOUSE_NAME"]'


# Contact Info

mobile_no= r'//*[@id="P826_MOBILE_NO"]'

mail_id= r'//*[@id="P826_MAIL_ID"]'

doc_type= r'//*[@id="report_R51601459985692709"]/tbody[2]/tr/td/table/tbody'

# joint account scenerio

customer_main_doc_table= r'//*[@id="report_R51601459985692709"]/tbody[2]/tr/td/table/tbody'
customer_sec_doc_table=r'//*[@id="report_R31874087525714563"]/tbody[2]/tr/td/table/tbody'
bacKbutton=r'//*[@id="P447_BACK_TO_PREVIOUS"]/span'



#Adress
perm_district=r'//*[@id="report_R51606549056692720"]/tbody[2]/tr/td/table/tbody/tr[1]/td[2]'
perm_upazila=r'//*[@id="report_R51606549056692720"]/tbody[2]/tr/td/table/tbody/tr[1]/td[3]' 
perm_union=r'//*[@id="report_R51606549056692720"]/tbody[2]/tr/td/table/tbody/tr[1]/td[4]'
perm_village=r'//*[@id="report_R51606549056692720"]/tbody[2]/tr/td/table/tbody/tr[1]/td[6]'
pres_district=r'//*[@id="report_R51606549056692720"]/tbody[2]/tr/td/table/tbody/tr[2]/td[2]'
pres_upazila=r'//*[@id="report_R51606549056692720"]/tbody[2]/tr/td/table/tbody/tr[2]/td[3]'
pres_union=r'//*[@id="report_R51606549056692720"]/tbody[2]/tr/td/table/tbody/tr[2]/td[4]'
pres_village=r'//*[@id="report_R51606549056692720"]/tbody[2]/tr/td/table/tbody/tr[2]/td[6]'


# Nominee Info
nom_name=r'//*[@id="report_R51682743462638959"]/tbody[2]/tr/td/table/tbody/tr/td[1]'
nom_father=r'//*[@id="report_R51682743462638959"]/tbody[2]/tr/td/table/tbody/tr/td[2]'
nom_mother=r'//*[@id="report_R51682743462638959"]/tbody[2]/tr/td/table/tbody/tr/td[3]'
nom_dob=r'//*[@id="report_R51682743462638959"]/tbody[2]/tr/td/table/tbody/tr/td[4]'
nom_rel=r'//*[@id="report_R51682743462638959"]/tbody[2]/tr/td/table/tbody/tr/td[5]'
nom_percent=r'//*[@id="report_R51682743462638959"]/tbody[2]/tr/td/table/tbody/tr/td[6]'
nom_percent=r'//*[@id="report_R51682743462638959"]/tbody[2]/tr/td/table/tbody/tr/td[6]'
nom_doc_type=r'//*[@id="report_R51682743462638959"]/tbody[2]/tr/td/table/tbody/tr/td[7]'
nom_doc_no=r'//*[@id="report_R51682743462638959"]/tbody[2]/tr/td/table/tbody/tr/td[8]'


nom_img = r'//*[@id="report_R51682743462638959"]/tbody[2]/tr/td/table/tbody/tr/td[9]/img'



nom_frnt = r'//*[@id="report_R51682743462638959"]/tbody[2]/tr/td/table/tbody/tr/td[10]/img'

nom_bck = r'//*[@id="report_R51682743462638959"]/tbody[2]/tr/td/table/tbody/tr/td[11]/img'


live_picture= r'//*[@id="report_R47260151525825765"]/tbody[2]/tr/td/table/tbody/tr/td/img'

Sign_picture= r'//*[@id="report_R40084013193953156"]/tbody[2]/tr/td/table/tbody/tr/td/img'



nom_front_pic =r'//*[@id="report_R51682743462638959"]/tbody[2]/tr/td/table/tbody/tr/td[9]/img'

nom_back_pic = r'//*[@id="report_R51682743462638959"]/tbody[2]/tr/td/table/tbody/tr/td[11]/img'



#ARRAYS


# Instantiate all the arrays as we will be  writing these arrays to a data frame
urls = []
acnt_no_arr = []
acnt_title_arr = []
acnt_type_arr = []
agent_boothname_arr = []
sector_code_arr = []
aml_status_arr = []

# Personal Info
name_arr = []
gender_arr = []
occupation_arr = []
father_name_arr = []
mother_name_arr = []
maritual_status_arr = []
spouse_name_arr = []

# Contact Info
mobile_no_arr = []
mail_id_arr = []

# Related Document
document_type_arr = [[]]
document_no_arr = [[]]
document_image_arr = [[]]


# Accouny_Operator
customer_id_arr = [[]]
customer_name_arr = [[]]
customer_dob_arr = [[]]
customer_url_arr =[[]]

# Address Details

perm_district_arr = []
perm_upazila_arr = []
perm_union_arr = []
perm_village_arr = []
pres_district_arr = []
pres_upazila_arr = []
pres_union_arr = []
pres_village_arr = []

# Nominee Info

nom_name_arr = []
nom_father_arr = []
nom_mother_arr = []
nom_dob_arr = []
nom_rel_arr = []
nom_percent_arr = []
nom_doc_type_arr = []
nom_doc_no_arr = []
nom_img_arr = []
nom_frnt_arr = []
nom_bck_arr = []

# joined acc
# customer2_id_arr=[]
# cutomer_name_arr2 = []
# cutomer_dob_arr2 = []
# customer2_doc_type = []
# customer2_doc_no = []
# customer2_nid_front_pic_path = []
# # images

live_pic_path = []
added_pic_path = []
signcard_pic_path = []
nid_front_pic_path = [[]]
nom_image_path = []