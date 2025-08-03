from .parse_version import ParseBrowser
from .parse_json import ParseJson
from .request_json import RequestJson
from .query import QueryInstallPath

from pathlib import Path
import platform


class ChromeDriver(object):
    def __init__(self,
                 browser: str | None = 'chrome',
                 update_registry: bool = False,
                 clean_registry: bool = False,
                 update_json_api: bool = False,
                 clean_json_api: bool = False,
                 ) -> None:
        self._query: QueryInstallPath = QueryInstallPath()
        self._request: RequestJson = RequestJson()

        self._parent_dir = Path(__file__).parent
        self._query_cache = self._parent_dir.joinpath(
            'InstalledApps.csv',
        )
        self._json_cache = self._parent_dir.joinpath(
            'chromedriver_info.json',
        )
        if update_registry:
            if self._query_cache.exists():
                self._query.update()
        if clean_registry:
            if self._query_cache.exists():
                self._query.clean()

        if update_json_api:
            if self._json_cache.exists():
                self._query.update()
        if clean_json_api:
            if self._json_cache.exists():
                self._query.clean()

        if not self._query_cache.exists():
            self._query.query()
        if not self._json_cache.exists():
            self._request.request_json()

        # 获取浏览器的版本信息
        self._browser = browser
        self._parse_browser = ParseBrowser(self._browser)
        self._browser_name, self._browser_version = self._parse_browser.browser()

        # 获取平台信息和处理器架构
        self._system = platform.system()
        self._arch = platform.machine()
        # 创建platform
        self._platform = ''
        if self._system.lower() == 'windows':
            if self._arch.lower() == 'amd64':
                self._platform = 'win64'
            if self._arch.lower() == 'amd32':
                self._platform = 'win32'

        # 根据platform和version解析json文件
        self._parse_json = ParseJson(
            platform=self._platform,
            version=self._browser_version,
        )

    def install(self) -> str:
        binary_path = self._parse_json.install()
        return binary_path

__all__ = [
    'ChromeDriver',
]
