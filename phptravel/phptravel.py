from selenium import webdriver
import os
import phptravel.constants as const
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Phptravel(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\Program Files (x86)"):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Phptravel, self).__init__()
    
    def go_first_page(self):
        self.get(const.BASE_URL)
