from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #button = browser.find_element(By.TAG_NAME, "button")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    #button.click()

    button1 = browser.find_element(By.ID, "book")
    button2 = WebDriverWait(browser, 5).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button1.click()



    # new_window = browser.window_handles[1]
    # browser.switch_to.window(new_window)
    ##confirm = browser.switch_to.alert
    ##confirm.accept()

    # input1 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter first name']")
    # input1.send_keys("Ivan")
    # input2 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter last name']")
    # input2.send_keys("Ivanov")
    # input3 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter email']")
    # input3.send_keys("ivanov@mail.com")
    #
    # current_dir = os.path.abspath(os.path.dirname(__file__))
    # file_name = "file.txt"
    # file_path = os.path.join(current_dir, file_name)
    # element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    # element.send_keys(file_path)
    browser.execute_script("return arguments[0].scrollIntoView(true);", button1)
    input3 = browser.find_element(By. ID, "input_value")
    x = input3.text
    y = calc(x)

    input4 = browser.find_element(By.CSS_SELECTOR, ".form-control")
    input4.send_keys(y)

    #e_element = browser.find_element(By.ID, "robotCheckbox")
    #e_element.click()
    #
    #a_element = browser.find_element(By.ID, "robotsRule")
    #a_element.click()
    # input2 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
    # input2.send_keys("Vasnetsov")
    # input3 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email'")
    # input3.send_keys("testmail@mail.cm")
    # # Отправляем заполненную форму

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()
    #
    # # Проверяем, что смогли зарегистрироваться
    # # ждем загрузки страницы
    time.sleep(1)
    #
    # # находим элемент, содержащий текст
    # welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # # записываем в переменную welcome_text текст из элемента welcome_text_elt
    # welcome_text = welcome_text_elt.text
    #
    # # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    # assert "Congratulations! You have successfully registered!" == welcome_text
    # alert = browser.switch_to.alert
    # alert_text = alert.text
    # print(alert_text)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()