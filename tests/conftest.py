import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default=None,
        help="Base URL to test against",
    )
    parser.addoption(
        "--report_dir",
        action="store",
        default=None,
        help="Directory combine report and zip files",
    )


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def report_dir(request):
    return request.config.getoption("--report_dir")
