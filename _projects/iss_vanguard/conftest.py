import pytest

def pytest_addoption(parser):
    parser.addoption('--monte-carlo', action='store_true', default=False)
    parser.addoption('--monte-carlo-create', action='store_true', default=False)

@pytest.fixture(scope='session')
def monte_carlo_update(request):
    return request.config.getoption('--monte-carlo')

@pytest.fixture(scope='session')
def monte_carlo_create(request):
    return request.config.getoption('--monte-carlo-create')
