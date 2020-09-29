from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    
    button = WebDriverWait(browser, 12).until( EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    )
    
    #button.click()
    
    
    
    button2 = browser.find_element_by_css_selector("button[id = 'book']")
    button2.click()
    
    #new_window = browser.window_handles[1]
    #browser.switch_to.window(new_window)
    
    #alert = browser.switch_to.alert
    #alert.accept()
    
    x_elem = browser.find_element_by_id("input_value")
    x = x_elem.text
    y = calc(x)
    
    
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    
    button2 = browser.find_element_by_xpath("//button[@type = 'submit']")
    button2.click()
    
finally:
    time.sleep(5)
    browser.quit()