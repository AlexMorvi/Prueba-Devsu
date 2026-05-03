# Page Object Model for Cart Page
from selenium.webdriver.common.by import By
from utils.driver_manager import BasePage
import time

class CartPage(BasePage):
    # Locators
    CART_LINK = (By.ID, "cartur")
    CART_ITEMS = (By.XPATH, "//tbody[@id='tbodyid']/tr")
    ITEM_NAME = (By.XPATH, ".//td[2]")
    ITEM_PRICE = (By.XPATH, ".//td[3]")
    DELETE_BUTTON = (By.XPATH, ".//td[4]/a")
    TOTAL_PRICE = (By.ID, "totalp")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Place Order')]")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def navigate_to_cart(self):
        """Navigate to cart page"""
        print("      → Haciendo clic en el enlace del carrito...")
        self.click_element(self.CART_LINK)
        time.sleep(3)
        print("      → Página del carrito cargada")
    
    def get_cart_items(self):
        """Get all items in cart"""
        print("      → Analizando productos en el carrito...")
        items = []
        try:
            cart_rows = self.driver.find_elements(*self.CART_ITEMS)
            for i, row in enumerate(cart_rows):
                try:
                    name = row.find_element(*self.ITEM_NAME).text
                    price = row.find_element(*self.ITEM_PRICE).text
                    items.append({
                        'name': name,
                        'price': price
                    })
                    print(f"        • Producto {i+1}: {name} - ${price}")
                except:
                    continue
        except:
            print("      → No se encontraron productos en el carrito")
        return items
    
    def get_cart_items_count(self):
        """Get number of items in cart"""
        try:
            items = self.driver.find_elements(*self.CART_ITEMS)
            count = len(items)
            print(f"      → Conteo de productos: {count}")
            return count
        except:
            print("      → Error al contar productos, asumiendo 0")
            return 0
    
    def get_total_price(self):
        """Get total price from cart"""
        try:
            total = self.get_text(self.TOTAL_PRICE)
            print(f"      → Precio total calculado: ${total}")
            return total
        except:
            print("      → Error al obtener precio total, asumiendo $0")
            return "0"
    
    def delete_item(self, item_index=0):
        """Delete an item from cart by index"""
        print(f"      → Eliminando producto en posición {item_index}...")
        items = self.driver.find_elements(*self.CART_ITEMS)
        if items and item_index < len(items):
            delete_btn = items[item_index].find_element(*self.DELETE_BUTTON)
            delete_btn.click()
            time.sleep(2)
            print("      → Producto eliminado del carrito")
        else:
            print("      → No se pudo eliminar el producto (índice inválido)")
    
    def proceed_to_checkout(self):
        """Click Place Order button"""
        print("      → Buscando botón 'Place Order'...")
        self.scroll_to_element(self.PLACE_ORDER_BUTTON)
        print("      → Haciendo clic en 'Place Order'...")
        self.click_element(self.PLACE_ORDER_BUTTON)
        time.sleep(2)
        print("      → Formulario de checkout abierto")
    
    def is_cart_empty(self):
        """Check if cart is empty"""
        is_empty = self.get_cart_items_count() == 0
        print(f"      → Carrito vacío: {'Sí' if is_empty else 'No'}")
        return is_empty
