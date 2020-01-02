#user import
import definitions
import config
#system import
import time
from selenium.webdriver.common.action_chains import ActionChains
import os
from PIL import Image
from io import BytesIO

import cv2

class utils:


    def __init__(self):
        pass

    #BOTs
    def get_captcha(self, browser,type_image,directory,xpath):
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
        # sendCaptchaReceived("success")
    
    def driver(self):
        today_date=config.TODAY_DATE
        if not os.path.exists(today_date):
            os.makedirs(today_date)
        browser =  config.BROWSER
        # SELENIUM_GRID_URL = "http://selenium-hub:4444/wd/hub"
        # CAPABILITIES = DesiredCapabilities.CHROME.copy()
        # browser = webdriver.Remote(desired_capabilities=CAPABILITIES,
        #command_executor=SELENIUM_GRID_URL)
        browser.implicitly_wait(60)
        return browser

    def creating_folders(self, dirname):
        # create folders to save the data  and data folder
        for items in definitions.folders:
            print(os.path.join(dirname, items))
            os.mkdir(os.path.join(dirname, items))


    #ABS
    def hovering_to_options(self, xpath,browser):
        element_to_hover_over = browser.find_element_by_xpath(xpath)
        if xpath == definitions.verification:
            hover = ActionChains(browser).move_to_element(element_to_hover_over).click()
        else:
            hover = ActionChains(browser).move_to_element(element_to_hover_over)
        hover.perform()
        time.sleep(1)
    
    def getScreenshot(self, browser,type_image,directory):
        # now that we have the preliminary stuff out of the way time to get that image :D
        # element = browser.find_element_by_xpath(xpath) # find part of the page you want image of
        png = browser.get_screenshot_as_png() 
        # saves screenshot of entire page
        im = Image.open(BytesIO(png)) 
        # uses PIL library to open image in memory
        im.save(r"{0}/{1}.png".format(directory, type_image)) # saves new cropped image
        # sendCaptchaReceived("success")

    def getCaptchaAndSend(self, browser):
        dirname = os.path.dirname(__file__)
        CUSTOM_DIR_NAME = 'captcha'
        captcha_dir= os.path.join(dirname, CUSTOM_DIR_NAME)
        self.get_captcha(browser, "captcha", captcha_dir, definitions.captchaXPath)

    #verification list page
    def vconcat_resize_min(self, im_list, interpolation=cv2.INTER_CUBIC):
        # Concatanating two image vertically
        w_min = min(im.shape[1] for im in im_list)
        im_list_resize = [
            cv2.resize(im, (w_min, int(im.shape[0] * w_min / im.shape[1])), interpolation=interpolation)
            for im in im_list]
        return cv2.vconcat(im_list_resize)

    #DOCS
