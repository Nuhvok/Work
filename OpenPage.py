from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://google.com/')

element = driver.find_element_by_name("q")
element.send_keys("some text")
