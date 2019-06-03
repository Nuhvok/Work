from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Opens RB digital in Chrome
driver = webdriver.Chrome()
driver.get('http://rbdigital.rbdigitalqa.com/home')

# Waits for the page to load
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="sign_in"]/a')))

# Opens the log in popup
element = driver.find_element_by_xpath('//*[@id="sign_in"]/a')
element.click()

# Waits for the popup to open
element = WebDriverWait(driver, 5).until(
   EC.presence_of_element_located((By.XPATH, '//*[@id="sign_in"]/a'))
)

# Enteres the username
element = driver.find_element_by_xpath('//*[@id="username"]')
element.send_keys("") # Enter your username

# Enters the password
element = driver.find_element_by_xpath('//*[@id="password"]')
element.send_keys("") # Enter your pssword

# Submits the username and password
element = driver.find_element_by_xpath('//*[@id="btn-sign-in"]')
element.click()