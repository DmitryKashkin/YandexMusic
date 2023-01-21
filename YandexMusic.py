from selenium import webdriver
import selenium
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
import auth_data


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

            original_window = driver.current_window_handle
            wait = WebDriverWait(driver, 10)
            element = driver.find_element(By.CSS_SELECTOR,
                                          'body > div.page-root.page-root_no-player.deco-pane-back.page-root_empty-player > div.head-container > div > div > div.head-kids__user > a > span > span')

            driver.execute_script("arguments[0].click();", element)
            wait.until(EC.number_of_windows_to_be(2))
            for window_handle in driver.window_handles:
                if window_handle != original_window:
                    driver.switch_to.window(window_handle)
                    break

            element_login = driver.find_element(By.CSS_SELECTOR, '#passp-field-login')
            element_login.send_keys(auth_data.user + Keys.RETURN)
            sleep(2)
            element_pass = driver.find_element('id', 'passp-field-passwd')
            element_pass.send_keys(auth_data.password + Keys.RETURN)
            sleep(1)
            action.send_keys(Keys.RETURN)
            action.perform()
            sleep(1)

            while True:
                try:
                    element = driver.find_element(By.CLASS_NAME, 'auth-challenge__call')
                except selenium.common.exceptions.NoSuchElementException:
                    break
                else:
                    sleep(.1)
            sleep(1)
            while True:
                try:
                    element = driver.find_element(By.CLASS_NAME, 'passp-phone-template')
                except selenium.common.exceptions.NoSuchElementException:
                    break
                except selenium.common.exceptions.WebDriverException:
                    break
                else:
                    sleep(.1)

            sleep(5)
            driver.switch_to.window(original_window)
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

    def ad_close():
        try:
            element = driver.find_element(By.CLASS_NAME, 'pay-promo-close-btn js-close')
        except selenium.common.exceptions.NoSuchElementException:
            pass
        else:
            element.click()

    driver = webdriver.Chrome()
    # driver = webdriver.Edge()

    action = ActionChains(driver)
    driver.get(
        'https://music.yandex.ru/home')
    sleep(.5)
    ad_close()
    sleep(.5)
    login()
    sleep(1)
    ad_close()
    driver.get('https://music.yandex.ru/home')
    sleep(1)
    element = driver.find_element(By.CLASS_NAME, 'rup__content-button-play')
    element.click()

    while True:
        main()


if __name__ == '__main__':
    yandex_music()
