from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path = r'C:\dchrome\chromedriver.exe')
driver.get('https://facebook.com')

usuario = driver.find_element_by_id('email')
usuario.send_keys('jcamilovilla194@gmail.com')
#usuario.send_keys(Keys.ENTER)
#time.sleep(3)

clave = driver.find_element_by_id('pass')
clave.send_keys('villa123')
clave.send_keys(Keys.ENTER)


