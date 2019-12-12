from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

def calc(x, y):
    return str(int(x) + int(y))

try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('num1')
    x = x_element.text
    y_element = browser.find_element_by_id('num2')
    y = y_element.text
    z = calc(x, y)

    #select = Select(browser.find_element_by_id('dropdown')
    select = Select(browser.find_element_by_tag_name("select"))                
    select.select_by_value(z) 

    button = browser.find_element_by_class_name("btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
