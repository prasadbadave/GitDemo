import time

from selenium import webdriver

driver=webdriver.Chrome(executable_path="D://Drivers//Chrome Driver//chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes=driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(checkboxes))
for checkbox in checkboxes:
    checkbox.click()
    #time.sleep(10)
    assert checkbox.is_selected()



    #driver.close()