from selenium import webdriver

driver=webdriver.Chrome(executable_path="D://Drivers//Chrome Driver//chromedriver.exe")
driver.get("https://login.salesforce.com/?locale=in")
driver.minimize_window()
driver.find_element_by_css_selector("input#username").send_keys("prbadave")
driver.find_element_by_css_selector("input#password").send_keys("34543")
#find element by visible text
driver.find_element_by_xpath("//a[text()='Try for Free']").click()
#driver.find_element_by_xpath("//input[@id='Login']").click()