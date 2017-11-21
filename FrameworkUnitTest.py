import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import urllib2

class DemoFBLogin(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome("D:\\Lib\\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def setUp(self):
        driver = self.driver
        driver.get("http://automationpractice.com/")
        driver.find_element_by_link_text("Sign in").click()
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("rajuvallabha@gmail.com")
        driver.find_element_by_id("passwd").clear()
        driver.find_element_by_id("passwd").send_keys("149162536")
        driver.find_element_by_id("SubmitLogin").click()

    def test_myAddresses(self):
        driver = self.driver
        driver.find_element_by_link_text("My addresses").click()

    def tearDown(self):
        driver = self.driver
        driver.find_element_by_link_text("Sign out").click()

    @classmethod
    def tearDownClass(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
    #suite = unittest.TestSuite()
