# Simple WebDriver Manager for E2E Tests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

class DriverManager:
    """Simple WebDriver manager with automatic driver downloads"""
    
    def __init__(self):
        self.driver = None
        self.browser_type = None
    
    def setup_driver(self, headless=False):
        """Setup WebDriver with automatic driver management"""
        print("🚀 Setting up browser...")
        
        # Strategy 1: Try Chrome with WebDriver Manager
        try:
            print("🔍 Trying Chrome with WebDriver Manager...")
            chrome_options = self._get_chrome_options(headless)
            service = ChromeService(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            self.browser_type = "Chrome (WebDriver Manager)"
            self._configure_driver()
            print("✅ Chrome configured successfully!")
            return self.driver
        except Exception as e:
            print(f"❌ Chrome with WebDriver Manager failed: {str(e)}")
        
        # Strategy 2: Try Chrome without service (system PATH)
        try:
            print("🔍 Trying Chrome from system PATH...")
            chrome_options = self._get_chrome_options(headless)
            self.driver = webdriver.Chrome(options=chrome_options)
            self.browser_type = "Chrome (System PATH)"
            self._configure_driver()
            print("✅ Chrome configured successfully!")
            return self.driver
        except Exception as e:
            print(f"❌ Chrome from system PATH failed: {str(e)}")
        
        # Strategy 3: Try Edge with WebDriver Manager
        try:
            print("🔍 Trying Edge with WebDriver Manager...")
            edge_options = self._get_edge_options(headless)
            service = EdgeService(EdgeChromiumDriverManager().install())
            self.driver = webdriver.Edge(service=service, options=edge_options)
            self.browser_type = "Edge (WebDriver Manager)"
            self._configure_driver()
            print("✅ Edge configured successfully!")
            return self.driver
        except Exception as e:
            print(f"❌ Edge with WebDriver Manager failed: {str(e)}")
        
        # Strategy 4: Try Edge without service (system PATH)
        try:
            print("🔍 Trying Edge from system PATH...")
            edge_options = self._get_edge_options(headless)
            self.driver = webdriver.Edge(options=edge_options)
            self.browser_type = "Edge (System PATH)"
            self._configure_driver()
            print("✅ Edge configured successfully!")
            return self.driver
        except Exception as e:
            print(f"❌ Edge from system PATH failed: {str(e)}")
        
        # If all strategies fail, provide clear error
        raise Exception("""
❌ Could not setup any browser!

SOLUTION STEPS:
1. Install Google Chrome: https://www.google.com/chrome/
2. Or install Microsoft Edge: https://www.microsoft.com/edge
3. Ensure good internet connection for first run
4. Run: pip install webdriver-manager

If still failing, the browser may be installed but not in system PATH.
        """)
    
    def _get_chrome_options(self, headless=False):
        """Get optimized Chrome options"""
        options = ChromeOptions()
        
        if headless:
            options.add_argument("--headless")
        
        # Essential options for stability
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        
        # Suppress unnecessary messages for clean output
        options.add_argument("--log-level=3")
        options.add_argument("--silent")
        options.add_argument("--disable-logging")
        options.add_argument("--disable-background-networking")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_experimental_option('useAutomationExtension', False)
        
        return options
    
    def _get_edge_options(self, headless=False):
        """Get optimized Edge options"""
        options = EdgeOptions()
        
        if headless:
            options.add_argument("--headless")
        
        # Essential options for stability  
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        
        # Suppress unnecessary messages for clean output
        options.add_argument("--log-level=3")
        options.add_argument("--silent")
        options.add_argument("--disable-logging")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_experimental_option('useAutomationExtension', False)
        
        return options
    
    def _configure_driver(self):
        """Configure the driver after successful initialization"""
        if self.driver:
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)
    
    def quit_driver(self):
        """Close the browser and quit the driver"""
        if self.driver:
            try:
                self.driver.quit()
                print(f"🔚 {self.browser_type} browser closed")
            except Exception as e:
                print(f"⚠️ Error closing browser: {e}")
            finally:
                self.driver = None

class BasePage:
    """Base page with common WebDriver utilities"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
    
    def click_element(self, locator):
        """Click on an element with wait"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def send_keys_to_element(self, locator, text):
        """Send keys to an element with wait"""
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)
    
    def wait_for_element(self, locator):
        """Wait for element to be present"""
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def wait_for_element_clickable(self, locator):
        """Wait for element to be clickable"""
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    def get_text(self, locator):
        """Get text from element"""
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element.text
    
    def is_element_present(self, locator):
        """Check if element is present"""
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except:
            return False
    
    def scroll_to_element(self, locator):
        """Scroll to element"""
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.5)
    
    def accept_alert(self):
        """Accept browser alert"""
        try:
            alert = self.wait.until(EC.alert_is_present())
            alert.accept()
            return True
        except:
            return False