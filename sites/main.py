import os
import subprocess
import sys
from pathlib import Path


EXCLUDE = {
    "__init__.py",
    "main.py",
}
SITES_DIR = Path(__file__).resolve().parent
REPO_ROOT = SITES_DIR.parent
SCRAPER_TIMEOUT_SECONDS = int(os.getenv("SCRAPER_TIMEOUT_SECONDS", "120"))
MAX_LOG_LENGTH = 4000


def truncate_output(content, limit=MAX_LOG_LENGTH):
    if not content:
        return "No output captured."

    content = content.strip()
    if len(content) <= limit:
        return content

    return content[:limit] + "\n...[truncated]"


def run_scraper(script_path):
    return subprocess.run(
        [sys.executable, str(script_path)],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
        timeout=SCRAPER_TIMEOUT_SECONDS,
    )


def main():
    for site in sorted(os.listdir(SITES_DIR)):
        if not site.endswith(".py") or site in EXCLUDE:
            continue

        script_path = SITES_DIR / site

        try:
            action = run_scraper(script_path)
        except subprocess.TimeoutExpired:
            print(f"Timeout scraping {site}")
            continue

        if action.returncode == 0:
            print(f"Success scraping {site}")
            continue

        print(f"Error scraping {site}")
        print(truncate_output(action.stderr))


class Scraper:
    def __init__(self, exclude=None):
        self.exclude = set(EXCLUDE if exclude is None else exclude)

    def run(self):
        for site in sorted(os.listdir(SITES_DIR)):
            if not site.endswith(".py") or site in self.exclude:
                continue

            script_path = SITES_DIR / site

            try:
                action = run_scraper(script_path)
            except subprocess.TimeoutExpired:
                print(f"Timeout scraping {site}")
                continue

            if action.returncode == 0:
                print(f"Success scraping {site} with exit code {action.returncode}")
                continue

            print(f"Error scraping {site} with exit code {action.returncode}")
            print(truncate_output(action.stderr))


if __name__ == "__main__":
    main()
