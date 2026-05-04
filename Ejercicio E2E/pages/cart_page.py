from dataclasses import dataclass
from typing import List, Optional

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage


@dataclass(frozen=True)
class CartItem:
    name: str
    price: int

class CartPage(BasePage):
    # Locators
    CART_LINK = (By.ID, "cartur")
    CART_ITEMS = (By.XPATH, "//tbody[@id='tbodyid']/tr")
    ITEM_NAME = (By.XPATH, ".//td[2]")
    ITEM_PRICE = (By.XPATH, ".//td[3]")
    DELETE_BUTTON = (By.XPATH, ".//td[4]/a")
    TOTAL_PRICE = (By.ID, "totalp")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Place Order')]")
    
    def __init__(self, driver, timeout: int):
        super().__init__(driver, timeout)
    
    def navigate_to_cart(self):
        """Navigate to cart page"""
        self.click(self.CART_LINK)
        self.wait_visible(self.PLACE_ORDER_BUTTON)
    
    def get_cart_items(self) -> List[CartItem]:
        """Get all items in cart"""
        for attempt in range(3):
            try:
                items: List[CartItem] = []
                for row in self._get_cart_rows():
                    name = row.find_element(*self.ITEM_NAME).text
                    price = row.find_element(*self.ITEM_PRICE).text
                    items.append(CartItem(name=name, price=self._parse_price(price)))
                return items
            except StaleElementReferenceException:
                if attempt == 2:
                    raise
        return []
    
    def get_cart_items_count(self) -> int:
        """Get number of items in cart"""
        for attempt in range(3):
            try:
                return len(self._get_cart_rows())
            except StaleElementReferenceException:
                if attempt == 2:
                    raise
        return 0
    
    def get_total_price(self) -> int:
        """Get total price from cart"""
        total = self.get_text(self.TOTAL_PRICE)
        return self._parse_price(total)
    
    def delete_item(self, item_index: int = 0) -> None:
        """Delete an item from cart by index"""
        for attempt in range(3):
            try:
                items = self._get_cart_rows()
                if not items or item_index >= len(items):
                    return

                before_count = len(items)
                delete_btn = items[item_index].find_element(*self.DELETE_BUTTON)
                delete_btn.click()
                WebDriverWait(self.driver, self.timeout).until(
                    lambda driver: self.get_cart_items_count() == before_count - 1
                )
                return
            except StaleElementReferenceException:
                if attempt == 2:
                    raise
    
    def proceed_to_checkout(self):
        """Click Place Order button"""
        self.scroll_into_view(self.PLACE_ORDER_BUTTON)
        self.click(self.PLACE_ORDER_BUTTON)
    
    def is_cart_empty(self) -> bool:
        """Check if cart is empty"""
        return self.get_cart_items_count() == 0

    def wait_for_items_count(self, expected_min: int, timeout: Optional[int] = None) -> None:
        """Wait until cart has at least the expected number of items"""
        WebDriverWait(self.driver, timeout or self.timeout).until(
            lambda driver: self.get_cart_items_count() >= expected_min
        )

    def _get_cart_rows(self):
        for attempt in range(3):
            try:
                return self.driver.find_elements(*self.CART_ITEMS)
            except StaleElementReferenceException:
                if attempt == 2:
                    raise
        return []

    @staticmethod
    def _parse_price(value: str) -> int:
        digits = "".join(ch for ch in value if ch.isdigit())
        return int(digits) if digits else 0
