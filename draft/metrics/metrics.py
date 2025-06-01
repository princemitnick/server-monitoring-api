import psutil

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)


print(get_cpu_usage())