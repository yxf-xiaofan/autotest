from lib2to3.pgen2 import driver
from selenium import webdriver
from time import sleep
from configuration import *

driver = webdriver.Chrome()
driver.get(url)
sleep(3)


