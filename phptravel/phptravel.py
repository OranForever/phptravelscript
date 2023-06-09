
import types
import typing
from selenium import webdriver
import os
import phptravel.constants as const
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
import selenium.webdriver.support.expected_conditions as EC
import time


import unittest

class Phptravel(webdriver.Chrome, unittest.TestCase):

    #Initialize path of webdriver
    def __init__(self, driver_path=r"C:\Program Files (x86)", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Phptravel, self).__init__()
        self.implicitly_wait(10)
        self.maximize_window()

    #Keep Window Open
    def __exit__(self, exc_type, exc_val, exc_tb):
        time.sleep(5)
        if self.teardown:
            self.quit()
        
    #Open Website
    def go_first_page(self):
        self.get(const.BASE_URL)
        

    #find form elements
    def enter_object(username_box, text, element):
        fname_text = username_box.find_element(By.NAME, element)
        fname_text.click()
        fname_text.send_keys(text)
    
    #test form attributes
    def enter_form(self, fname, lname, bname, email):
        
        username_box = self.find_element(By.CLASS_NAME, "form")
        Phptravel.enter_object(username_box, fname, "first_name")
        Phptravel.enter_object(username_box, lname, "last_name")
        Phptravel.enter_object(username_box, bname, "business_name")
        Phptravel.enter_object(username_box, email, "email")
        num1 = username_box.find_element(By.ID, "numb1").text
        num2 = username_box.find_element(By.ID, "numb2").text
        
        
        equals = username_box.find_element(By.ID, "number")
        equals.click()
        equals.send_keys(int(num1) + int(num2))
        username_box.find_element(By.ID, "demo").click()

        checkbox = self.find_element(By.CLASS_NAME, "completed")
        if (checkbox.is_displayed()):
            print(checkbox.find_element(By.CSS_SELECTOR, "h2").text)
            formWork = self.assertIn("Thank you!", checkbox.find_element(By.CSS_SELECTOR, "h2").text)
        else:
            count = 0
            failFlag = False
            while (checkbox.is_displayed() == False):
                time.sleep(5)
                count +=1
                if (count > 3):
                    break
            try:
                self.assertIn("Thank you!", checkbox.find_element(By.CSS_SELECTOR, "h2").text)
            except:
                print("[Assertion Test] Fail")
                failFlag = True

            if (failFlag == False):
                print("[Assertion Test] Success")

    def test_Buttons(self):
        button = self.find_element(By.CLASS_NAME, "nav_left")
        print(self.title)

        
        




    

