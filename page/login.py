from selenium import webdriver
from time import sleep

import sys
from os.path import dirname,abspath
project_path = dirname(dirname(abspath(__file__)))
sys.path.append(project_path + r'/config')

from configuration import *

driver = webdriver.Chrome()
driver.get(test_url())
sleep(3)


