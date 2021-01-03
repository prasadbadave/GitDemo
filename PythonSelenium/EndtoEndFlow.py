from selenium import webdriver

driver = webdriver.Chrome(executable_path="D://Drivers//Chrome Driver//chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(6)
# click on shop button
driver.find_element_by_link_text("Shop").click()
# //div[@class='card h-100']/div/h4/a
products = driver.find_elements_by_xpath("//div[@class='card h-100']")
for product in products:
    productname = product.find_element_by_xpath("div/h4/a").text
    #print(product.find_element_by_xpath("div/h4/a").text)
    if productname=="Blackberry":
        #add blackberry items into cart
        product.find_element_by_xpath("div/button").click()

#click on checkout button
driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()
#proceed to checkout
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
#Enter country
driver.find_element_by_xpath("//input[@id='country']").send_keys("Ind")
driver.find_element_by_link_text("India").click()
#click on purchase button
driver.find_element_by_xpath("//input[@value='Purchase']").click()
#verify text
message=driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text
assert  "Thank you! Your order" in message
driver.get_screenshot_as_file("endtoend.png")