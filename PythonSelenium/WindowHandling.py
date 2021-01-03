from selenium import webdriver

driver=webdriver.Chrome(executable_path="D://Drivers//Chrome Driver//chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/windows")
driver.implicitly_wait(5)
driver.find_element_by_link_text("Click Here").click()
childwindow=driver.window_handles[1] #it will get all opened windows
#switched to child window
driver.switch_to.window(childwindow)
print(driver.find_element_by_tag_name("h3").text)
#close child window
driver.close()
parentwindow=driver.window_handles[0]
driver.switch_to.window(parentwindow)
print(driver.find_element_by_tag_name("h3").text)
#it get text from child window
