from selenium.webdriver.common.by import By
import datetime
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from django.test import TestCase
# Create your tests here.

class AutenticationTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=options)

        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('http://127.0.0.1:8000/')
        username = self.driver.find_element(by=By.NAME,value='username')
        username.send_keys('toni')
        password = self.driver.find_element(by=By.NAME,value='password')
        password.send_keys('1234')
        submit = self.driver.find_element(by=By.CLASS_NAME,value='btn-info')
        submit.submit()
        self.logs = open('logs.txt', mode='a')


    def test_form(self):
        if value := '' in self.driver.page_source:
            self.logs.write(f"{value}, {datetime.datetime.now()}\n")
        assert value