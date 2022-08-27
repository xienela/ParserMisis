"""
    Код должен парсить элементы с сайта, который получает HTML шаблон с сервера, реализованный
с помощью JavaScript.

    Используется библиотека Selenium, предназначенная для автоматизации действий в веб-браузере,
а также для выполнения рутинных задач и тестирования Web-приложений
    (Установка Selenium: pip3 install selenium)

    Для работы с данной библиотекой используется WebDriver, необходимый для эмуляции обычного браузера,
который будет управляться через Selenium.
    (Мой браузер - Chrome, поэтому я устанавливаю ChromeDriver - https://chromedriver.chromium.org/downloads)
    Версия Chrome должна совпадать с версией ChromeDriver.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("D:\\Education\\Web\\untitled9\\chromedriver.exe")


def existence_check(num, path_elem):
    try:
        driver.find_element(By.XPATH, path_elem + "tr[%s]/td[2]" % (num + 1))
        return True
    except:
        return False


def collection_results():
    path_elem = "/html[@class='ru detect_flexbox']" \
                "/body[@class='inner-page ranged-list']" \
                "/div[@class='layout']/div[@class='wrapper']" \
                "/div[@id='js-content']/div[@class='wide']" \
                "/div[@class='data-table-container mCustomScrollbar _mCS_1']" \
                "/div[@id='mCSB_1']/div[@id='mCSB_1_container']" \
                "/div[@class='table-container']/table[@class='data with-hover sortable js-fixed js-table-data']" \
                "/tbody/"
    num = 0
    reg_numbers = list()
    sum_points = list()
    accept = list()
    orig = list()

    while existence_check(num, path_elem):
        reg_numbers.append(driver.find_element(By.XPATH, path_elem + "tr[%s]/td[2]" % (num + 1)).text)
        sum_points.append(driver.find_element(By.XPATH, path_elem + "tr[%s]/td[4]" % (num + 1)).text)
        accept.append(driver.find_element(By.XPATH, path_elem + "tr[%s]/td[7]" % (num + 1)).text)
        orig.append(driver.find_element(By.XPATH, path_elem + "tr[%s]/td[8]" % (num + 1)).text)
        num = num + 1

    dic = {}
    for i in range(len(reg_numbers)):
        if accept[i] == "+" and orig[i] == "+":
            dic[reg_numbers[i]] = sum_points[i]

    return dic


def print_result(dic):
    i = 0
    print("---Проходят на бюджет:---")
    for key,value in dic.items():
        i += 1
        if i > count_budget_places:
            break
        else:
            print(str(i) + ". " + key + " " + value)

    print("Количество непрошедших: " + str(len(dic) - count_budget_places))


def main():
    global count_budget_places, driver
    url = input("Ссылка на ранжированный список: ")

    try:
        driver = webdriver.Chrome(service=s)
        driver.get(url=url)
        print(driver.find_element(By.XPATH, "/html[@class='ru detect_flexbox']/body[@class='inner-page ranged-list']"
                                            "/div[@class='layout']/div[@class='wrapper']/div[@id='js-content']/div[@class='col-sm-4 col-md-2']/div[@class='data data-indent'][2]/div[@class='row'][3]/div[@class='col-md-2 col-sm-2 col-xs-4'][2]/direction").text)
        count_budget_places = int(driver.find_element(By.XPATH, "/html[@class='ru detect_flexbox']"
                                                        "/body[@class='inner-page ranged-list']"
                                                        "/div[@class='layout']/div[@class='wrapper']/div[@id='js-content']"
                                                        "/div[@class='col-sm-4 col-md-2']/div[@class='data data-indent'][2]"
                                                        "/div[@class='row'][1]/div[@class='col-md-2 col-sm-2 col-xs-4'][2]").text)
    finally:
        print_result(collection_results())
        driver.close()
        driver.quit()


main()
