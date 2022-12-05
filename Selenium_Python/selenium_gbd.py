from selenium import webdriver
from selenium.webdriver.common.by import By
import time
url='https://www.google.com/search?q=tesla&sxsrf=ALiCzsYxy31asmIM5uwaXrw0Uw1FcBU2jA%3A1670226908387&ei=3KONY96pF5XrmAXh4pvgBw&ved=0ahUKEwjeh8aMgOL7AhWVNaYKHWHxBnwQ4dUDCA8&uact=5&oq=tesla&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIECCMQJzIKCAAQsQMQgwEQQzINCC4QxwEQsQMQ0QMQQzIHCAAQsQMQQzIKCAAQsQMQgwEQQzIKCAAQsQMQgwEQQzIHCAAQsQMQQzIKCAAQsQMQgwEQQzIECAAQQzIHCAAQsQMQQzoECC4QJzoLCC4QgwEQsQMQkQI6BQgAEJECOgUIABCABDoHCCMQ6gIQJzoHCC4Q6gIQJzoECC4QQzoQCC4QsQMQgwEQxwEQ0QMQQzoICAAQsQMQgwE6CwgAEIAEELEDEIMBOgUILhCABDoHCC4Q1AIQQzoNCC4QsQMQxwEQ0QMQQzoKCC4QxwEQ0QMQQ0oECEEYAEoECEYYAFCvBVibK2CMLmgCcAF4BIAB8QGIAaEOkgEFMC45LjGYAQCgAQGwAQrAAQE&sclient=gws-wiz-serp'
driver = webdriver.Chrome()
driver.get(url)
title = driver.find_elements(By.CLASS_NAME,"LC20lb MBeuO DKV0Md")
for t in title :
    description= title.find_elements(By.XPATH,'//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[2]/div/span')
    print(description.text)



time.sleep(30)