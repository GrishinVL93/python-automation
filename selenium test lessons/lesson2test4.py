from selenium import webdriver
import time
import math
import os


try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector("[name = 'firstname']")
    input1.send_keys("Ivan")
    
    input2 = browser.find_element_by_css_selector("[name = 'lastname']")
    input2.send_keys("Ivanov")
    
    input3 =  browser.find_element_by_css_selector("[name = 'email']")
    input3.send_keys("ivani@mail.ru")
    
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 

    loadf = browser.find_element_by_xpath("//input[@type='file']")
    loadf.send_keys(file_path)
    
    
    button = browser.find_element_by_xpath("//button[@type = 'submit']")
    button.click()
    
    
    



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()