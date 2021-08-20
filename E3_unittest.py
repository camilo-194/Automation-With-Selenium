import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys # Opciones de teclado
import time

class usando_unittest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r'C:\dchrome\chromedriver.exe')

	def test_buscar(self):
		driver = self.driver
		driver.get('https://www.google.com')
		self.assertIn('Google', driver.title) #validamos si estamos en la pagina correcta	
		elemento = driver.find_element_by_name('q')#buscamos es elemento que necesitamos
		elemento.send_keys('instagram')#insertamos la palabranos que vamos a buscar
		elemento.send_keys(Keys.RETURN)#damos enter para cargar la informacion 
		time.sleep(1)
		driver.execute_script("window.open('');")
		driver.switch_to.window(driver.window_handles[1])
		driver.get('https://www.facebook.com')
		time.sleep(2)


		assert 'No se encontro el elemento:' not in driver.page_source

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()		