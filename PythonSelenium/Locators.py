from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path="D://Drivers//Chrome Driver//chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("Prasad Badave")
driver.find_element_by_name("email").send_keys("prbadave@gmail.com")
#driver.find_element_by_id("exampleInputPassword1").send_keys("Kavya@2218")
driver.find_element_by_css_selector("input[id='exampleInputPassword1']").send_keys("Kavya@2218")

#click on checkbox
driver.find_element_by_id("exampleCheck1").click()
#select value from dropdown
dropdown=Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_index(1)

#Click on button
driver.find_element_by_xpath("//input[@type='submit']").click()
message=driver.find_element_by_class_name("alert-success").text
assert "succesffs" in message


#driver.close()