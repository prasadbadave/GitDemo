import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome(executable_path="D://Drivers//Chrome Driver//chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(6)
#Enter value in search box
driver.find_element_by_xpath("//input[@type='search']").send_keys("ber")
time.sleep(4)
count=len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count==3
buttons=driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:
    button.click()

#Click on cart icon
driver.find_element_by_xpath("//a[@class='cart-icon']").click()
time.sleep(3)
#click on proceed to checkout
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

#to check total amount
amounts=driver.find_elements_by_xpath("//tr/td[5]/p")
sum=0
for amt in amounts:
    sum = sum + int(amt.text)

print("Total amount is:",sum)

#enter promocode

#wait=WebDriverWait(driver,5)
#wait.until(expected_conditions.presence_of_element_located((By.Class_name,"promocode")))'''

originalamount=driver.find_element_by_css_selector(".discountAmt").text
print(originalamount)
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
#click on apply
driver.find_element_by_xpath("//button[text()='Apply']").click()
time.sleep(5)
discountedamount=driver.find_element_by_css_selector(".discountAmt").text
print(discountedamount)

assert originalamount>discountedamount
#click on place order
driver.find_element_by_xpath("//button[text()='Place Order']").click()


#driver.close()