import allure
import pytest


@pytest.fixture()
def browser(request: pytest.FixtureRequest):
    # assert request.config.getoption("browser") == "chrome"
    assert request.param == "chrome-latest"
    print()


def pytest_generate_tests(metafunc: pytest.Metafunc):
    if 'browser' in metafunc.fixturenames:
        metafunc.parametrize("browser", [metafunc.config.getoption("--browser")], indirect=True)


@pytest.mark.parametrize("some", [1, 2, 3])
def test_desktop_page(browser, request, some):
    assert False


def test_mobile_page(browser):
    pass
