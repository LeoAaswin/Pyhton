from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
service = Service('C:\\Users\\nisha\\Desktop\\chromedriver\\chromedriver.exe')

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-self-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    
    driver = webdriver.Chrome(service=service,options=options)
    driver.get("https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6")
    return driver


def main():
    driver = get_driver()
    element = driver.find_element(by="span", value="stock-trend trend-grow")
    time.sleep(5)
    return element.text

print(main())