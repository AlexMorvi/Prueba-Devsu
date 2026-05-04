import logging
import os
from typing import Optional


def configure_logging(level_name: Optional[str] = None) -> None:
    value = level_name or os.getenv("LOG_LEVEL", "INFO")
    level = getattr(logging, value.upper(), logging.INFO)
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
        datefmt="%H:%M:%S",
    )
    logging.getLogger("selenium").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)
