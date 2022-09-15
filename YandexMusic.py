from selenium import webdriver
import selenium
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import pickle


def yandex():
    EXE_PATH = r'chromedriver.exe'
    driver = webdriver.Chrome()
    action = ActionChains(driver)
    driver.get(
        'https://yandex.ru')
    sleep(1)
    element = driver.find_element('id', 'text')
    element.send_keys('dsfdsfsdf')
    sleep(1)
    action.send_keys(Keys.RETURN)
    action.perform()
    sleep(100)


def yandex_music():
    ad_id = []
    with open('ad_id.txt', 'r') as f:
        for line in f.readlines():
            ad_id.append(line[:-1])

    def login():

        try:
            for cookie in pickle.load(open('cookies', 'rb')):
                driver.add_cookie(cookie)
        except FileNotFoundError:

            element = driver.find_element(By.CLASS_NAME, 'AuthLoginInputToggle-type')
            element.click()
            element_login = driver.find_element('id', 'passp-field-login')
            element_login.send_keys('m7842066' + Keys.RETURN)
            sleep(2)
            element_pass = driver.find_element('id', 'passp-field-passwd')
            element_pass.send_keys('Pim$h@srh@12' + Keys.RETURN)
            sleep(1)
            action.send_keys(Keys.RETURN)
            action.perform()
            sleep(1)

            while True:
                try:
                    element = driver.find_element(By.CLASS_NAME, 'passp-phone-template')
                except selenium.common.exceptions.NoSuchElementException:
                    break
                else:
                    sleep(.1)

            sleep(1)
            pickle.dump(driver.get_cookies(), open('cookies', 'wb'))
        else:
            driver.refresh()

    def shadow_root(host, ad_id):
        shadowRoot = driver.execute_script("return arguments[0].shadowRoot", host)

        for item in ad_id:
            try:
                element = shadowRoot.find_element(By.CSS_SELECTOR, item)
            except selenium.common.exceptions.NoSuchElementException:
                pass
            else:
                driver.execute_script("arguments[0].click();", element)
                return

    def main():
        while True:
            sleep(.25)
            # input('continue?')
            try:
                host = driver.find_element(By.XPATH,
                                           '/html/body/div[1]/div[13]/div[1]/div[3]/div[2]/div/div[1]/div/div[2]')
            except selenium.common.exceptions.NoSuchElementException:
                pass
            else:
                shadow_root(host, ad_id)

    driver = webdriver.Chrome()
    action = ActionChains(driver)
    driver.get(
        'https://music.yandex.ru/home')
    sleep(.5)
    login()
    sleep(1)
    try:
        element = driver.find_element(By.CLASS_NAME, 'pay-promo-close-btn js-close')
    except selenium.common.exceptions.NoSuchElementException:
        pass
    else:
        element.click()
    driver.get('https://music.yandex.ru/home')
    sleep(1)
    element = driver.find_element(By.CLASS_NAME, 'rup__content-button')
    element.click()

    while True:
        main()


if __name__ == '__main__':
    yandex_music()
