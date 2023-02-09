import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.command import Command

from sys import exit

def get_status(web):
    try:
        response = requests.get(web)
        if response.status_code == 200:
            print('Web site exists')
            return True
    except Exception as e:
        print('Web site does not exist') 
        return False

def main_function():
    if get_status('http://127.0.0.1:5000'):

        my_driver = webdriver.Chrome()
        my_driver.get("http://127.0.0.1:5000")

        score = int(my_driver.find_element(By.ID, "score").text)
        if isinstance(score,int):
            print("0")
            exit(0)
        else:
            print("-1")
            exit(-1)
    else:
        print("-1")
        exit(-1)
main_function()
# print(int(score))
