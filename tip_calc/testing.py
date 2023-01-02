import time
from selenium import webdriver
from selenium.webdriver.common.by import By

my_driver = webdriver.Chrome(executable_path='/home/saeed/Downloads/chromedriver_linux64/chromedriver')
# google = my_driver.get("https://google.com")
my_driver.get("https://www.google.com/search?q=usd+to+nis&sxsrf=ALiCzsZkthVwDi5mDXmx7Pw6Lnx5a4rlGg%3A1670442998478&ei=9u-QY-3oHIKskdUP65OYyAQ&ved=0ahUKEwjtu6qMpej7AhUCVqQEHesJBkkQ4dUDCA8&uact=5&oq=usd+to+nis&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIQCAAQgAQQsQMQgwEQRhCCAjIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoJCAAQBxAeELADOgQIIxAnOgUIABCRAjoICAAQsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOgsIABCABBCxAxCDAToKCAAQgAQQhwIQFDoKCAAQsQMQgwEQQzoECAAQQzoHCAAQsQMQQzoICAAQgAQQsQM6DwgAELEDEIMBEEMQRhCCAjoHCAAQgAQQCkoECEEYAUoECEYYAFDjJViFsgFg-bQBaAZwAHgAgAHeAYgBvA-SAQYwLjExLjKYAQCgAQHIAQHAAQE&sclient=gws-wiz-serp")

# billamt = my_driver.find_element(By.ID, "billamt").send_keys("100")
usd_to_nis = my_driver.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[3]/div/div[2]/input')
# peopleamt = my_driver.find_element(By.ID, "peopleamt").send_keys("4")
# calculate = my_driver.find_element(By.ID, "calculate").click()

# time.sleep(5)
print(usd_to_nis.find_element())