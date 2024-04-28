from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()
chrome_binary_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
options.binary_location = chrome_binary_path
print("Sample test case started")
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.google.com/")
# Identify the Google search text box and enter the value
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("javatpoint")
time.sleep(3)
# Click on the Google search button
search_box.submit()
time.sleep(3)
# Close the browser
driver.close()
print("Sample test case successfully completed")
