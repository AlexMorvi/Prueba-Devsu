# E2E Test for Demoblaze Purchase Flow
import pytest
import time
from utils.driver_manager import DriverManager
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

class TestPurchaseFlow:
    
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        """Setup and teardown for each test"""
        # Setup
        self.driver_manager = DriverManager()
        self.driver = self.driver_manager.setup_driver()
        
        # Initialize page objects
        self.home_page = HomePage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)
        
        yield
        
        # Teardown
        self.driver_manager.quit_driver()
    
    def test_complete_purchase_flow(self):
        """
        Complete E2E test for purchase flow:
        1. Navigate to home page
        2. Add two products to cart
        3. View cart
        4. Complete purchase form
        5. Finalize purchase
        """
        
        print("\n" + "="*80)
        print("🚀 INICIANDO FLUJO COMPLETO DE COMPRA E2E")
        print("="*80)
        
        # Step 1: Navigate to home page
        print("\n📍 PASO 1: NAVEGANDO A LA PÁGINA PRINCIPAL")
        print("   • Accediendo a https://demoblaze.com...")
        self.home_page.navigate_to_home()
        print("   ✅ Página principal cargada exitosamente")
        
        # Step 2: Add first product (Samsung Galaxy S6)
        print("\n🛒 PASO 2: AGREGANDO PRIMER PRODUCTO AL CARRITO")
        print("   • Navegando a la categoría 'Phones'...")
        self.home_page.click_phones_category()
        print("   • Seleccionando producto 'Samsung Galaxy S6'...")
        self.home_page.select_product("Samsung galaxy s6")
        
        # Verify we're on product page and add to cart
        product_name_1 = self.product_page.get_product_name()
        print(f"   • Producto seleccionado: {product_name_1}")
        print("   • Agregando al carrito...")
        self.product_page.add_to_cart()
        print("   ✅ Primer producto agregado exitosamente")
        
        # Go back to home
        print("   • Regresando a la página principal...")
        self.product_page.go_back_to_home()
        
        # Step 3: Add second product (Nokia Lumia 1520)
        print("\n🛒 PASO 3: AGREGANDO SEGUNDO PRODUCTO AL CARRITO")
        print("   • Navegando nuevamente a la categoría 'Phones'...")
        self.home_page.click_phones_category()
        print("   • Seleccionando producto 'Nokia Lumia 1520'...")
        self.home_page.select_product("Nokia lumia 1520")
        
        # Verify we're on product page and add to cart
        product_name_2 = self.product_page.get_product_name()
        print(f"   • Producto seleccionado: {product_name_2}")
        print("   • Agregando al carrito...")
        self.product_page.add_to_cart()
        print("   ✅ Segundo producto agregado exitosamente")
        
        # Step 4: View cart
        print("\n👁️ PASO 4: VISUALIZANDO EL CARRITO DE COMPRAS")
        print("   • Navegando al carrito...")
        self.cart_page.navigate_to_cart()
        
        # Verify cart contents
        cart_items = self.cart_page.get_cart_items()
        cart_count = self.cart_page.get_cart_items_count()
        total_price = self.cart_page.get_total_price()
        
        print("   📊 RESUMEN DEL CARRITO:")
        print(f"   • Número de productos: {cart_count}")
        print(f"   • Productos en el carrito: {cart_items}")
        print(f"   • Precio total: ${total_price}")
        print("   ✅ Carrito verificado exitosamente")
        
        # Assertions for cart verification
        assert cart_count == 2, f"Expected 2 items in cart, but found {cart_count}"
        assert len(cart_items) == 2, f"Expected 2 items in cart list, but found {len(cart_items)}"
        
        # Step 5: Proceed to checkout
        print("\n💳 PASO 5: PROCEDIENDO AL CHECKOUT")
        print("   • Haciendo clic en 'Place Order'...")
        self.cart_page.proceed_to_checkout()
        print("   ✅ Modal de checkout abierto")
        
        # Step 6: Fill purchase form
        print("\n📝 PASO 6: COMPLETANDO FORMULARIO DE COMPRA")
        customer_data = {
            'name': 'Juan Pérez',
            'country': 'México',
            'city': 'Ciudad de México',
            'card': '4111111111111111',
            'month': '12',
            'year': '2025'
        }
        
        print("   📋 DATOS DEL CLIENTE:")
        print(f"   • Nombre: {customer_data['name']}")
        print(f"   • País: {customer_data['country']}")
        print(f"   • Ciudad: {customer_data['city']}")
        print(f"   • Tarjeta: ****-****-****-{customer_data['card'][-4:]}")
        print(f"   • Mes de vencimiento: {customer_data['month']}")
        print(f"   • Año de vencimiento: {customer_data['year']}")
        
        print("   • Llenando formulario...")
        self.checkout_page.fill_purchase_form(customer_data)
        print("   ✅ Formulario completado exitosamente")
        
        # Step 7: Complete purchase
        print("\n🎯 PASO 7: FINALIZANDO LA COMPRA")
        print("   • Procesando el pago...")
        self.checkout_page.complete_purchase()
        print("   ✅ Compra procesada")
        
        # Step 8: Verify purchase success
        print("\n🔍 PASO 8: VERIFICANDO ÉXITO DE LA COMPRA")
        print("   • Validando mensaje de confirmación...")
        assert self.checkout_page.is_purchase_successful(), "Purchase was not successful"
        
        success_message = self.checkout_page.get_success_message()
        order_details = self.checkout_page.get_order_details()
        
        print("   🎉 COMPRA EXITOSA:")
        print(f"   • Mensaje: {success_message}")
        print(f"   • Detalles de la orden: {order_details}")
        
        # Verify success message
        assert "Thank you for your purchase!" in success_message, "Success message not found"
        
        # Close success modal
        print("   • Cerrando modal de confirmación...")
        self.checkout_page.close_success_modal()
        
        print("\n" + "="*80)
        print("🎉 ¡FLUJO DE COMPRA COMPLETADO EXITOSAMENTE!")
        print("✅ Todos los pasos ejecutados correctamente")
        print("="*80)
    
    def test_add_and_remove_from_cart(self):
        """
        Test adding and removing items from cart
        """
        print("\n" + "="*80)
        print("🧪 PRUEBA: AGREGAR Y REMOVER PRODUCTOS DEL CARRITO")
        print("="*80)
        
        # Navigate to home and add a product
        print("\n📍 NAVEGANDO A LA PÁGINA PRINCIPAL")
        print("   • Accediendo a https://demoblaze.com...")
        self.home_page.navigate_to_home()
        print("   ✅ Página principal cargada")
        
        print("\n🛒 AGREGANDO PRODUCTO AL CARRITO")
        print("   • Seleccionando categoría 'Phones'...")
        self.home_page.click_phones_category()
        print("   • Seleccionando producto 'Samsung Galaxy S6'...")
        self.home_page.select_product("Samsung galaxy s6")
        print("   • Agregando al carrito...")
        self.product_page.add_to_cart()
        print("   ✅ Producto agregado exitosamente")
        
        # View cart
        print("\n👁️ VERIFICANDO CARRITO")
        print("   • Navegando al carrito...")
        self.cart_page.navigate_to_cart()
        
        # Verify item was added
        initial_count = self.cart_page.get_cart_items_count()
        print(f"   • Productos en carrito: {initial_count}")
        assert initial_count == 1, f"Expected 1 item in cart, but found {initial_count}"
        print("   ✅ Producto verificado en el carrito")
        
        # Remove item
        print("\n🗑️ REMOVIENDO PRODUCTO DEL CARRITO")
        print("   • Eliminando primer producto...")
        self.cart_page.delete_item(0)
        
        # Verify item was removed
        final_count = self.cart_page.get_cart_items_count()
        print(f"   • Productos restantes: {final_count}")
        assert final_count == 0, f"Expected 0 items in cart after deletion, but found {final_count}"
        print("   ✅ Producto removido exitosamente")
        
        print("\n" + "="*80)
        print("🎉 ¡PRUEBA DE AGREGAR/REMOVER COMPLETADA EXITOSAMENTE!")
        print("="*80)
    
    def test_empty_cart_checkout(self):
        """
        Test attempting to checkout with empty cart
        """
        print("\n" + "="*80)
        print("🧪 PRUEBA: CHECKOUT CON CARRITO VACÍO")
        print("="*80)
        
        # Navigate to home then to cart
        print("\n📍 NAVEGANDO A LA PÁGINA PRINCIPAL")
        print("   • Accediendo a https://demoblaze.com...")
        self.home_page.navigate_to_home()
        print("   ✅ Página principal cargada")
        
        print("\n🛒 VERIFICANDO CARRITO VACÍO")
        print("   • Navegando al carrito...")
        self.cart_page.navigate_to_cart()
        
        # Verify cart is empty
        print("   • Verificando que el carrito esté vacío...")
        assert self.cart_page.is_cart_empty(), "Cart should be empty"
        print("   ✅ Carrito confirmado como vacío")
        
        # Try to proceed to checkout - this should not work or should handle gracefully
        print("\n💳 INTENTANDO CHECKOUT CON CARRITO VACÍO")
        print("   • Intentando proceder al checkout...")
        try:
            self.cart_page.proceed_to_checkout()
            print("   • Modal de checkout abierto (comportamiento inesperado)")
            # If checkout modal opens, close it
            self.checkout_page.close_purchase_modal()
            print("   • Modal cerrado")
        except:
            print("   ✅ Checkout bloqueado correctamente (comportamiento esperado)")
        
        print("\n" + "="*80)
        print("🎉 ¡PRUEBA DE CARRITO VACÍO COMPLETADA!")
        print("="*80)

if __name__ == "__main__":
    # Run tests directly
    pytest.main(["-v", __file__])
