from selenium import webdriver

driver=webdriver.Chrome(executable_path="D://Drivers//Chrome Driver//chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(7)
driver.find_element_by_xpath("//input[@name='name']").send_keys("Hello Prasad")
print(driver.find_element_by_xpath("//input[@name='name']").text)
#print entered text by javascript executer
print(driver.find_element_by_xpath("//input[@name='name']").get_attribute("value"))
print(driver.execute_script('return document.getElementsByName("name")[0].value'))

shopbutton=driver.find_element_by_link_text("Shop")
driver.execute_script("arguments[0].click();",shopbutton)
