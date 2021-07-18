import os

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By

login = 'ВАШ_ЛОГИН'
password = 'ВАШ_ПАРОЛЬ'

url = 'https://esia.gosuslugi.ru/'


def main():
    driver = webdriver.Chrome(executable_path='chromedriver')

    driver.get("https://esia.gosuslugi.ru")

    w_login = driver.find_element(By.ID, "login")
    w_password = driver.find_element(By.ID, "password")
    enter = driver.find_element(By.ID, "loginByPwdButton")

    w_login.send_keys(login)
    w_password.send_keys(password)
    enter.click()

    driver.get_cookies()
    content = driver.find_element_by_css_selector('div.content-box')

    try:
        os.mkdir('Profile')
    except OSError:
        pass

    with open('Profile/profile.html', 'w+') as f:
        bs = BeautifulSoup(content.get_attribute('innerHTML'), 'lxml')
        rows = bs.find_all('div', {'class': 'row'})
        for row in rows:
            try:
                dd = row.find_all('div')
                if 'Паспорт' in dd[1].text:
                    f.write(dd[1].text)
            except:
                pass


if __name__ == '__main__':
    main()
