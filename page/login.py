from selenium import webdriver
from time import sleep
import sys

"""sys.path.append("C:\Users\fanhao\Desktop\auto\autotest\configuration.py")"""
from configuration import *

driver = webdriver.Chrome()
driver.get(url)
sleep(3)


