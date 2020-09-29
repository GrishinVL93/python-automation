from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math



def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_elem = browser.find_element_by_id("num1")
    x = x_elem.text
    
    y_elem = browser.find_element_by_id("num2")
    y = y_elem.text
    sum = int(x) + int(y)
    
    
    select = Select(browser.find_element_by_id("dropdown"))
    
    select.select_by_value(str(sum))
    

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()