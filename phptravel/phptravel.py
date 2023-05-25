import types
import typing
from selenium import webdriver
import os
import phptravel.constants as const
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class Phptravel(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\Program Files (x86)", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Phptravel, self).__init__()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def go_first_page(self):
        self.get(const.BASE_URL)
        #self.quit
        time.sleep(5)
