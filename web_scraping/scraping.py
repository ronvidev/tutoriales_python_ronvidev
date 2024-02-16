from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


URL_PAGE = 'https://www.pasionariabordados.com.ar/textiles-para-el-hogar'


def presionar_boton(driver):
    while True:
        try:
            boton = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="products_feed-btn"]')))
            boton.click()
        except:
            break


def obtener_datos(driver):
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    elementos_h3 = soup.find_all('h3', attrs={'class':'products-feed__product-name text--primary'})
    
    for h3 in elementos_h3:
        elemento_a = h3.find('a')
        if elemento_a:
            texto = elemento_a.text.replace('\n', '').strip()
            print(texto)
    

driver = webdriver.Chrome()
driver.get(URL_PAGE)
presionar_boton(driver)
obtener_datos(driver)
driver.quit()