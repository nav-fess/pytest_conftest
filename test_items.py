from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


def test_button_basket_expected_conditions(browser):
    browser.get(link)
   
    button = WebDriverWait(browser, 6).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket"))) 
    
    
    assert button != False, "Button not found"  

    time.sleep(10)
