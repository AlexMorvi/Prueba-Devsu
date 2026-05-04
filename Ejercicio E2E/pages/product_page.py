from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class ProductPage(BasePage):
    # Locators
    PRODUCT_NAME = (By.XPATH, "//h2[@class='name']")
    PRODUCT_PRICE = (By.XPATH, "//h3[@class='price-container']")
    PRODUCT_DESCRIPTION = (By.ID, "more-information")
    ADD_TO_CART_BUTTON = (By.XPATH, "//a[contains(text(),'Add to cart')]")
    HOME_LINK = (By.XPATH, "//a[contains(text(),'Home')]")
    
    def __init__(self, driver, timeout: int):
        super().__init__(driver, timeout)
    
    def get_product_name(self):
        """Get the product name"""
        return self.get_text(self.PRODUCT_NAME)
    
    def get_product_price(self):
        """Get the product price"""
        return self.get_text(self.PRODUCT_PRICE)
    
    def add_to_cart(self):
        """Add product to cart"""
        for attempt in range(3):
            self.scroll_into_view(self.ADD_TO_CART_BUTTON)
            self.click(self.ADD_TO_CART_BUTTON)
            if self.accept_alert(timeout=5):
                return

        raise TimeoutException("Add to cart confirmation did not appear")
        
    def go_back_to_home(self):
        """Navigate back to home page"""
        self.click(self.HOME_LINK)
