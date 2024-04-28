from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("sample test")

# Launch the Edge browser
driver = webdriver.Edge()

# Maximize the browser window
driver.maximize_window()

# Open the URL
driver.get('https://mydy.dypatil.edu')

# Find the username and password input fields
username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))

# Input username and password
username_input.send_keys('reu.bar.rt21@dypatil.edu')
password_input.send_keys('dypatil@123')

# Submit the form by pressing Enter
password_input.send_keys(Keys.ENTER)

# Wait for the page to load after login
WebDriverWait(driver, 10).until(EC.title_contains("Dashboard"))

# Close the browser
driver.quit()

print("sample test successfully")
