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

    def query(self) -> None:
        subprocess.run(
            [
                'powershell',
                '-NoProfile',
                '-ExecutionPolicy',
                'Bypass',
                '-File',
                self._query_ps1_path
                ,
            ],
            check=True
        )
        return None

    def update(self) -> None:
        query_result_path = self._parent_dir.joinpath(
            'InstalledApps.csv',
        )
        query_result_path.unlink(
            missing_ok=True,
        )
        self.query()
        return None

__all__ = [
    'QueryInstallPath',
]
