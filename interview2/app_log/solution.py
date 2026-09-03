def solution():
    totals = {}
    counts = {}

    with open("/root/devops/app.log", "r") as f:
        for line in f:
            parts = line.split('"')
            if len(parts) < 3:
                continue

            request = parts[1].split()
            if len(request) < 2 or request[0] != "POST":
                continue

            status_parts = parts[2].split()
            if not status_parts:
                continue

            try:
                status = int(status_parts[0])
            except ValueError:
                continue

            if 200 <= status < 300:
                path = request[1]
                size = int(status_parts[1])

                counts[path] = counts.get(path, 0) + 1
                totals[path] = totals.get(path, 0) + size

    resources = sorted(
        totals,
        key=lambda path: (-counts[path], path)
    )

    return [f"{path} {totals[path]}" for path in resources]


if __name__ == "__main__":
    print(solution())