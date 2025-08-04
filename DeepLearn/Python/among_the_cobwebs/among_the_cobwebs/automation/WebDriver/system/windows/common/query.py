import subprocess
from pathlib import Path


class QueryInstallPath(object):
    def __init__(self) -> None:
        self._parent_dir = Path(
            __file__
        ).parent
        self._query_ps1_path = self._parent_dir.joinpath(
            'query.ps1'
        )
        self._query_result_path = self._parent_dir.joinpath(
            'InstalledApps.csv',
        )

    def query(self) -> None:
        subprocess.run(
            ['powershell', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', self._query_ps1_path],
            capture_output=True,  # 捕获输出
            text=True,  # 返回字符串格式的输出
            check=True  # 如果命令失败，抛出异常
        )
        return None

    def update(self) -> None:
        self._query_result_path.unlink(
            missing_ok=True,
        )
        self.query()
        return None

    def clean(self) -> None:
        self._query_result_path.unlink(
            missing_ok=True,
        )
        return None

__all__ = [
    'QueryInstallPath',
]
