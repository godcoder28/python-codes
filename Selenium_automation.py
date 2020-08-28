from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = "C:\Program Files\Python38\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://online.vidyamandir.com")
id = driver.find_element_by_id("edit-name-1")
id.send_keys("shivang2873@gmail.com")

password = driver.find_element_by_id("edit-pass-1")
password.send_keys("52RA54")

password.submit()

liveclass = driver.get("https://online.vidyamandir.com/liveclass/list")

while True:
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ffbgneryjnbrdfwebiner"))
        )
        print("try")
    except:
        print("timeout")
