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

# desired_capabilities = DesiredCapabilities.CHROME  # 修改页面加载策略
# desired_capabilities["pageLoadStrategy"] = "none"  # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe" #chromedriver的路徑
driver = webdriver.Chrome(chrome_driver, options=chrome_options)

分支Test1
# --------------------------------座位選擇函式--------------------------------------------------------------------------------------------------#
def onepart():
    # js = "var q=document.documentElement.scrollTop=100000"
    # driver.execute_script(js)
    # --------------------------------座位編號--------------------------------------------------------------------------------------------------#
    A = '#ticket_239760 .plus'
    B = '#ticket_239759 .plus'
    C = '#ticket_239758 .plus'
    D = '#ticket_239757 .plus'
    E = '#ticket_239756 .plus'
    F = '#ticket_239755 .plus'
    G = '#ticket_239754 .plus'
    H = '#ticket_239761 .plus'
    I = '#ticket_239762 .plus'
    # --------------------------------------------------------------------------------------------------------------------------------------------------#
    time.sleep(0.5)
    for c in [A, B, C, D, E, F, G, H, I]:
        try:
            n = 0
            while n < 3:
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

n=0
while n<1:
    try:
        driver.get('https://kktix.com/events/20-jolin-0509/registrations/new')#--------------------------------kktix網址
        time.sleep(1)
        if driver.find_element_by_css_selector("#person_agree_terms").is_displayed():
            onepart()  # --------------------------------選票
        else:
            time.sleep(1)
            print(n)
            continue


#--------------------------------題目--------------------------------------------------------------------------------------------------#

        try:
            js = "var q=document.documentElement.scrollTop=100000"
            driver.execute_script(js)
            wait = WebDriverWait(driver, 5)
            for x in ["B", "B2", "C3", "D4", "B1", "B2", "B3", "B4", "C1", "C2", "C3", "C4", "D1", "D2", "D3", "D4",
                      "1A", "1B", "1C", "1D", "2A", "2B", "2C", "2D", "3A", "3B", "3C", "3D", "4A", "4B", "4C", "4D",
                      "Aa", "Ab", "Ac", "Ad", "Ba", "Bb", "Cc", "Dd", "Ca", "Cb", "Cc", "Cd", "Da", "Db", "Dc", "Dd",
                      "AA", "AB", "AC", "AD", "BA", "BB", "BC", "BD", "CA", "CB", "CC", "CD", "DA", "DB", "DC", "DD",
                      "A1a", "B2b", "C3c", "D4d",
                      "a1", "a2", "a3", "a4", "b1", "b2", "b3", "b4", "c1", "c2", "c3", "c4", "d1", "d2", "d3", "d4",
                      "1a", "2a", "3a", "4a", "1b", "2b", "3b", "4b", "1c", "2c", "3c", "4c", "1d", "2d", "3d", "4d",
                      "aa", "ab", "ac", "ad", "ba", "bb", "bc", "bd", "ca", "cb", "cc", "cd", "da", "db", "dc", "dd",
                      "11", "12", "13", "14", "21", "22", "23", "24", "31", "32", "33", "34", "41", "42", "43", "44",
                      "aA", "aB", "aC", "aD", "bA", "bB", "bC", "bD", "cA", "cB", "cC", "cD", "dA", "dB", "dC", "dD", ]:
                # for x in range(1, 101):
            #for x in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L","M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X","Y", "Z"]:
            #for x in ["AA", "AB", "AC", "AD", "AE", "BA", "BB", "BC", "BD", "BE", "CA", "CB", "CC", "CD", "CE", "DA", "DB", "DC", "DD", "DE", "EB", "EC", "ED", "EE"]:
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
window_before = driver.window_handles[0]
window_after = driver.window_handles[1]#開的分頁-1
driver.switch_to.window(window_after)
time.sleep(2)
driver.find_element_by_xpath('//div[4]/table/tbody/tr/td/div/div[2]/div').click()
