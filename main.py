import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--window-size=1600,980')
driver = webdriver.Chrome("./chromedriver", options=options)
# driver = webdriver.Chrome("./chromedriver", chrome_options=options)
options.add_argument('headless')
# options.add_argument('--headless')
driver.get("https://covid-19.ontario.ca/school-screening/")
print(driver.title)

# Page 1
# Find Element By CSS Class And Click
driver.find_element_by_css_selector(".button__StyledButton-sc-1hmy6jw-0").click()

# Page 2
# Save Current Page Prl
current_url = driver.current_url

# Wait For URL Change With 5 seconds Timeout
WebDriverWait(driver, 5).until(EC.url_changes(current_url))

# Print New URL
new_url = driver.current_url
print(new_url)

driver.find_element_by_css_selector(".button__StyledButton-sc-1hmy6jw-0").click()

# Page 3
current_url = driver.current_url
WebDriverWait(driver, 5).until(EC.url_changes(current_url))
new_url = driver.current_url
print(new_url)

driver.find_element_by_css_selector(".button__StyledButton-sc-1hmy6jw-0").click()

# Page 4
current_url = driver.current_url
WebDriverWait(driver, 5).until(EC.url_changes(current_url))
new_url = driver.current_url
print(new_url)
# Find Element By ID And Click
driver.find_element_by_id("none_of_the_above").click()
driver.find_element_by_css_selector(".button__StyledButton-sc-1hmy6jw-0").click()

# Page 5
current_url = driver.current_url
WebDriverWait(driver, 5).until(EC.url_changes(current_url))
new_url = driver.current_url
print(new_url)

driver.find_element_by_css_selector(".button__StyledButton-sc-1hmy6jw-0").click()

# Page 6
current_url = driver.current_url
WebDriverWait(driver, 5).until(EC.url_changes(current_url))
new_url = driver.current_url
print(new_url)

driver.find_element_by_css_selector(".button__StyledButton-sc-1hmy6jw-0").click()

#Page  7
current_url = driver.current_url
WebDriverWait(driver, 5).until(EC.url_changes(current_url))
new_url = driver.current_url
print(new_url)

driver.find_element_by_css_selector(".button__StyledButton-sc-1hmy6jw-0").click()

# Page 8
current_url = driver.current_url
WebDriverWait(driver, 5).until(EC.url_changes(current_url))
new_url = driver.current_url
print(new_url)

driver.find_element_by_css_selector(".button__StyledButton-sc-1hmy6jw-0").click()

# Page  9
current_url = driver.current_url
WebDriverWait(driver, 5).until(EC.url_changes(current_url))
new_url = driver.current_url
print(new_url)
# Find Element By Xpath And Click
driver.find_element_by_xpath("//*[contains(text(), 'Download result (PDF)')]").click()

# Close Browser
# Wait 5 Seconds Before Quiting
time.sleep(5)
driver.quit()