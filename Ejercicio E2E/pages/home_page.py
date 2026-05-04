from selenium.webdriver.common.by import By

from pages.base_page import BasePage

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
    
    def __init__(self, driver, base_url: str, timeout: int):
        super().__init__(driver, timeout)
        self.base_url = base_url
    
    def navigate_to_home(self):
        """Navigate to the home page"""
        self.driver.get(self.base_url)
        self.wait_visible(self.CATEGORIES_SECTION)
    
    def click_phones_category(self):
        """Click on Phones category"""
        self.click(self.PHONES_CATEGORY)
        self.wait_visible(self.SAMSUNG_GALAXY_S6)
    
    def click_laptops_category(self):
        """Click on Laptops category"""
        self.click(self.LAPTOPS_CATEGORY)
        self.wait_visible(self.MACBOOK_AIR)
    
    def click_monitors_category(self):
        """Click on Monitors category"""
        self.click(self.MONITORS_CATEGORY)
        self.wait_visible(self.APPLE_MONITOR_24)
    
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
            self.scroll_into_view(product_locators[product_name])
            self.click(product_locators[product_name])
        else:
            raise ValueError(f"Product {product_name} not found in predefined products")
    
    def click_next_page(self):
        """Click next page button"""
        if self.is_present(self.NEXT_BUTTON):
            self.click(self.NEXT_BUTTON)
    
    def click_previous_page(self):
        """Click previous page button"""
        if self.is_present(self.PREVIOUS_BUTTON):
            self.click(self.PREVIOUS_BUTTON)
