from __future__ import annotations

from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions, EdgeOptions
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utils import config
from pathlib import Path
import os
import stat


def _chrome_options() -> ChromeOptions:
    options = ChromeOptions()
    if config.headless():
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1400,900")
    options.add_argument("--no-sandbox")
    prefs = {
        "download.default_directory": str(config.download_dir()),
        "download.prompt_for_download": False,
        "safebrowsing.enabled": True,
    }
    options.add_experimental_option("prefs", prefs)
    return options


def _firefox_options() -> FirefoxOptions:
    options = FirefoxOptions()
    if config.headless():
        options.add_argument("-headless")
    options.set_preference("browser.download.folderList", 2)
    options.set_preference("browser.download.dir", str(config.download_dir()))
    options.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv,application/pdf")
    return options


def _edge_options() -> EdgeOptions:
    options = EdgeOptions()
    if config.headless():
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1400,900")
    return options


def create_driver() -> WebDriver:
    config.download_dir().mkdir(parents=True, exist_ok=True)
    remote_url = config.remote_url()
    browser = config.browser()

    if remote_url:
        if browser == "firefox":
            return webdriver.Remote(command_executor=remote_url, options=_firefox_options())
        if browser == "edge":
            return webdriver.Remote(command_executor=remote_url, options=_edge_options())
        return webdriver.Remote(command_executor=remote_url, options=_chrome_options())

    if browser == "firefox":
        return webdriver.Firefox(options=_firefox_options(), service=webdriver.FirefoxService(GeckoDriverManager().install()))
    if browser == "edge":
        return webdriver.Edge(options=_edge_options(), service=webdriver.EdgeService(EdgeChromiumDriverManager().install()))

    chrome_path = _resolve_driver_path(ChromeDriverManager().install(), "chromedriver")
    _ensure_executable(chrome_path)
    return webdriver.Chrome(options=_chrome_options(), service=webdriver.ChromeService(chrome_path))


def _resolve_driver_path(path: str, binary_name: str) -> str:
    candidate = Path(path)
    if candidate.name.startswith(binary_name):
        return str(candidate)

    # webdriver-manager can return a non-executable metadata file; search sibling dir for the real binary.
    search_dir = candidate.parent
    for item in search_dir.iterdir():
        if item.is_file() and item.name == binary_name:
            return str(item)

    # Fallback to any matching binary in nested directories.
    for item in search_dir.rglob(f"{binary_name}*"):
        if item.is_file() and item.name == binary_name:
            return str(item)

    return str(candidate)


def _ensure_executable(path: str) -> None:
    file_path = Path(path)
    if not file_path.exists():
        return
    mode = file_path.stat().st_mode
    if mode & stat.S_IXUSR:
        return
    file_path.chmod(mode | stat.S_IXUSR)
