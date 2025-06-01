from unittest.mock import patch
from ..metrics import get_cpu_usage

@patch("metrics.psutil.cpu_percent", return_value=47.5)
def test_get_cpu_usage(mock_cpu_percent):
    result = get_cpu_usage()

    assert result == 47.5
    mock_cpu_percent.assert_called_once_with(interval=1)