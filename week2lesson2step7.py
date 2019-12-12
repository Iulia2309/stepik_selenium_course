import os 
from selenium import webdriver
import time

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector("[name='firstname']")
    input1.send_keys("F")
    input2 = browser.find_element_by_css_selector("[name='lastname']")
    input2.send_keys("S")
    input3 = browser.find_element_by_css_selector("[name='email']")
    input3.send_keys("f@s.c")
    
    choose_file = browser.find_element_by_css_selector("[type='file']")
    choose_file.send_keys(file_path)

    button = browser.find_element_by_class_name('btn-primary')
    button.click() 

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
   
