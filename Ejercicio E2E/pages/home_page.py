# Page Object Model for Home Page
from selenium.webdriver.common.by import By
from utils.driver_manager import BasePage
import time

class HomePage(BasePage):
    # Locators
    HOME_LINK = (By.XPATH, "//a[contains(text(),'Home')]")
    CATEGORIES_SECTION = (By.ID, "cat")
    PHONES_CATEGORY = (By.XPATH, "//a[contains(text(),'Phones')]")
    LAPTOPS_CATEGORY = (By.XPATH, "//a[contains(text(),'Laptops')]")
    MONITORS_CATEGORY = (By.XPATH, "//a[contains(text(),'Monitors')]")
    
    # Product links - using more specific selectors
    SAMSUNG_GALAXY_S6 = (By.XPATH, "//a[contains(text(),'Samsung galaxy s6')]")
    NOKIA_LUMIA_1520 = (By.XPATH, "//a[contains(text(),'Nokia lumia 1520')]")
    SONY_VAIO_I5 = (By.XPATH, "//a[contains(text(),'Sony vaio i5')]")
    MACBOOK_AIR = (By.XPATH, "//a[contains(text(),'MacBook air')]")
    APPLE_MONITOR_24 = (By.XPATH, "//a[contains(text(),'Apple monitor 24')]")
    
    # Navigation
    NEXT_BUTTON = (By.ID, "next2")
    PREVIOUS_BUTTON = (By.ID, "prev2")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.demoblaze.com/"
    
    def navigate_to_home(self):
        """Navigate to the home page"""
        print(f"      → Cargando URL: {self.url}")
        self.driver.get(self.url)
        time.sleep(2)
        print("      → Esperando a que la página se cargue completamente...")
    
    def click_phones_category(self):
        """Click on Phones category"""
        print("      → Buscando categoría 'Phones'...")
        self.click_element(self.PHONES_CATEGORY)
        time.sleep(2)
        print("      → Categoría 'Phones' seleccionada, cargando productos...")
    
    def click_laptops_category(self):
        """Click on Laptops category"""
        print("      → Buscando categoría 'Laptops'...")
        self.click_element(self.LAPTOPS_CATEGORY)
        time.sleep(2)
        print("      → Categoría 'Laptops' seleccionada, cargando productos...")
    
    def click_monitors_category(self):
        """Click on Monitors category"""
        print("      → Buscando categoría 'Monitors'...")
        self.click_element(self.MONITORS_CATEGORY)
        time.sleep(2)
        print("      → Categoría 'Monitors' seleccionada, cargando productos...")
    
    def select_product(self, product_name):
        """Select a product by name"""
        product_locators = {
            "Samsung galaxy s6": self.SAMSUNG_GALAXY_S6,
            "Nokia lumia 1520": self.NOKIA_LUMIA_1520,
            "Sony vaio i5": self.SONY_VAIO_I5,
            "MacBook air": self.MACBOOK_AIR,
            "Apple monitor 24": self.APPLE_MONITOR_24
        }
        
        if product_name in product_locators:
            print(f"      → Buscando producto '{product_name}' en la página...")
            self.scroll_to_element(product_locators[product_name])
            print(f"      → Producto '{product_name}' encontrado, haciendo clic...")
            self.click_element(product_locators[product_name])
            time.sleep(2)
            print(f"      → Navegando a la página del producto '{product_name}'...")
        else:
            raise ValueError(f"Product {product_name} not found in predefined products")
    
    def click_next_page(self):
        """Click next page button"""
        if self.is_element_present(self.NEXT_BUTTON):
            self.click_element(self.NEXT_BUTTON)
            time.sleep(2)
    
    def click_previous_page(self):
        """Click previous page button"""
        if self.is_element_present(self.PREVIOUS_BUTTON):
            self.click_element(self.PREVIOUS_BUTTON)
            time.sleep(2)
