from selenium import webdriver
import selenium
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.key_actions import KeyActions
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

    driver = webdriver.Chrome()
    # shadow = Shadow(driver)
    action = ActionChains(driver)
    driver.get(
        'https://music.yandex.ru/home')
    # driver.get(
    #     'https://passport.yandex.ru/auth?origin=music_button-header&retpath=https%3A%2F%2Fmusic.yandex.ru%2Fsettings%3Freqid%3D42336580116627399272688109178242113%26from-passport')
    sleep(1)

    login()

    sleep(.5)

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
        input('continue?')

        # shadow_host = driver.find_element(By.CLASS_NAME, 'mdj')
        # shadow_root = shadow_host.shadow_root
        # shadow_content = shadow_root.find_element(By.CLASS_NAME, 'Q87uEBIjuV')
        # shadow_content.click()

        host = driver.find_element(By.CLASS_NAME, 'mdj')
        print('ok')
        # driver.execute_script("return arguments[0].shadowRoot.getElementsByClassName('A4IcEp')[0].click()", host)
        shadowRoot = driver.execute_script("return arguments[0].shadowRoot", host)
        element = shadowRoot.find_element(By.CSS_SELECTOR, 'div > div > div.My9Rp0DBP > div.dq7AOa.hF2ft0 > div > div > div:nth-child(1)')
        print(element)
        driver.execute_script("arguments[0].click();", element)
        # element.click()



        # sleep(.25)
        # shadow_root.find_element(By.CLASS_NAME, 'dOszY').click()
        #
        # # driver.find_element(By.CLASS_NAME, 'U4mmIQOw').click()
        # sleep(.25)
        # shadow_root.find_element(By.CLASS_NAME, 'dOszY').click()

        # driver.find_element(By.CLASS_NAME, 'U4mmIQOw').click()

        # while True:
        #     sleep(.25)
        #     try:
        #         shadow_host = driver.find_element(By.CLASS_NAME, 'C7Yd')
        #     except selenium.common.exceptions.NoSuchElementException:
        #         pass
        #     else:
        #         shadow_root = shadow_host.shadow_root
        #
        #         element.click()
        #         sleep(.25)
        #         driver.find_element(By.CLASS_NAME, 'iLXh Zqa0uC14Of fRHekJD').click()
        #         sleep(.25)
        #         driver.find_element(By.CLASS_NAME, 'U4mmIQOw').click()

if __name__ == '__main__':
    yandex_music()