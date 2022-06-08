from selenium import webdriver
from time import sleep
from configuration import *

driver = webdriver.Chrome()
driver.get(test_url())
sleep(3)


