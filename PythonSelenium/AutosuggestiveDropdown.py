import time

from selenium import webdriver

driver=webdriver.Chrome(executable_path="D://Drivers//Chrome Driver//chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element_by_xpath("//input[@id='autocomplete']").send_keys("Ind")
time.sleep(2)
countries=driver.find_elements_by_css_selector("li[class='ui-menu-item'] div")
print(len(countries))
for country in countries:
    print(country.text)
    if country.text=="India":
        country.click()
