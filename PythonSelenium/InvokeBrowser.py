from selenium import webdriver

driver = webdriver.Firefox(executable_path="D://Drivers//Firefox Driver//geckodriver.exe")#for firefox driver
# For ChromeDriver
#driver = webdriver.Chrome(executable_path="D://Drivers//Chrome Driver//chromedriver.exe")
# for IE driver
#driver=webdriver.Ie(executable_path="D://Drivers//IE Driver//IEDriverServer.exe")
#driver = webdriver.Chrome(executable_path="D://Drivers//Chrome Driver//chromedriver.exe")
driver.get("https://rahulshettyacademy.com/#/index")
driver.maximize_window()
driver.back()
driver.refresh()
driver.minimize_window()
print(driver.title)
print(driver.current_url)
#print(driver.get_screenshot_as_png("D://"))
#open in firefox browser





driver.close()
