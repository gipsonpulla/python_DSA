from collections import defaultdict
from datetime import datetime, timedelta
import os


def solution(threshold: int, duration: int):
    log_dir = "/var/logs/server"

    current_date = datetime.strptime(
        "15/Sep/2021:00:00:00 +0000",
        "%d/%b/%Y:%H:%M:%S %z"
    )
    start_date = current_date - timedelta(days=duration)

    requests = defaultdict(list)

    for root, _, files in os.walk(log_dir):
        for filename in files:
            if not filename.endswith(".log"):
                continue

            with open(os.path.join(root, filename), "r") as f:
                for line in f:
                    parts = line.split('"')
                    if len(parts) < 3:
                        continue

                    timestamp = datetime.strptime(
                        parts[0].strip(" []"),
                        "%d/%b/%Y:%H:%M:%S %z"
                    )

                    if not (start_date <= timestamp <= current_date):
                        continue

                    request = parts[1].split()
                    if len(request) < 2 or request[0] != "POST":
                        continue

                    fields = parts[2].split()
                    if len(fields) < 2:
                        continue

                    ip = fields[0]
                    status = int(fields[1])

                    if 200 <= status < 300:
                        requests[ip].append(timestamp)

    suspicious = []

    for ip, times in requests.items():
        times.sort()
        left = 0

        for right in range(len(times)):
            while times[right] - times[left] > timedelta(minutes=15):
                left += 1

            if right - left + 1 > threshold:
                suspicious.append(ip)
                break

    return sorted(suspicious)
