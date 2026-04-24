# app.py - Python automation script containerized with Docker

import requests
import datetime
import json

urls = [
    "https://google.com",
    "https://github.com",
    "https://python.org",
    "https://docker.com"
]

def check_servers():
    print("=" * 50)
    print("   Dockerized Server Availability Checker")
    print(f"   Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)

    results = []

    for url in urls:
        try:
            response = requests.get(url, timeout=5)
            status = "UP"
            code = response.status_code
        except requests.exceptions.RequestException:
            status = "DOWN"
            code = 0

        results.append({"url": url, "status": status, "code": code})
        print(f"  {status}  {url} — {code}")

    print("=" * 50)
    print(f"  Total checked: {len(results)}")
    print(f"  UP: {sum(1 for r in results if r['status'] == 'UP')}")
    print(f"  DOWN: {sum(1 for r in results if r['status'] == 'DOWN')}")
    print("=" * 50)

if __name__ == "__main__":
    check_servers()
