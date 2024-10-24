from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def sacar_datos(driver,pag_min,pag_max,categoria,def_list):
    aux = []
    for x in range(pag_min, pag_max):
        url="https://www.santaisabel.cl/"+categoria+"?page="+str(x)
        driver.get(url)
        print("-----------------------------------PAGINA "+str(x)+" ---------------------------------------------------")
        try:
            WebDriverWait(driver, 60).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'product-card')))
            products = driver.find_elements(By.CLASS_NAME, 'product-card') 
            for product in products:
                product_name_elem = product.find_element(By.CLASS_NAME,'product-card-name')
                if product_name_elem:
                    product_name = product_name_elem.text.strip()
                try:
                    product_regular_price_elem=product.find_element(By.CLASS_NAME,'prices-main-price')
                    product_regular_price = product_regular_price_elem.text.strip()
                    product_regular_price = product_regular_price.replace("$", "").replace(".", "")
                    num_regular_price = int(product_regular_price)
                except:
                    num_regular_price=0
                try:
                    product_sale_price_elem=product.find_element(By.CLASS_NAME,'prices-old-price')
                    product_sale_price = product_sale_price_elem.text.strip()
                    #print(product_sale_price)
                    product_sale_price = product_sale_price.replace("$", "").replace(".", "")
                    num_sale_price = int(product_sale_price)
                except:
                    num_sale_price=0
                
                try:
                    offer_element = product.find_element(By.CSS_SELECTOR,'.area-promo-tmp.prices-price.price-box.tmp-order-one.p1')
                    offer_text = offer_element.text
                except:
                    offer_text = 0
                if num_sale_price>num_regular_price:
                    num_aux=num_regular_price
                    num_regular_price=num_sale_price
                    num_sale_price=num_aux
                aux.append(product_name)
                aux.append(num_regular_price)
                aux.append(num_sale_price)
                aux.append(offer_text)
                def_list.append(aux)
                aux=[]
        except Exception as e:
            print('Error:', e)
    return def_list