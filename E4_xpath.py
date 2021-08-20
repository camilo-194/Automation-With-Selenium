import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r'C:\dchrome\chromedriver.exe')

	def test_buscar_por_xpath(self):
		driver = self.driver
		driver.get('https://www.google.com')
		time.sleep(1)
		buscar_por_xpath = driver.find_element_by_xpath(#aca va la ruta) # xpath es una estructura de carpetas, objetos, etc... xpath relativo y absoluto
		time.sleep(1)
		buscar_por_xpath.send_keys('instagram', Keys.RETURN)
		time.sleep(1)

	def tearDowm(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()			