from selenium import webdriver

driver=webdriver.Chrome(executable_path="D://Drivers//Chrome Driver//chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/")
driver.implicitly_wait(7)
driver.find_element_by_link_text("Frames").click()

driver.find_element_by_link_text("iFrame").click()
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_xpath("//body[@id='tinymce']").clear()
driver.find_element_by_xpath("//body[@id='tinymce']").send_keys("Prasad Badave")