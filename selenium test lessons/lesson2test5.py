import time
from selenium import webdriver
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element_by_css_selector("button[type = 'submit']")
    button.click()
    
    alert = browser.switch_to.alert
    alert.accept()
    
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