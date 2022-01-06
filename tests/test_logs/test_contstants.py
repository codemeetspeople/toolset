import pytest

from toolset.logs.constants import LogSeverity


@pytest.mark.parametrize('property_name', [
    'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'
])
def test_log_severity_properties(property_name):
    assert hasattr(LogSeverity, property_name)
    assert getattr(LogSeverity, property_name) == property_name.lower()


def test_log_severity():
    assert LogSeverity.all() == ('debug', 'info', 'warning', 'error', 'critical')
