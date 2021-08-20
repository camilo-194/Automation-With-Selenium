import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class using_test(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r'C:\dchrome\chromedriver.exe')

	def testnavegando_pestañas(self):
		driver = self.driver
		driver.get('https://www.gmail.com')
		time.sleep(2)
		driver.get('https://www.google.com')
		time.sleep(2)
		driver.get('https://www.youtube.com')
		time.sleep(2)
		driver.back()#regresamos a la pagina anterior, codigo de SELENIUM
		time.sleep(2)
		driver.back()#regresamos a la pagina anterior
		time.sleep(2)
		driver.forward()#regresamos a la pagina siguiente, codigo de SELENIUM
		time.sleep(2)

if __name__ == '__main__':
	unittest.main()