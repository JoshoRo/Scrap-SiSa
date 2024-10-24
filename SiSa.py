#Codigo de Web Scraping para sacar los productos del supermercado Santa Isabel
#Se utiliza la libreria Selenium y despues los datos extraidos se guardan en un documento excel

#Librerias a utilizar
from selenium import webdriver
from selenium.webdriver.edge.service import Service
import datetime

#Modulos
import Modulos.funciones_excel as FE
import Modulos.funciones_scrap as FS

lista_productos=[]

edge_driver_path = 'driver.exe'
service=Service(executable_path=edge_driver_path)
options=webdriver.EdgeOptions()
driver = webdriver.Edge(service=service,options=options)
driver.set_window_size(1024, 768)
driver.maximize_window()

FS.sacar_datos(driver,1,16,"lacteos",lista_productos)
FS.sacar_datos(driver,1,36,"despensa",lista_productos)
FS.sacar_datos(driver,1,5,"frutas-y-verduras",lista_productos)
FS.sacar_datos(driver,1,4,"carniceria",lista_productos)
FS.sacar_datos(driver,1,21,"limpieza",lista_productos)
FS.sacar_datos(driver,1,17,"bebidas-aguas-y-jugos",lista_productos)
FS.sacar_datos(driver,1,23,"vinos-cervezas-y-licores",lista_productos)
FS.sacar_datos(driver,1,9,"congelados",lista_productos)
FS.sacar_datos(driver,1,3,"pescaderia",lista_productos)
FE.crear_y_guardar_libro_excel(lista_productos,r"SiSa.xlsx")

