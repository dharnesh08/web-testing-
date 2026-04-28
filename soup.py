import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://erp.sece.ac.in/impreserp/Students/Default.aspx")
username = driver.find_element(By.ID, "txtLoginCodeSL")
pwd = driver.find_element(By.ID, "txtPasswordSL")
username.send_keys("<your username>")
pwd.send_keys("<your password>")
driver.find_element(By.ID, "ext-gen29").click()
driver.get("https://erp.sece.ac.in/impreserp/Students/Home.aspx")
actions = ActionChains(driver)
driver.find_element(By.LINK_TEXT, "My Academics").click()
driver.find_element(By.ID,"StudentAttendanceSummary.aspx").click()
time.sleep(1000)
