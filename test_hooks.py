import allure
import pytest


@pytest.fixture()
def browser(request: pytest.FixtureRequest):
    pass


def pytest_generate_tests(metafunc: pytest.Metafunc):
    if 'browser' in metafunc.fixturenames:
        metafunc.parametrize("browser", [metafunc.config.getoption("--browser")], indirect=True)


def test_desktop_page(browser, request):
    pass


def test_mobile_page(browser):
    pass
