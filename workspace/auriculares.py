from selenium import webdriver as wd
#Para presionar enter
from selenium.webdriver.common.keys import Keys


website='https://www.mercadolibre.com.ar/'
path='C:/Users/Alejandro Ocampo/Downloads/chromedriver'
driver=wd.Chrome(path)
#Instancia de la pagina
driver.get(website)
#Busqueda de producto
search=driver.find_element_by_css_selector('#cb1-edit')
search.send_keys('auriculares')
search.send_keys(Keys.ENTER)