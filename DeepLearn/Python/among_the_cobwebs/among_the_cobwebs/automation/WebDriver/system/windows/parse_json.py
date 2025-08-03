import json
import ijson
from pathlib import Path

class ParseJson(object):
    def __init__(self,
                 system: str,
                 arch: str,
                 version: str,
                 ) -> None:
        self._version = version
        self._parent_dir = Path(__file__).parent
        self._cache_json_path = self._parent_dir.joinpath(
            'chromedriver_info.json',
        )

    @staticmethod
    def parse_json(cache_json_path) -> str:
        with open(cache_json_path, 'r', encoding='utf-8') as f:







