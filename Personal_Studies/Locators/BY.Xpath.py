import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

serv_obj = Service(ChromeDriverManager().install())
url = "https://web.facebook.com/"

driver = webdriver.Chrome(service=serv_obj)
driver.get(url)
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@id='email']").clear()
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("nedmond99@gmail.com")
driver.find_element(By.XPATH, "//input[@id='pass']").clear()
driver.find_element(By.XPATH, "//input[@id='pass']").send_keys("1234567")
