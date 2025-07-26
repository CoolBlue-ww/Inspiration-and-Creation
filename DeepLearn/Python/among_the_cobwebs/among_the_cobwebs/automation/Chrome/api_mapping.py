from selenium.webdriver.chrome.options import Options as BaseOptions
from selenium.webdriver.chrome.service import Service as BaseService
from typing import IO, Sequence, Mapping, Any


class Options(BaseOptions):
    __slots__ = ()

    def __init__(self) -> None:
        super().__init__()

    def add_arg(self, arg: str) -> None:
        return super().add_argument(arg)

    def add_exp_arg(self, name: str, value: str | list | dict | list[str]) -> None:
        return super().add_experimental_option(name=name, value=value)


class Service(BaseService):
    __slots__ = ()

    def __init__(self,
                 executable_path: str | None = None,
                 log_output: int | str | IO | None = None,
                 service_args: Sequence[str] | None = None,
                 env: Mapping[str, str] | None = None,
                 port: int = 0,
                 **kwargs: Any,
                 ) -> None:
        super().__init__(
            executable_path=executable_path,
            log_output=log_output,
            env=env,
            port=port,
            service_args=service_args,
            **kwargs
        )


__all__ = [
    'Options',
    'Service'
]
