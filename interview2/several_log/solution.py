from collections import Counter
import os


def solution():
    counts = Counter()
    log_dir = "/root/user/logs"

    for filename in os.listdir(log_dir):
        if not filename.endswith(".log"):
            continue

        with open(os.path.join(log_dir, filename), "r") as f:
            for line in f:
                parts = line.split('"')

                if len(parts) < 3:
                    continue

                request = parts[1].split()
                status = parts[2].split()

                if len(request) < 2 or not status:
                    continue

                method = request[0]
                code = int(status[0])

                if method == "POST" and 400 <= code < 500:
                    hour = parts[0].split(":")[1]
                    counts[hour] += 1

    if not counts:
        return "00 0"

    # Highest count first, lowest hour in case of a tie
    hour = min(counts, key=lambda h: (-counts[h], int(h)))

    return f"{hour} {counts[hour]}"