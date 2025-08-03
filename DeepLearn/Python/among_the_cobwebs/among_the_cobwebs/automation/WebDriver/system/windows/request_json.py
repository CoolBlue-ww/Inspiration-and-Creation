import requests
from pathlib import Path
import json


class RequestJson(object):
    def __init__(self) -> None:
        self._chrome_json = 'https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json'
        self._parent_dir = Path(__file__).parent
        self._cache_json_path = self._parent_dir.joinpath(
            'chromedriver_info.json',
        )

    def request_json(self) -> None:
        response = requests.get(self._chrome_json, timeout=10)
        response.raise_for_status()
        content = response.json()
        with open(self._cache_json_path, 'w', encoding='utf-8') as f:
            json.dump(
                content,
                f,
                ensure_ascii=False,
                indent=4,
            )
        return None

    def update(self) -> None:
        self._cache_json_path.unlink(missing_ok=True)
        self.request_json()
        return None

    def clean(self) -> None:
        self._cache_json_path.unlink(
            missing_ok=True,
        )
        return None

_all__ = [
    'RequestJson',
]
