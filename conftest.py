import allure
import pytest


def pytest_addoption(parser: pytest.Parser, pluginmanager: pytest.PytestPluginManager):
    """Add options to pytest"""
    parser.addoption(
        "--browser",
        help="This is browser",
        required=False,
        default="chrome",
        choices=['chrome', 'firefox'],
    )
    parser.addoption(
        "--mobile-only",
        type=bool,
        default=False,
    )


def pytest_configure(config: pytest.Config):
    """Skip tests for firefox if mobile-only option is True"""
    if config.getoption("--mobile-only") and config.getoption("browser") == "firefox":
        raise ValueError("Нет мобильных тестов для firefox")
    if config.getoption("browser") == "chrome":
        config.option.browser = "chrome-latest"


def pytest_sessionstart(session: pytest.Session):
    print()


@pytest.hookimpl(trylast=True, hookwrapper=True)
def pytest_runtest_call(item: pytest.Item):
    """Allure dynamic title"""
    yield
    allure.dynamic.title(" ".join(item.name.split("_")[1:]).capitalize())


def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]):
    """Skip other tests if mobile-only option is True"""

    # for item in items:
    #     if "mobile" not in item.name and config.getoption("--mobile-only"):
    #         item.add_marker(pytest.mark.skip(reason="Mobile tests only"))
    #         item.add_marker(pytest.mark.mobile)
    if config.getoption("--mobile-only"):
        new_items = []
        for item in items:
            if "mobile" in item.name:
                new_items.append(item)
        items[:] = new_items
    items.sort(key=lambda x: x.name, reverse=True)


def pytest_sessionfinish(session: pytest.Session):
    print()


def pytest_report_teststatus(report, config):
    pass


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    # if call.when == "call" and result.passed is False:
    #     make_screenshot()