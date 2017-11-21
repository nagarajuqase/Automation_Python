import unittest
import urllib2
import json
import time
from selenium import webdriver
class RestAPIAndUIVerification(unittest.TestCase):
    def setUp(self):
        # http://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b1b15e88fa797225412429c1c50c122a1
        self.ApiUrl = "http://api.openweathermap.org/data/2.5/weather"
        self.ApiKey = "b1b15e88fa797225412429c1c50c122a1"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        print "Current test"+self._testMethodName

    def test_weather_api_by_city_name1(self):
        """Get weather data by city name and assert on the string output"""
        driver = self.driver
        # navigate to the UI
        driver.get(self.ApiUrl + "?q=London,uk" + "&" + "APPID=" + self.ApiKey)
        time.sleep(5)
        # get the ui element
        ui_element = driver.find_element_by_tag_name("pre")
        # get the weather data
        weather_data = ui_element.text
        print weather_data
        # assert response
        self.assertTrue("London" in weather_data)

    def tearDown(self):
        # self.driver.close()
        print " ----- test is over ---------- "

if __name__ == "__main__":
    unittest.main()