from selenium.webdriver.common.by import By

from pages.base_page import BasePage

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
    
    def __init__(self, driver, timeout: int):
        super().__init__(driver, timeout)
    
    def fill_purchase_form(self, customer_data):
        """Fill the purchase form with customer data"""
        self.wait_visible(self.PURCHASE_MODAL)

        self.type(self.NAME_FIELD, customer_data["name"])
        self.type(self.COUNTRY_FIELD, customer_data["country"])
        self.type(self.CITY_FIELD, customer_data["city"])
        self.type(self.CREDIT_CARD_FIELD, customer_data["card"])
        self.type(self.MONTH_FIELD, customer_data["month"])
        self.type(self.YEAR_FIELD, customer_data["year"])
    
    def complete_purchase(self):
        """Click the Purchase button to complete the order"""
        self.click(self.PURCHASE_BUTTON)
        self.wait_visible(self.SUCCESS_MODAL)
    
    def is_purchase_successful(self) -> bool:
        """Check if purchase was successful by looking for success message"""
        return self.is_visible(self.SUCCESS_MESSAGE, timeout=5)
    
    def get_success_message(self):
        """Get the success message text"""
        return self.get_text(self.SUCCESS_MESSAGE)
    
    def get_order_details(self):
        """Get order details from success modal"""
        return self.get_text(self.ORDER_DETAILS)
    
    def close_success_modal(self):
        """Close the success modal"""
        self.click(self.OK_BUTTON)
        self.wait_invisible(self.SUCCESS_MODAL)
    
    def close_purchase_modal(self):
        """Close the purchase modal"""
        self.click(self.CLOSE_BUTTON)
        self.wait_invisible(self.PURCHASE_MODAL)

    def wait_for_purchase_modal(self):
        """Wait until purchase modal is open"""
        self.wait_visible(self.PURCHASE_MODAL)

    def is_purchase_modal_open(self, timeout: int = 3) -> bool:
        """Check if the purchase modal is open"""
        return self.is_visible(self.PURCHASE_MODAL, timeout=timeout)
