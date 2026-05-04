import re
from pathlib import Path

import pytest

from config import load_settings
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from utils.driver_manager import DriverManager
from utils.logging_config import configure_logging
from tests.data import CUSTOMER_DATA


@pytest.fixture(scope="session", autouse=True)
def _configure_logging() -> None:
    configure_logging()


@pytest.fixture(scope="session")
def settings():
    return load_settings()


@pytest.fixture
def driver(settings, request):
    manager = DriverManager(settings)
    driver = manager.create()
    request.node.driver = driver
    yield driver
    manager.quit()


@pytest.fixture
def home_page(driver, settings):
    return HomePage(driver, settings.base_url, settings.explicit_wait)


@pytest.fixture
def product_page(driver, settings):
    return ProductPage(driver, settings.explicit_wait)


@pytest.fixture
def cart_page(driver, settings):
    return CartPage(driver, settings.explicit_wait)


@pytest.fixture
def checkout_page(driver, settings):
    return CheckoutPage(driver, settings.explicit_wait)


@pytest.fixture
def customer_data():
    return CUSTOMER_DATA.copy()


def _sanitize_filename(value: str) -> str:
    value = re.sub(r"[^a-zA-Z0-9_.-]", "_", value)
    return value.strip("_") or "test"


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when != "call" or not report.failed:
        return

    driver = getattr(item, "driver", None)
    if driver is None:
        return

    root_dir = Path(item.config.rootpath)
    screenshots_dir = root_dir / "reports" / "screenshots"
    screenshots_dir.mkdir(parents=True, exist_ok=True)
    file_name = _sanitize_filename(item.nodeid) + ".png"
    screenshot_path = screenshots_dir / file_name
    driver.save_screenshot(str(screenshot_path))

    pytest_html = item.config.pluginmanager.getplugin("html")
    if pytest_html:
        extra = getattr(report, "extra", [])
        extra.append(pytest_html.extras.image(str(screenshot_path)))

        try:
            extra.append(pytest_html.extras.url(driver.current_url))
        except Exception:
            pass

        try:
            logs = driver.get_log("browser")
        except Exception:
            logs = []

        if logs:
            formatted = "\n".join(
                f"[{entry.get('level')}] {entry.get('message')}" for entry in logs
            )
            extra.append(pytest_html.extras.text(formatted, "browser.log"))

        report.extra = extra
