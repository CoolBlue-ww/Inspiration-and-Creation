from among_the_cobwebs.automation.Chrome.api_mapping import Service
from typing import IO, Sequence, Any
from pathlib import Path
import sys


class DefaultOutput(object):
    __slots__ = [
        '_main_file',
        '_main_parent_dir',
        '_current_dir',
    ]

    def __init__(self) -> None:
        if hasattr(sys.modules['__main__'], '__file__'):
            self._main_file = sys.modules['__main__'].__file__
            self._main_parent_dir = str(Path(self._main_file).parent.resolve())
        else:
            self._current_dir = str(Path.cwd())

    @property
    def default_output(self) -> str:
        if self._main_parent_dir:
            return self._main_parent_dir
        else:
            return self._current_dir


class LogConfig(DefaultOutput):
    __slots__ = ['_enabled', '_dir', '_default_dir']

    def __init__(self) -> None:
        super().__init__()
        self._dir: str = super().default_output
        self._enabled: bool = False

    @property
    def enabled(self) -> bool:
        return self._enabled

    @property
    def dir(self) -> str | None:
        return self._dir

    @enabled.setter
    def enabled(self, value: str) -> None:
        self._enabled = value

    @dir.setter
    def dir(self, value: str) -> None:
        if self._enabled:
            if bool(value):
                self._dir = value
            else:
                self._dir = self._dir
        else:
            self._dir = None


class ServiceHandler:
    __slots__ = [
        '_executable_path',
        '_port',
        '_env',
        '_service_args',
        '_log_config',
        '_service',
    ]

    def __init__(self,
                 executable_path: str | None = None,
                 enabled_log: bool = False,
                 log_output: int | str | IO | None = None,
                 port: int = 0,
                 env: dict[str, str] | None = None,
                 service_args: Sequence[str] = None,
                 **kwargs: Any,
                 ) -> None:
        self._executable_path = executable_path
        self._port = port
        self._env = env
        self._service_args = service_args
        self._log_config = LogConfig()
        self._log_config.enabled = enabled_log
        self._log_config.dir = log_output
        self._service = Service(
            executable_path=self._executable_path,
            log_output=self._log_config.dir,
            port=self._port,
            env=self._env,
            serivce_args=self._service_args,
            **kwargs,
        )

    @property
    def service(self) -> Service:
        return self._service


__all__ = [
    'DefaultOutput',
    'LogConfig',
    'ServiceHandler',
]
