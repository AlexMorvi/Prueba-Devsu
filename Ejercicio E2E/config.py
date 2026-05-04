from dataclasses import dataclass
import os


def _env_bool(name: str, default: bool = False) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "y", "on"}


@dataclass(frozen=True)
class Settings:
    base_url: str
    headless: bool
    browser: str
    explicit_wait: int
    page_load_timeout: int
    script_timeout: int
    window_width: int
    window_height: int


def load_settings() -> Settings:
    return Settings(
        base_url=os.getenv("BASE_URL", "https://www.demoblaze.com/"),
        headless=_env_bool("HEADLESS", False),
        browser=os.getenv("BROWSER", "auto").lower(),
        explicit_wait=int(os.getenv("EXPLICIT_WAIT", "15")),
        page_load_timeout=int(os.getenv("PAGE_LOAD_TIMEOUT", "30")),
        script_timeout=int(os.getenv("SCRIPT_TIMEOUT", "30")),
        window_width=int(os.getenv("WINDOW_WIDTH", "1920")),
        window_height=int(os.getenv("WINDOW_HEIGHT", "1080")),
    )
