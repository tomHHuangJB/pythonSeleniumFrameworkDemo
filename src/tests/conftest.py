import os
import pytest

from utils.driver_factory import create_driver
from utils import config
from utils import jira_client


def pytest_addoption(parser):
    parser.addoption("--base-url", action="store", default=config.base_url())
    parser.addoption("--browser", action="store", default=config.browser())
    parser.addoption("--headless", action="store", default=str(config.headless()).lower())
    parser.addoption("--remote-url", action="store", default=config.remote_url())


@pytest.fixture(scope="session")
def base_url(pytestconfig) -> str:
    return pytestconfig.getoption("--base-url")


@pytest.fixture(scope="session")
def driver(pytestconfig):
    os.environ["BASE_URL"] = pytestconfig.getoption("--base-url")
    os.environ["BROWSER"] = pytestconfig.getoption("--browser")
    os.environ["HEADLESS"] = pytestconfig.getoption("--headless")
    os.environ["REMOTE_URL"] = pytestconfig.getoption("--remote-url")

    driver = create_driver()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when != "call" or not report.failed or getattr(report, "wasxfail", False):
        return

    summary = f"Test failed: {item.nodeid}"
    description = "\n".join(
        [
            f"Test: {item.nodeid}",
            f"Base URL: {config.base_url()}",
            f"Browser: {config.browser()}",
            f"Headless: {config.headless()}",
            f"Remote URL: {config.remote_url() or 'local'}",
            "",
            str(report.longrepr),
        ]
    )
    jira_client.create_issue(summary, description)
