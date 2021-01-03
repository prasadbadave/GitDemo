import time

from selenium import webdriver

driver=webdriver.Chrome(executable_path="D://Drivers//Chrome Driver//chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
validatetext="Prasad"
#Enter name in texbox
driver.find_element_by_id("name").send_keys(validatetext)
time.sleep(3)
#click on alert
driver.find_element_by_xpath("//input[@id='alertbtn']").click()
alert=driver.switch_to.alert
print(alert.text)
assert validatetext in alert
alert.accept()
