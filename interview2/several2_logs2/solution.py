from typing import List
from collections import defaultdict
from datetime import datetime, timedelta
import os


def solution(threshold: int, duration: int) -> List[str]:
    #log_dir = "/var/logs/server"
    log_dir = "/Users/gipsonpulla/gipson_leet/python_DSA/interview2/several2_logs2/logs"
    current_date = datetime.strptime(
        "15/Sep/2021:00:00:00 +0000",
        "%d/%b/%Y:%H:%M:%S %z"
    )

    start_date = current_date - timedelta(days=duration)

    # IP -> list of timestamps of successful POST requests
    requests = defaultdict(list)

    # Search all .log files, including subdirectories
    for root, _, files in os.walk(log_dir):
        #print (root)
        print (files)
        for filename in files:
            if not filename.endswith(".log"):
                continue

            filepath = os.path.join(root, filename)

            with open(filepath, "r") as f:
                for line in f:
                    parts = line.split('"')

                    if len(parts) < 3:
                        continue

                    # Parse timestamp
                    timestamp = datetime.strptime(
                        parts[0].strip(" []"),
                        "%d/%b/%Y:%H:%M:%S %z"
                    )

                    # Only consider the requested date range
                    if not (start_date <= timestamp <= current_date):
                        continue

                    # Parse request
                    request = parts[1].split()

                    if len(request) < 1 or request[0] != "POST":
                        continue

                    # After the closing quote:
                    # IP STATUS SIZE
                    fields = parts[2].split()

                    if len(fields) < 2:
                        continue

                    ip = fields[0]
                    status = int(fields[1])

                    # Successful POST = 2xx
                    if 200 <= status < 300:
                        requests[ip].append(timestamp)

    suspicious = []

    # Check each IP for a 15-minute window
    for ip, timestamps in requests.items():
        timestamps.sort()

        left = 0

        for right in range(len(timestamps)):
            # Keep the window <= 15 minutes
            while timestamps[right] - timestamps[left] > timedelta(minutes=15):
                left += 1

            count = right - left + 1

            if count > threshold:
                suspicious.append(ip)
                break
            print (suspicious)

    return sorted(suspicious)


if __name__ == '__main__':
    print(solution(5, 30))