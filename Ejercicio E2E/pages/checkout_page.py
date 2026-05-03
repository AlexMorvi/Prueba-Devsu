# Page Object Model for Checkout Page
from selenium.webdriver.common.by import By
from utils.driver_manager import BasePage
import time

class CheckoutPage(BasePage):
    # Locators - Purchase Modal
    PURCHASE_MODAL = (By.ID, "orderModal")
    NAME_FIELD = (By.ID, "name")
    COUNTRY_FIELD = (By.ID, "country")
    CITY_FIELD = (By.ID, "city")
    CREDIT_CARD_FIELD = (By.ID, "card")
    MONTH_FIELD = (By.ID, "month")
    YEAR_FIELD = (By.ID, "year")
    PURCHASE_BUTTON = (By.XPATH, "//button[contains(text(),'Purchase')]")
    CLOSE_BUTTON = (By.XPATH, "//div[@id='orderModal']//button[contains(text(),'Close')]")
    
    # Success Modal
    SUCCESS_MODAL = (By.XPATH, "//div[contains(@class,'sweet-alert')]")
    SUCCESS_MESSAGE = (By.XPATH, '//h2[contains(text(),"Thank you for your purchase!")]')
    ORDER_DETAILS = (By.XPATH, "//p[@class='lead text-muted']")
    OK_BUTTON = (By.XPATH, "//button[contains(text(),'OK')]")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def fill_purchase_form(self, customer_data):
        """Fill the purchase form with customer data"""
        # Wait for modal to be visible
        print("      → Esperando que aparezca el modal de compra...")
        self.wait_for_element(self.PURCHASE_MODAL)
        time.sleep(1)
        print("      → Modal de compra visible, llenando campos...")
        
        # Fill form fields
        print(f"      → Ingresando nombre: {customer_data['name']}")
        self.send_keys_to_element(self.NAME_FIELD, customer_data['name'])
        
        print(f"      → Ingresando país: {customer_data['country']}")
        self.send_keys_to_element(self.COUNTRY_FIELD, customer_data['country'])
        
        print(f"      → Ingresando ciudad: {customer_data['city']}")
        self.send_keys_to_element(self.CITY_FIELD, customer_data['city'])
        
        print(f"      → Ingresando tarjeta: ****-****-****-{customer_data['card'][-4:]}")
        self.send_keys_to_element(self.CREDIT_CARD_FIELD, customer_data['card'])
        
        print(f"      → Ingresando mes: {customer_data['month']}")
        self.send_keys_to_element(self.MONTH_FIELD, customer_data['month'])
        
        print(f"      → Ingresando año: {customer_data['year']}")
        self.send_keys_to_element(self.YEAR_FIELD, customer_data['year'])
        
        print("      → Todos los campos del formulario completados")
    
    def complete_purchase(self):
        """Click the Purchase button to complete the order"""
        print("      → Haciendo clic en botón 'Purchase'...")
        self.click_element(self.PURCHASE_BUTTON)
        time.sleep(3)
        print("      → Orden procesada, esperando confirmación...")
    
    def is_purchase_successful(self):
        """Check if purchase was successful by looking for success message"""
        print("      → Verificando si la compra fue exitosa...")
        try:
            self.wait_for_element(self.SUCCESS_MESSAGE)
            print("      → ✅ Mensaje de éxito encontrado")
            return True
        except:
            print("      → ❌ No se encontró mensaje de éxito")
            return False
    
    def get_success_message(self):
        """Get the success message text"""
        try:
            message = self.get_text(self.SUCCESS_MESSAGE)
            print(f"      → Mensaje de éxito obtenido: {message}")
            return message
        except:
            print("      → Error al obtener mensaje de éxito")
            return ""
    
    def get_order_details(self):
        """Get order details from success modal"""
        try:
            details = self.get_text(self.ORDER_DETAILS)
            print(f"      → Detalles de la orden obtenidos")
            return details
        except:
            print("      → Error al obtener detalles de la orden")
            return ""
    
    def close_success_modal(self):
        """Close the success modal"""
        try:
            print("      → Cerrando modal de éxito...")
            self.click_element(self.OK_BUTTON)
            time.sleep(2)
            print("      → Modal de éxito cerrado")
        except:
            print("      → Error al cerrar modal de éxito")
    
    def close_purchase_modal(self):
        """Close the purchase modal"""
        try:
            print("      → Cerrando modal de compra...")
            self.click_element(self.CLOSE_BUTTON)
            time.sleep(2)
            print("      → Modal de compra cerrado")
        except:
            print("      → Error al cerrar modal de compra")
