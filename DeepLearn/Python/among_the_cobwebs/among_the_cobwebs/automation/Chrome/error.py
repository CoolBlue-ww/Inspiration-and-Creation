from typing import Any


class CompatibleError(Exception):
    __slots__ = [
        '_message',
        '_status_code'
    ]

    def __init__(self,
                 message: str | None = None,
                 status_code: int | str | None = None
                 ) -> None:
        self._message = message
        self._status_code = status_code

    @property
    def message(self) -> str | None:
        return self._message

    @property
    def status_code(self) -> int | str | None:
        return self._status_code


class ExecutableFileError(Exception):
    __slots__ = [
        '_message',
        '_status_code'
    ]

    def __init__(self,
                 message: str | None = None,
                 status_code: int | str | None = -1
                 ) -> None:
        super().__init__(message)
        self._message = message
        self._status_code = status_code

    @property
    def message(self) -> str | None:
        return self._message

    @property
    def status_code(self) -> int | str | None:
        return self._status_code


__all__ = [
    'ExecutableFileError',
    'CompatibleError'
]
