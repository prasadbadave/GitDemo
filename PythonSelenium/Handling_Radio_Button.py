from selenium import webdriver

driver=webdriver.Chrome(executable_path="D://Drivers//Chrome Driver//chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
RadioButton=driver.find_elements_by_xpath("//input[@name='radioButton']")
RadioButton[2].click()