import pytest
from services.system_metric import save_metrics

from db import mongodb

@pytest.mark.asyncio
async def test_save_metrics():
    test_data =  {
        "cpu": 33,
        "memory": {
            "virtual": {"used": 1000, "total": 8000, "percent":12.5, "available": 7000},
            "swap": {"used": 0, "total": 2000, "percent": 0}
        },
        "network": {"upload_bytes_per_sec": 1000, "download_bytes_per_sec": 2000},
        "running_services": ["nginx", "docker"]
    }
    result = await save_metrics(test_data)
    return result.acknowledge is True

