import allure
import pytest


def pytest_addoption(parser: pytest.Parser, pluginmanager: pytest.PytestPluginManager):
    """Add options to pytest"""
    parser.addoption(
        "--browser",
        choices=['chrome', 'firefox'],
    )
    parser.addoption(
        "--mobile-only",
        type=bool,
        default=False,
    )


def pytest_configure(config: pytest.Config):
    """Skip tests for firefox if mobile-only option is True"""


def pytest_sessionstart(session: pytest.Session):
    pass


def pytest_runtest_call(item: pytest.Item):
    """Allure dynamic title"""


def pytest_collection_modifyitems(session: pytest.Session, config: pytest.Config, items: list[pytest.Item]):
    """Skip other tests if mobile-only option is True"""


def pytest_sessionfinish(session: pytest.Session):
    pass


def pytest_report_teststatus(report, config):
    pass
