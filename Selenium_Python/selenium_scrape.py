from selenium import webdriver
from selenium.webdriver.common.by import By
import time
url='https://www.youtube.com/@fifa/videos'
driver = webdriver.Chrome()
driver.get(url)
videos = driver.find_elements(By.CLASS_NAME,"style-scope ytd-rich-grid-media")
for vid in videos:
    title = vid.find_elements(By.XPATH,'//*[@id="details"]')
    views = vid.find_elements(By.XPATH,'//*[@id="metadata-line"]/span[1]')
    when = vid.find_elements(By.XPATH, '//*[@id="metadata-line"]/span[2]')
    print(title)
time.sleep(30)