import unittest
from selenium import webdriver


class AutoComplete(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test(self):
        driver = self.driver
        driver.implicitly_wait(20)
        driver.get("http://jqueryui.com/autocomplete/")
        frames = driver.find_element_by_tag_name("iframe")
        driver.switch_to.frame(frames)
        input_field = driver.find_element_by_id("tags")
        input_field.send_keys("j")
        driver.find_element_by_css_selector("#ui-id-1 > li:nth-child(2)").click()
        input_text = input_field.get_attribute("value")
        self.assertEqual(input_text, 'Java', 'Expected and Actual is same')

