import asyncio

from fastapi import  FastAPI, WebSocket, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from services.system_metric import (
    get_cpu_usage,
    get_memory_usage,
    get_network_bandwith,
    get_running_services
)
from auth.token import verify_token

app = FastAPI(title="System Monitoring API")

@app.get("/metrics")
def read_metrics():
    return {
        "cpu": get_cpu_usage(),
        "memory": get_memory_usage(),
        "network": get_network_bandwith(),
        "running_services": get_running_services(),
    }

@app.websocket("/ws/metrics")
async  def websocket_metrics(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            metrics = {
                "cpu": get_cpu_usage(),
                "memory": get_memory_usage(),
                "network": get_network_bandwith(),
                "running_services": get_running_services(),
            }
            await  websocket.send_json(metrics)
            await asyncio.sleep(2)
    except Exception:
        await websocket.close()