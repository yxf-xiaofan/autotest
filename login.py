from lib2to3.pgen2 import driver
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://avengers.wandianzhang.com/#/login")
sleep(3)


