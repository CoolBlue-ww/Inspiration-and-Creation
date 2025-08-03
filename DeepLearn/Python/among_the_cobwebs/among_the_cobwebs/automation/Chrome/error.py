from selenium.common.exceptions import WebDriverException, NoSuchDriverException, SessionNotCreatedException
from typing import Any


class ExecutableNotFoundError(NoSuchDriverException):
    def __init__(self,
                 massage: str,
                 ) -> None:
        self._massage = massage
        super().__init__(self._massage)


class VersionCompatibilityError(SessionNotCreatedException):
    def __init__(self,
                 massage: str
                 ) -> None:
        self._massage = massage
        super().__init__(self._massage)


class StartupError(WebDriverException):
    def __init__(self,
                 massage: str
                 ) -> None:
        self._massage = massage
        super().__init__(self._massage)




