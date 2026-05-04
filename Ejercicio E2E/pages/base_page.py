import logging
from typing import Optional

from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver, timeout: int):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)
        self.logger = logging.getLogger(self.__class__.__name__)

    def wait_visible(self, locator, timeout: Optional[int] = None):
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_present(self, locator, timeout: Optional[int] = None):
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_clickable(self, locator, timeout: Optional[int] = None):
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_invisible(self, locator, timeout: Optional[int] = None) -> bool:
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def click(self, locator) -> None:
        for attempt in range(3):
            try:
                element = self.wait_clickable(locator)
                element.click()
                return
            except StaleElementReferenceException:
                if attempt == 2:
                    raise

    def type(self, locator, text: str) -> None:
        element = self.wait_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator) -> str:
        for attempt in range(3):
            try:
                element = self.wait_visible(locator)
                return element.text
            except StaleElementReferenceException:
                if attempt == 2:
                    raise

    def is_present(self, locator) -> bool:
        return len(self.driver.find_elements(*locator)) > 0

    def is_visible(self, locator, timeout: int = 2) -> bool:
        try:
            self.wait_visible(locator, timeout=timeout)
            return True
        except TimeoutException:
            return False

    def scroll_into_view(self, locator) -> None:
        element = self.wait_present(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element,
        )

    def accept_alert(self, timeout: int = 5) -> bool:
        try:
            alert = WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            alert.accept()
            return True
        except TimeoutException:
            return False
