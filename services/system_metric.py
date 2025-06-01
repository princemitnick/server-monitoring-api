import datetime

import psutil
import platform
import time
from db import mongodb

async def save_metrics(metrics: dict):
    metrics["timestamp"] = datetime.datetime.utcnow()
    await mongodb.metrics_collection.insert_one(metrics)

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    virtual = psutil.virtual_memory()
    swap = psutil.swap_memory()

    return {
        "virtual": {
            "total": virtual.total,
            "available": virtual.available,
            "used": virtual.used,
            "percent": virtual.percent
        },
        "swap": {
            "total": swap.total,
            "used": swap.used,
            "percent": swap.percent
        }
    }

def get_network_bandwith():
    net1 = psutil.net_io_counters()
    time.sleep(2)
    net2 = psutil.net_io_counters()
    upload = net2.bytes_sent - net1.bytes_sent
    download = net2.bytes_recv - net1.bytes_recv
    return {
        "upload_bytes_per_sec": upload,
        "download_bytes_per_sec": download
    }

def get_running_services():
    system = platform.system().lower()
    services = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            services.append(proc.info['name'])
        except Exception:
            continue
    return services

