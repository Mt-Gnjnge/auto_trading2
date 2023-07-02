from selenium import webdriver
from selenium.webdriver.common.by import By
 
# SeleniumでChromeを起動
driver = webdriver.Chrome()
url = "https://www.sbisec.co.jp/ETGate"
driver.get(url)
driver.implicitly_wait(60) #対象となる要素が見つかるまで待機する

username_value = dummy # 任意の値を設定してください
password_value = dummy # 任意の値を設定してください
username = driver.find_element(By.NAME,"user_id")
# driver.find_element(By.NAME,"name").send_keys("test1")  
username.send_keys(username_value)
password = driver.find_element(By.NAME,"user_password")
password.send_keys(password_value)

driver.find_element(By.NAME,"ACT_login").click()