import pandas as pd
import subprocess
from pathlib import Path


class ParseBrowser(object):
    def __init__(self,
                 browser: str | None = None,
                 ) -> None:
        self._browser = browser.lower()
        self._parent_dir = Path(__file__).parent
        self._csv_path = self._parent_dir.joinpath(
            'InstalledApps.csv'
        )
        self._csv_data = pd.read_csv(
            self._csv_path,
        )

    @staticmethod
    def parse_version(binary_path: str) -> str:
        powershell_command = f'[System.Diagnostics.FileVersionInfo]::GetVersionInfo("{binary_path}").FileVersion'
        result = subprocess.run(
            ["powershell", "-Command", powershell_command],
            capture_output=True,  # 捕获输出
            text=True,  # 返回字符串格式的输出
            check=True  # 如果命令失败，抛出异常
        )
        browser_version = result.stdout.strip()
        return browser_version

    def browser(self) -> tuple[str, str] | None:
        # 不区分大小写，模糊匹配第一列的内容
        mask = self._csv_data.iloc[:, 0].astype(str).str.contains(self._browser, case=False, na=False)
        matched_rows = self._csv_data[mask]
        name_list = matched_rows['Name'].tolist()
        installed_path_list = matched_rows['InstallPath'].tolist()
        for name, installed_path in zip(name_list, installed_path_list):
            installed_path = Path(installed_path)
            binary_path = ''
            if self._browser == 'chrome':
                binary_path = Path(installed_path).joinpath(
                    'chrome.exe'
                )
            if self._browser == 'edge':
                binary_path = Path(installed_path).joinpath(
                    'msedge.exe'
                )
            if self._browser == 'firefox':
                binary_path = Path(installed_path).joinpath(
                    'firefox.exe'
                )
            if binary_path.exists():
                browser_version = self.parse_version(
                    str(binary_path)
                )
                print(browser_version)
                return name, browser_version
        return None


__all__ = [
    'ParseBrowser',
]
