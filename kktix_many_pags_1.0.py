from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe" #chromedriver的路徑
driver = webdriver.Chrome(chrome_driver, options=chrome_options)


# --------------------------------座位選擇函式--------------------------------------------------------------------------------------------------#
def onepart():
    # js = "var q=document.documentElement.scrollTop=100000"
    # driver.execute_script(js)
    # --------------------------------座位編號--------------------------------------------------------------------------------------------------#
    A = '#ticket_237764 .plus'
    B = '#ticket_237763 .plus'
    C = '#ticket_237765 .plus'
    D = '#ticket_222221 .plus'
    E = '#ticket_237767 .plus'
    F = '#ticket_237768 .plus'
    # --------------------------------------------------------------------------------------------------------------------------------------------------#
    time.sleep(0.5)
    for c in [A, B, C, D, E, F]:
        try:
            n = 0
            while n < 2:
                if driver.find_element_by_css_selector(c).is_displayed():
                    driver.find_element_by_css_selector(c).click()
                n += 1
            print(c)
        except:
            pass
    wait = WebDriverWait(driver, 2)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//label/input')))
    driver.find_element_by_xpath("//input[@id='person_agree_terms']").click()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------#

n=12
while n<13:
    try:
        driver.get('https://kktix.com/events/2a4d920d/registrations/new')#--------------------------------kktix網址
        time.sleep(1)
        if driver.find_element_by_css_selector("#person_agree_terms").is_displayed():
            onepart()  # --------------------------------選票
        else:
            time.sleep(1)
            print(n)
            continue
        # onepart()


        #--------------------------------題目--------------------------------------------------------------------------------------------------#

        try:
            js = "var q=document.documentElement.scrollTop=100000"
            driver.execute_script(js)
            wait = WebDriverWait(driver, 5)
            for x in["1930", "1940", "1A", "1B", "1C", "1D", "2A", "2B", "2C", "2D", "3A", "3B", "3C", "3D", "4A", "4B", "4C", "4D", "5E", "6H", "A1", "A2", "A3", "A4", "B1", "B2", "B3", "B4", "C1", "C2", "C3", "C4", "D1", "D2", "D3", "D4", "Aa", "Bb", "Cc", "Dd", "Ee", "Ff", "Aa", "Bb", "Cc", "Dd", "Ee", "Ff", "1", "2", "3", "4", "5", "A", "B", "C", "D", "E", "F", "AA", "AB", "AC", "AD", "AE", "BA", "BB", "BC", "BD", "BE", "CA", "CB", "CC", "CD", "CE", "DA", "DB", "DC", "DD", "DE", "1930", "EB", "EC", "ED", "EE", "0"]:
            # for x in range(5, 101):
            # for x in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L","M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X","Y", "Z"]:
                time.sleep(0.1)
                wait.until(EC.element_to_be_clickable((By.XPATH, '//div/div/input')))
                driver.find_element_by_name("captcha_answer").send_keys(x)
                driver.find_element_by_css_selector('.btn-lg').click()
                print(x)
        except:
            print("GGG")
            pass
        #------------------------------------------------------------------------------------------------------------------------------------------------------------#

        if driver.find_element_by_css_selector(".register-new-next-button-area").is_displayed():
            break
        elif driver.find_element_by_css_selector(".modal-dialog:nth-child(2) .btn").is_displayed():
            print("WWW")
            break
        else:
            wait = WebDriverWait(driver, 20)
            wait.until(EC.alert_is_present())
            driver.switch_to.alert.accept()
            print("EEE")
            continue

        #--------------------------------防止沒有題目--------------------------------------------------------------------------------------------------#
        # try:
        #     driver.find_element_by_xpath("//div[5]/button").click()
        # except:
        #     pass
        #---------------------------------------------------------------------------------------------------------------------------------------#


    except:
        break
