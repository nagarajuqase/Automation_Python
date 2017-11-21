from selenium import webdriver
from selenium.webdriver import ActionChains
driver = webdriver.Chrome("D:\\Lib\\chromedriver.exe")
# driver=webdriver.Firefox(executable_path="D:\\Lib\\geckodriver.exe")
# driver = webdriver.Ie("D:\\Lib\\IEDriverServer.exe")
# driver.set_page_load_timeout(10)
#driver.implicitly_wait(20)
driver.get("https://www.facebook.com/")
# Browser version
print(driver.capabilities['version'])
driver.maximize_window()
driver.find_element_by_id("email").send_keys("Username")
driver.find_element_by_id("pass").send_keys("password")
driver.find_element_by_xpath("//button[text()='Log In']").click()
hover = ActionChains.move_to_element()
driver.get_screenshot_as_file("facebook2.png")
driver.close()
