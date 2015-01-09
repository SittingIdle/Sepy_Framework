import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


chromedriver = "E:\BeachBody\CASL\Selenium_Python"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://p90xcertificationqa.productpartners.com")
##time.sleep(15)
##driver.find_element_by_id("sign-in-drop").click()
##driver.find_element_by_link_text("SHOP").click()
for x in range(1, 30):
    element = driver.find_element_by_link_text("SHOP")
    if element.is_displayed():
        print element.is_displayed()
        if element.is_enabled():
            print element.is_enabled()
            element.click()
            break
        else :
            print 'Not enabled'
            time.sleep(1)
    else :
        time.sleep(1)
        print 'not visible'
##### Selecting a product ##################
driver.find_element_by_css_selector("div[class='prodThumb'] > a[class='viewDetail'] > img").click()

#### Selecting the size and quantity
buttonElement = driver.find_element_by_class_name("atcBtn")
if buttonElement.is_enabled == False:
    print "Pass, Add to cart button is disabled"
else:
    print "Fail, Add to cart should be disabled"

selectSize = Select(driver.find_element_by_id("attributes"))
selectSize.select_by_index(1)

selectQuanity = Select(driver.find_element_by_id("quantity"))
selectQuanity.select_by_visible_text("1")

if buttonElement.is_enabled == False:
    print "Fail, Add to cart button is disabled"
else:
    print "Fail, Add to cart is enable"
    buttonElement.click()

###### Go to View Cart and Checkout ###########
time.sleep(2)
driver.find_element_by_css_selector("a[class='btn'][href='cert-shopping-cart']").click()

##driver.find_element_by_class_name("btn checkout").click()
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='shopping-checkout'][class='btn checkout']")))
element.click()

##### Create New User ####################
def getCurrentDateTime() :
    current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
    return current_time
sEmailId = "test" + getCurrentDateTime() + "@mailinator.com"
print sEmailId
driver.find_element_by_name("email").send_keys(sEmailId)
driver.find_element_by_id("non-member-submit-track").click()

###### Enter Shipping Info for P90X ##############3
##def enterShippingInfoWithoutCountry(firstName, lastName, city, state, postalCode):
driver.find_element_by_name("firstName").send_keys("Sam")
driver.find_element_by_name("lastName").send_keys("Samlast")
driver.find_element_by_name("addressLine1").send_keys("3301 Bouleverd Extension")
driver.find_element_by_name("city").send_keys("Lincoln")

selectState = Select(driver.find_element_by_name("stateId"))
selectState.select_by_visible_text("Nebraska")

driver.find_element_by_name("zipCode").send_keys("68502")
##    return True

##    enterShippingInfoWithoutCountry("Sam", "Sobi", "Santa Monica", "California", "90404")
##    print "executed the funtion"
    
    

##wait = WebDriverWait(driver, 10)
##element = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Shop")))
##element.click()
#try:
#   element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "Shop")))

#driver.find_element_by_link_text("Shop").click()

    
