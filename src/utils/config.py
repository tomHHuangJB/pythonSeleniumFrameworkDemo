import os
from pathlib import Path


def get(key: str, default: str) -> str:
    value = os.getenv(key.upper().replace(".", "_")) or os.getenv(key)
    return value if value else default


def base_url() -> str:
    return get("base.url", "http://localhost:5173")


def browser() -> str:
    return get("browser", "chrome").lower()


def headless() -> bool:
    return get("headless", "false").lower() == "true"


def remote_url() -> str:
    return get("remote.url", "")


def download_dir() -> Path:
    return Path.cwd() / "downloads"
