from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="D://Drivers//Chrome Driver//chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(7)
action=ActionChains(driver)
action.move_to_element(driver.find_element_by_xpath("//button[@id='mousehover']")).perform()