import logging
from typing import Callable, List, Tuple

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from config import Settings


class DriverManager:
    """WebDriver factory with safe fallbacks and explicit configuration."""

    def __init__(self, settings: Settings):
        self.settings = settings
        self.logger = logging.getLogger(self.__class__.__name__)
        self.driver = None

    def create(self):
        strategies = self._build_strategies()
        errors: List[str] = []

        for name, factory in strategies:
            try:
                self.logger.info("Starting browser strategy: %s", name)
                driver = factory()
                self._configure_driver(driver)
                self.driver = driver
                self.logger.info("Browser ready: %s", name)
                return driver
            except Exception as exc:
                message = f"{name}: {exc}"
                errors.append(message)
                self.logger.warning("Strategy failed: %s", message)

        details = "\n".join(errors) or "No strategies configured"
        raise RuntimeError(
            "Could not start any browser.\n"
            "Check that Chrome or Edge is installed and that network access is available\n"
            f"when using WebDriver Manager.\n\nErrors:\n{details}"
        )

    def quit(self) -> None:
        if not self.driver:
            return
        try:
            self.driver.quit()
        finally:
            self.driver = None

    def _build_strategies(self) -> List[Tuple[str, Callable[[], webdriver.Remote]]]:
        browser = self.settings.browser
        strategies: List[Tuple[str, Callable[[], webdriver.Remote]]] = []

        if browser in {"auto", "chrome"}:
            strategies.extend(
                [
                    ("chrome-path", self._create_chrome_path),
                    ("chrome-manager", self._create_chrome_manager),
                ]
            )

        if browser in {"auto", "edge"}:
            strategies.extend(
                [
                    ("edge-path", self._create_edge_path),
                    ("edge-manager", self._create_edge_manager),
                ]
            )

        return strategies

    def _configure_driver(self, driver: webdriver.Remote) -> None:
        driver.set_page_load_timeout(self.settings.page_load_timeout)
        driver.set_script_timeout(self.settings.script_timeout)
        driver.set_window_size(self.settings.window_width, self.settings.window_height)

    def _chrome_options(self) -> ChromeOptions:
        options = ChromeOptions()
        if self.settings.headless:
            options.add_argument("--headless")

        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument(
            f"--window-size={self.settings.window_width},{self.settings.window_height}"
        )

        options.add_argument("--log-level=3")
        options.add_argument("--disable-logging")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_experimental_option("useAutomationExtension", False)
        options.set_capability("goog:loggingPrefs", {"browser": "ALL"})
        return options

    def _edge_options(self) -> EdgeOptions:
        options = EdgeOptions()
        if self.settings.headless:
            options.add_argument("--headless")

        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument(
            f"--window-size={self.settings.window_width},{self.settings.window_height}"
        )

        options.add_argument("--log-level=3")
        options.add_argument("--disable-logging")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_experimental_option("useAutomationExtension", False)
        options.set_capability("goog:loggingPrefs", {"browser": "ALL"})
        return options

    def _create_chrome_manager(self):
        service = ChromeService(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=self._chrome_options())

    def _create_chrome_path(self):
        return webdriver.Chrome(options=self._chrome_options())

    def _create_edge_manager(self):
        service = EdgeService(EdgeChromiumDriverManager().install())
        return webdriver.Edge(service=service, options=self._edge_options())

    def _create_edge_path(self):
        return webdriver.Edge(options=self._edge_options())