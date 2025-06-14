from services.system_metric import (
    get_cpu_usage,
    get_memory_usage,
    get_network_bandwith
)

from unittest.mock import patch

def test_get_cpu_usage():
    with patch("services.system_metric.psutil.cpu_percent", return_value=42.0):
        result = get_cpu_usage()
        assert result == 42.0

def test_get_memory_usage():
    fake_virtual = type('vmem', (object,),{
        'total': 8000, 'available': 4000, 'used': 4000, 'percent': 50
    })()
    fake_swap = type('smem', (object,),{
        'total': 2000, 'used': 500, 'percent': 25
    })()

    with patch("services.system_metric.psutil.virtual_memory", return_value=fake_virtual):
        with patch("services.system_metric.psutil.swap_memory", return_value=fake_swap):
            result = get_memory_usage()
            assert result["virtual"]["percent"] == 50
            assert result["swap"]["used"] == 500


