# Page Object Model for Product Page
from selenium.webdriver.common.by import By
from utils.driver_manager import BasePage
import time

class ProductPage(BasePage):
    # Locators
    PRODUCT_NAME = (By.XPATH, "//h2[@class='name']")
    PRODUCT_PRICE = (By.XPATH, "//h3[@class='price-container']")
    PRODUCT_DESCRIPTION = (By.ID, "more-information")
    ADD_TO_CART_BUTTON = (By.XPATH, "//a[contains(text(),'Add to cart')]")
    HOME_LINK = (By.XPATH, "//a[contains(text(),'Home')]")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def get_product_name(self):
        """Get the product name"""
        print("      → Obteniendo nombre del producto...")
        product_name = self.get_text(self.PRODUCT_NAME)
        print(f"      → Nombre del producto: {product_name}")
        return product_name
    
    def get_product_price(self):
        """Get the product price"""
        print("      → Obteniendo precio del producto...")
        product_price = self.get_text(self.PRODUCT_PRICE)
        print(f"      → Precio del producto: {product_price}")
        return product_price
    
    def add_to_cart(self):
        """Add product to cart"""
        print("      → Buscando botón 'Add to cart'...")
        self.scroll_to_element(self.ADD_TO_CART_BUTTON)
        print("      → Haciendo clic en 'Add to cart'...")
        self.click_element(self.ADD_TO_CART_BUTTON)
        time.sleep(1)
        
        # Handle the alert that appears after adding to cart
        print("      → Esperando confirmación del sistema...")
        if self.accept_alert():
            print("      → ✅ Confirmación recibida: Producto agregado al carrito")
            time.sleep(1)
        else:
            print("      → ⚠️ No se recibió confirmación del sistema")
        
    def go_back_to_home(self):
        """Navigate back to home page"""
        print("      → Regresando a la página principal...")
        self.click_element(self.HOME_LINK)
        time.sleep(2)
        print("      → De vuelta en la página principal")
