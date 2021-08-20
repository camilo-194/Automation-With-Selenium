import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class using_unittes(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r'C:\dchrome\chromedriver.exe')

	def test_cambiar_venta(self):
		driver = self.driver
		driver.get('https://www.google.com')
		time.sleep(2)
		#se puede meter información al anterior script
		driver.execute_script("window.open('');")
		time.sleep(2)
		driver.switch_to.window(driver.window_handles[1])#volvemos a la anterior pestaña 
		driver.get('https://www.facebook.com')#ingresamos información 
		time.sleep(2)
		driver.switch_to.window(driver.window_handles[0])
		time.sleep(2)


if __name__ == '__main__':
	unittest.main()	


