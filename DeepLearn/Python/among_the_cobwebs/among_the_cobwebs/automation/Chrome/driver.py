from selenium import webdriver
from selenium.webdriver.common.bidi.browser import Browser
from selenium.webdriver.common.bidi.browsing_context import BrowsingContext
from selenium.webdriver.common.bidi.network import Network
from selenium.webdriver.common.by import By
from selenium.webdriver.common.bidi.permissions import Permissions
from selenium.webdriver.common.print_page_options import PrintOptions
from selenium.webdriver.common.timeouts import Timeouts
from selenium.webdriver.common.bidi.webextension import WebExtension
from selenium.webdriver.common.bidi.storage import Storage
from selenium.webdriver.common.bidi.script import Script
from selenium.webdriver.common.fedcm.dialog import Dialog
from selenium.webdriver.common.virtual_authenticator import VirtualAuthenticatorOptions, Credential
from selenium.webdriver.remote.errorhandler import ErrorHandler
from selenium.webdriver.remote.file_detector import FileDetector
from selenium.webdriver.remote.remote_connection import RemoteConnection
from selenium.webdriver.remote.script_key import ScriptKey
from selenium.webdriver.remote.switch_to import SwitchTo
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.websocket_connection import WebSocketConnection
from selenium.webdriver.remote.bidi_connection import BidiConnection
from selenium.webdriver.remote.fedcm import FedCM
from selenium.webdriver.remote.mobile import Mobile
from selenium.webdriver.remote.locator_converter import LocatorConverter
# =============================================================================
from typing import AsyncGenerator, Any, Generator, IO, Sequence, Mapping, Union
from among_the_cobwebs.automation.Chrome.options_handler import OptionsHandler
from among_the_cobwebs.automation.Chrome.service_handler import ServiceHandler


class Driver(object):
    __slots__ = [
        '_driver',
        '_service_handler',
        '_service',
        '_options_handler',
        '_options',
        '_executable_path',
        '_enabled_log',
        '_log_output',
        '_port',
        '_env',
        '_service_args',
        '_args',
        '_exp_args',
    ]

    def __init__(self,
                 executable_path: str | None = None,
                 *,
                 enabled_log: bool = False,
                 log_output: int | str | IO | None = None,
                 port: int = 0,
                 env: Mapping[str, str] | None = None,
                 service_args: Sequence[str] | None = None,
                 args: Union[Sequence[str], set[str]] | dict[str, Any] | None = None,
                 exp_args: dict[str, str | int | dict | list[str]] | None = None,
                 **kwargs: Any,
                 ) -> None:
        self._executable_path = executable_path
        self._enabled_log = enabled_log
        self._log_output = log_output
        self._port = port
        self._env = env
        self._service_args = service_args
        self._service_handler = ServiceHandler(
            executable_path=self._executable_path,
            enabled_log=self._enabled_log,
            log_output=self._log_output,
            port=self._port,
            env=self._env,
            service_args=self._service_args,
            **kwargs
        )
        self._args = args
        self._exp_args = exp_args
        self._options_handler = OptionsHandler(
            args=self._args,
            exp_args=self._exp_args,
        )
        self._driver = webdriver.Chrome(
            service=self._service_handler.service,
            options=self._options_handler.options,
        )

    @property
    def get_arguments(self):
        return self._options_handler.get_arguments

    # Driver实例的基础浏览器名称
    @property
    def name(self) -> str:
        return self._driver.name

    # Driver实例的会话id
    @property
    def session_id(self) -> str | None:
        return self._driver.session_id

    # Driver会话中有效功能的字典
    @property
    def capabilities(self) -> dict:
        return self._driver.capabilities

    # 命令执行器的通信接口
    @property
    def command_executor(self) -> str | RemoteConnection:
        return self._driver.command_executor

    # 错误处理器对象
    @property
    def error_handler(self) -> ErrorHandler:
        return self._driver.error_handler

    # 自定义开启Driver实例
    def start_client(self) -> None:
        return self._driver.start_client()

    # 自定义关闭Driver实例
    def stop_client(self) -> None:
        self._driver.stop_client()

    # 自定义创建新的session会话对象
    def start_session(self,
                      capabilities: dict
                      ) -> None:
        return self._driver.start_session(capabilities=capabilities)

    # 创建具有指定element_id的元素
    def create_web_element(self,
                           element_id: str
                           ) -> WebElement:
        return self._driver.create_web_element(element_id=element_id)

    # 执行Chrome浏览器CDP命令
    def execute_cdp_cmd(self,
                        cmd: str,
                        cmd_args: dict
                        ) -> Any:
        return self._driver.execute_cdp_cmd(cmd=cmd, cmd_args=cmd_args)

    # 执行底层Exec命令
    def execute(self,
                driver_command: str,
                params: dict[str, Any] | None = None
                ) -> dict[str, Any]:
        return self._driver.execute(driver_command=driver_command, params=params)

    # 储存常用的javascript脚本
    def pin_script(self,
                   script: str,
                   script_key: Any = None
                   ) -> ScriptKey:
        return self._driver.pin_script(script=script, script_key=script_key)

    # 从储存中删除javascript脚本
    def unpin(self,
              script_key: ScriptKey
              ) -> None:
        return self._driver.unpin(script_key=script_key)

    # 返回一个列表，包含所有添加的固定脚本
    def get_pinned_scripts(self) -> list[str]:
        return self._driver.get_pinned_scripts()

    # 同步执行当前窗口或者框架中的JavaScript
    def execute_script(self,
                       script: str, *args: Any
                       ) -> Any | None:
        return self._driver.execute_script(script=script, *args)

    # 异步执行当前窗口或者框架的JavaScript
    def execute_async_script(self,
                             script: str, *args: Any
                             ) -> Any | None:
        return self._driver.execute_async_script(script=script, *args)

    # 前往目标url地址
    def get(self,
            url: str
            ) -> None:
        return self._driver.get(url)

    # 获取当前页面的标题
    @property
    def title(self) -> str:
        return self._driver.title

    # 获取当前页面的连接地址
    @property
    def current_url(self) -> str:
        return self._driver.current_url

    # 获取当前页面的网页源码
    @property
    def page_source(self) -> str:
        return self._driver.page_source

    # 获取当前页面的窗口句柄
    @property
    def current_window_handle(self) -> str:
        return self._driver.current_window_handle

    # 获取所有的窗口句柄
    @property
    def window_handles(self) -> list[str]:
        return self._driver.window_handles

    # 最大化Driver实例的窗口大小
    def maximize_window(self) -> None:
        return self._driver.maximize_window()

    # 对当前页面打开全屏模式
    def fullscreen_window(self) -> None:
        return self._driver.fullscreen_window()

    # 最小化Driver实例的窗口大小
    def minimize_window(self) -> None:
        return self._driver.minimize_window()

    # 打印页面
    def print_page(self,
                   print_options: PrintOptions | None = None
                   ) -> str:
        return self._driver.print_page(print_options=print_options)

    # 切换上下文（聚焦）
    @property
    def switch_to(self) -> SwitchTo:
        return self._driver.switch_to

    # 前进
    def forward(self) -> None:
        return self._driver.forward()

    # 回退
    def back(self) -> None:
        return self._driver.back()

    # 刷新页面
    def refresh(self):
        return self._driver.refresh()

    # 获取所有的cookie
    def get_cookies(self) -> list[dict]:
        return self._driver.get_cookies()

    # 通过cookie的名称还获取对应的cookie值
    def get_cookie(self,
                   name: str
                   ) -> dict | None:
        return self._driver.get_cookie(name=name)

    # 通过cookie的名称，删除cookie
    def delete_cookie(self,
                      name: str
                      ) -> None:
        return self._driver.delete_cookie(name=name)

    # 删除所有cookie
    def delete_all_cookies(self) -> None:
        return self._driver.delete_all_cookies()

    # 通过加入字典的方式向会话对象注入cookie
    def add_cookie(self,
                   cookie_dict: dict
                   ) -> None:
        return self._driver.add_cookie(cookie_dict=cookie_dict)

    # 隐式等待页面特定元素加载（全局属性）
    def implicitly_wait(self,
                        time_to_wait: float
                        ) -> None:
        return self._driver.implicitly_wait(time_to_wait=time_to_wait)

    # 设置JavaScript异步脚本的超时时间
    def set_script_timeout(self,
                           time_to_wait: float
                           ) -> None:
        return self._driver.set_script_timeout(time_to_wait=time_to_wait)

    # 等待整个页面加载完成的超时时间
    def set_page_load_timeout(self,
                              time_to_wait: float
                              ) -> None:
        return self._driver.set_page_load_timeout(time_to_wait=time_to_wait)

    # 获取当前会话中的所有超时设置
    @property
    def timeouts(self) -> Timeouts:
        return self._driver.timeouts

    # 通过By提供的方式来查找网页中的一个元素
    def find_element(self,
                     by: str = By.ID,
                     value: str | None = None
                     ) -> WebElement:
        return self._driver.find_element(by=by, value=value)

    # 通过By提供的方法来查找网页中的多个元素
    def find_elements(self,
                      by: str = By.ID,
                      value: str | None = None
                      ) -> list[WebElement]:
        return self._driver.find_elements(by=by, value=value)

    # 将当前窗口的屏幕截图保存到PNG文件中
    def get_screenshot_as_file(self,
                               filename: str | Any
                               ) -> bool:
        return self._driver.get_screenshot_as_file(filename=filename)

    # 将当前窗口屏幕截图保存到PNG文件中
    def save_screenshot(self,
                        filename: str | Any
                        ) -> bool:
        return self._driver.save_screenshot(filename=filename)

    # 以二进制的形式保存当前屏幕截图
    def get_screenshot_as_png(self) -> bytes:
        return self._driver.get_screenshot_as_png()

    # 以base64编码的字符串保存当前的屏幕截图
    def get_screenshot_as_base64(self) -> str:
        return self._driver.get_screenshot_as_base64()

    # 修改当前窗口的大小
    def set_window_size(self,
                        width: int | Any,
                        height: int | Any,
                        windowHandle: str = 'current'
                        ) -> None:
        return self._driver.set_window_size(width=width, height=height, windowHandle=windowHandle)

    # 获取当前窗口的大小
    def get_window_size(self,
                        windowHandle: str = 'current'
                        ) -> dict:
        return self._driver.get_window_size(windowHandle=windowHandle)

    # 设置当前窗口的位置
    def set_window_position(self,
                            x: float,
                            y: float,
                            windowHandle: str = 'current'
                            ) -> dict:
        return self._driver.set_window_position(x=x, y=y, windowHandle=windowHandle)

    # 获取当前窗口的位置
    def get_window_position(self,
                            windowHandle: str = 'current'
                            ) -> dict:
        return self._driver.get_window_position(windowHandle=windowHandle)

    # 获取当前窗口的位置和大小
    def get_window_rect(self) -> dict:
        return self._driver.get_window_rect()

    # 设置当前窗口的位置和大小（兼容的浏览器）
    def set_window_rect(self,
                        x: Any = None,
                        y: Any = None,
                        width: Any = None,
                        height: Any = None
                        ) -> dict:
        return self._driver.set_window_rect(x=x, y=y, width=width, height=height)

    # 文件的路径检查（主要用于远程服务）
    @property
    def file_detector(self) -> FileDetector:
        return self._driver.file_detector

    # 控制和获取移动端的屏幕方向
    @property
    def orientation(self) -> Any:
        return self._driver.orientation

    # 目前不知道用途
    @property
    def script(self) -> Script:
        return self._driver.script

    # 打开开发者工具
    def start_devtools(self) -> tuple[None, WebSocketConnection] | tuple[Any, WebSocketConnection] | tuple[Any, Any]:
        return self._driver.start_devtools()

    # 双向通信
    async def bidi_connection(self) -> AsyncGenerator[BidiConnection, Any]:
        return await self._driver.bidi_connection()  # 异步，装饰器

    # 目前不确定用途
    @property
    def network(self) -> Network:
        return self._driver.network

    # 返回双向浏览器命令的浏览器模块对象
    @property
    def browser(self) -> Browser:
        return self._driver.browser

    # 返回双向浏览上下文命令的浏览上下文模块对象
    @property
    def browsing_context(self) -> BrowsingContext:
        return self._driver.browsing_context

    # 返回双向储存命令的储存模块对象
    @property
    def storage(self) -> Storage:
        return self._driver.storage

    # 返回双向webxtension命令的webxtension模块对象
    @property
    def webextension(self) -> WebExtension:
        return self._driver.webextension

    # 添加具有给定选项的模拟验证器
    def add_virtual_authenticator(self,
                                  options: VirtualAuthenticatorOptions
                                  ) -> None:
        return self._driver.add_virtual_authenticator(options=options)

    # 返回虚拟验证器的ID
    @property
    def virtual_authenticator_id(self) -> str | None:
        return self._driver.virtual_authenticator_id

    # 删除之前添加的虚拟验证器
    def remove_virtual_authenticator(self) -> None:
        return self._driver.remove_virtual_authenticator()  # 装饰器

    # 将凭证注入验证器
    def add_credential(self,
                       credential: Credential
                       ) -> None:
        return self._driver.add_credential(credential=credential)  # 装饰器

    # 获取验证器拥有的凭证列表
    def get_credentials(self) -> list[Credential]:
        return self._driver.get_credentials()  # 装饰器

    # 从验证器中删除凭证
    def remove_credential(self,
                          credential_id: str | bytearray
                          ) -> None:
        return self._driver.remove_credential(credential_id=credential_id)  # 装饰器

    # 从身份验证器中删除所有凭证
    def remove_all_credentials(self) -> None:
        return self._driver.remove_all_credentials()  # 装饰器

    # 设置身份验证器是模拟用户成功还是失败
    def set_user_verified(self,
                          verified: bool
                          ) -> None:
        return self._driver.set_user_verified(verified=verified)  # 装饰器

    # 以文件名列表的形式检索可下载文件
    def get_downloadable_file(self,
                              *args,
                              **kwargs
                              ) -> list:
        return self._driver.get_downloadable_files(*args, **kwargs)

    # 将具有指定文件名的文件下载到指定目录
    def download_file(self,
                      file_name: str,
                      target_directory: str,
                      *args: Any,
                      **kwargs: Any
                      ) -> None:
        return self._driver.download_file(file_name=file_name, target_directory=target_directory, *args, *kwargs)

    # 删除所有可下载文件
    def delete_downloadable_files(self) -> None:
        return self._driver.delete_downloadable_files()

    # 是否支持FedCM功能
    @property
    def supports_fedcm(self) -> bool:
        return self._driver.supports_fedcm

    # 返回FedCM对话框对象进行交互
    @property
    def fedcm(self) -> FedCM:
        return self._driver.fedcm

    # 返回用于交互的FedCm对话框对象
    @property
    def dialog(self) -> Dialog:
        return self._driver.dialog

    # 等待并返回FedCM对话框
    def fedcm_dialog(self,
                     timeout: int = 5,
                     poll_frequency: float = 0.5,
                     ignored_exceptions: Any = None
                     ) -> Dialog:
        return self._driver.fedcm_dialog(timeout=timeout, poll_frequency=poll_frequency,
                                         ignored_exceptions=ignored_exceptions)

    # 关闭当前窗口
    def close(self) -> None:
        return self._driver.close()

    # 关闭Driver实例
    def quit(self) -> None:
        return self._driver.quit()

    # ==========================================================

    @property
    def caps(self) -> dict[str, Any]:
        return self._driver.caps

    def delete_network_conditions(self) -> None:
        return self._driver.delete_network_conditions()

    def file_detector_context(self,
                              file_detector: object | Any,
                              *args: tuple | Any,
                              **kwargs: dict | Any
                              ) -> Generator[
        Any, Any, None]:
        return self._driver.file_detector_context(file_detector=file_detector, *args, **kwargs)  # 装饰器

    def get_downloadable_files(self,
                               *args: Any,
                               **kwargs: Any
                               ) -> list:
        return self._driver.get_downloadable_files(*args, **kwargs)

    def get_issue_message(self) -> Any:
        return self._driver.get_issue_message()

    def get_log(self,
                log_type: str | Any
                ) -> Any:
        return self._driver.get_log(log_type=log_type)

    def get_network_conditions(self) -> dict | Any:
        return self._driver.get_network_conditions()

    def get_sinks(self) -> list:
        return self._driver.get_sinks()

    def launch_app(self,
                   id: Any
                   ) -> dict[str, Any]:
        return self._driver.launch_app(id=id)

    @property
    def locator_converter(self) -> LocatorConverter | None:
        return self._driver.locator_converter

    @property
    def log_types(self) -> list | Any:
        return self._driver.log_types

    @property
    def mobile(self) -> Mobile:
        return self._driver.mobile

    @property
    def permissions(self) -> Permissions:
        return self._driver.permissions

    def pinned_scripts(self) -> dict[str, Any]:
        return self._driver.pinned_scripts

    def set_network_conditions(self,
                               **network_conditions: dict | Any
                               ) -> None:
        return self._driver.set_network_conditions(**network_conditions)

    def set_permissions(self,
                        name: str,
                        value: str
                        ) -> None:
        return self._driver.set_permissions(name=name, value=value)

    def set_sink_to_use(self,
                        sink_name: str
                        ) -> dict:
        return self._driver.set_sink_to_use(sink_name=sink_name)

    def start_desktop_mirroring(self,
                                sink_name: str
                                ) -> dict:
        return self._driver.start_desktop_mirroring(sink_name=sink_name)

    def start_tab_mirroring(self,
                            sink_name: str
                            ) -> dict:
        return self._driver.start_tab_mirroring(sink_name=sink_name)

    def stop_casting(self,
                     sink_name: str
                     ) -> dict:
        return self._driver.stop_casting(sink_name=sink_name)


__all__ = [
    'Driver'
]
