from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)    

    input_y = browser.find_element_by_id('answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_y)
    input_y.send_keys(y)

    check_robot = browser.find_element_by_id('robotCheckbox')
    browser.execute_script("return arguments[0].scrollIntoView(true);", check_robot)
    check_robot.click()

    option_robot = browser.find_element_by_id('robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", option_robot)
    option_robot.click()

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
