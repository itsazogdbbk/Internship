import os
import time
import pandas as pd
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Firefox()
url='https://www.google.com/search?q=tesla&sxsrf=ALiCzsYxy31asmIM5uwaXrw0Uw1FcBU2jA%3A1670226908387&ei=3KONY96pF5XrmAXh4pvgBw&ved=0ahUKEwjeh8aMgOL7AhWVNaYKHWHxBnwQ4dUDCA8&uact=5&oq=tesla&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIECCMQJzIKCAAQsQMQgwEQQzINCC4QxwEQsQMQ0QMQQzIHCAAQsQMQQzIKCAAQsQMQgwEQQzIKCAAQsQMQgwEQQzIHCAAQsQMQQzIKCAAQsQMQgwEQQzIECAAQQzIHCAAQsQMQQzoECC4QJzoLCC4QgwEQsQMQkQI6BQgAEJECOgUIABCABDoHCCMQ6gIQJzoHCC4Q6gIQJzoECC4QQzoQCC4QsQMQgwEQxwEQ0QMQQzoICAAQsQMQgwE6CwgAEIAEELEDEIMBOgUILhCABDoHCC4Q1AIQQzoNCC4QsQMQxwEQ0QMQQzoKCC4QxwEQ0QMQQ0oECEEYAEoECEYYAFCvBVibK2CMLmgCcAF4BIAB8QGIAaEOkgEFMC45LjGYAQCgAQGwAQrAAQE&sclient=gws-wiz-serp'
driver.get(url)
title = driver.find_elements(By.CSS_SELECTOR, "LC20lb")
title_list=[]
for t in title:
    print(t.text)
    title_list.append(t.text)
description= driver.find_elements(By.CLASS_NAME,"VwiC3b")
description_list=[]
for d in description:
    print(d.text)
    description_list.append(d.text)
link= driver.find_elements(By.CLASS_NAME,"iUh30 qLRx3b tjvcx")
link_list=[]
for l in link:
    print(l.text)
    link_list.append(l.text)
dictonary={"Title":title_list[:5],"Description":description_list[:5], "Link":link_list[:5]}
#print(dictonary)
df = pd.DataFrame(dictonary)
df.to_csv('tesla.csv')
