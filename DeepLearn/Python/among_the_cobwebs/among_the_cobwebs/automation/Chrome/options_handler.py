from among_the_cobwebs.automation.Chrome.api_mapping import Options
from pathlib import Path
from typing import Any, Sequence, Union


class ParameterMapping(object):
    __slots__ = [
        '_options_mapping'
    ]

    def __init__(self) -> None:
        #  映射Options对象的参数值
        self._options_mapping = {
            'headless': '--headless',  # 无头浏览器模式  add_argument() 0
            'disable_sandbox': '--no-sandbox',  # 禁用沙盒模式 0
            'disable_gpu': '--disable-gpu',  # 禁用gpu加速 0
            'window_size': '--window-size=__,__',  # 自定义分辨率 0
            'max_window': 'start-maximized',  # 启动时最大化窗口 0
            'user_agent': '--user-agent=__',  # 用户代理，可以通过指定ua来模拟移动端，从而调节其分辨率 0
            'disable_alert_bar': '--disable-infobars',  # 禁用自动化提示栏 0
            'traceless': '--incognito',  # 无痕隐身模式 0
            'disable_features': '--disable-blink-features=AutomationControlled',  # 禁用自动化控制特征 0
            'disable_images': 'blink-settings=imagesEnabled=false',  # 禁止图片和视频加载 0
            'disable_javascript': '--disable-javascript',  # 禁用javascript 0
            'proxy': '--proxy-server=__',  # 通过代理服务器访问网站 0
            'disable_shm': '--disable-dev-shm-usage',  # 禁用共享内存 0
            'disable_expansions': '--disable-expansions',  # 禁用扩展 0
            'disable_notifications': '--disable-notifications',  # 禁用通知 0
            'ignore_certificate_errors': '--ignore-certificate-errors',  # 忽略证书错误 0
            'user_data_dir': '--user-data-dir=__',  # 指定用户数据目录 0
            'lang': '--lang=__',  # 语言设置 0
            'disable_webrtc': '--disable-webrtc',  # 禁用WebRTC 0
            'disable_web_security': '--disable-web-security',  # 禁用同源策略 0
            'allow_running_insecure_content': '--allow-running-insecure-content', # 允许不安全内容 0
        }

    @property
    def options_mapping(self):
        return self._options_mapping


class OptionsHandler(ParameterMapping):
    __slots__ = [
        '_args',
        '_exp_args',
        '_arguments',
        '_options',
    ]

    def __init__(self,
                 args: Union[Sequence[str], set[str]] | dict[str, Any] | None = None,
                 exp_args: dict[str, str | int | dict | list[str]] | None = None,
                 ) -> None:
        super().__init__()
        self._args = args
        self._exp_args = exp_args
        self._arguments = {
            'arguments': [],
            'experimental_arguments': {},
        }
        self._options = Options()
        if self._args and isinstance(self._args, dict):
            if 'headless' in self._args and self._args['headless']  == True:
                self._options.add_arg(
                    self.options_mapping['headless'],
                )
                self._arguments['arguments'].append(self.options_mapping['headless'])

            if 'disable_sandbox' in self._args and self._args['disable_sandbox'] == True:
                self._options.add_arg(
                    self.options_mapping['disable_sandbox'],
                )
                self._arguments['arguments'].append(self.options_mapping['disable_sandbox'])

            if 'disable_gpu' in self._args and self._args['disable_gpu'] == True:
                self._options.add_arg(
                    self.options_mapping['disable_gpu'],
                )
                self._arguments['arguments'].append(self.options_mapping['disable_gpu'])

            if 'window_size' in self._args and isinstance(self._args['window_size'], tuple):
                if len(self._args['window_size']) == 2 and all(isinstance(side_length, int | float) for side_length in self._args['window_size']):
                    width, height = self._args['window_size']
                    self._options.add_arg(
                        self.options_mapping['window_size'].replace(
                            '__,__',
                            str(width) + ',' + str(height),
                            1
                        )
                    )
                    self._arguments['arguments'].append(
                        self.options_mapping['window_size'].replace(
                            '__,__',
                            str(width) + ',' + str(height),
                            1
                        )
                    )

            if 'max_window' in self._args and self._args['max_window'] == True:
                self._options.add_arg(
                    self.options_mapping['max_window'],
                )
                self._arguments['arguments'].append(self.options_mapping['max_window'])

            if 'disable_alert_bar' in self._args and self._args['disable_alert_bar'] == True:
                self._options.add_arg(
                    self.options_mapping['disable_alert_bar'],
                )
                self._arguments['arguments'].append(self.options_mapping['disable_alert_bar'])

            if 'disable_features' in self._args and self._args['disable_features']  == True:
                self._options.add_arg(
                    self.options_mapping['disable_features'],
                )
                self._arguments['arguments'].append(self.options_mapping['disable_features'])

            if 'disable_javascript' in self._args and self._args['disable_javascript'] == True:
                self._options.add_arg(
                    self.options_mapping['disable_javascript'],
                )
                self._arguments['arguments'].append(self.options_mapping['disable_javascript'])

            if 'disable_images' in self._args and self._args['disable_images'] == True:
                self._options.add_arg(
                    self.options_mapping['disable_images'],
                )
                self._arguments['arguments'].append(self.options_mapping['disable_images'])

            if 'user_agent' in self._args and isinstance(self._args['user_agent'], str):
                self._options.add_arg(
                    self.options_mapping['user_agent'].replace(
                        '__',
                        str(self._args['user_agent']),
                        1,
                    ),
                )
                self._arguments['arguments'].append(
                    self.options_mapping['user_agent'].replace(
                        '__',
                        str(self._args['user_agent']),
                        1,
                    ),
                )

            if 'traceless' in self._args and self._args['traceless'] == True:
                self._options.add_arg(
                    self.options_mapping['traceless'],
                )
                self._arguments['arguments'].append(self.options_mapping['traceless'])

            if 'proxy' in self._args and isinstance(self._args['proxy'], str):
                self._options.add_arg(
                    self.options_mapping['proxy'].replace(
                        '__',
                        str(self._args['proxy']),
                        1,
                    )
                )
                self._arguments['arguments'].append(
                    self.options_mapping['proxy'].replace(
                        '__',
                        str(self._args['proxy']),
                        1,
                    )
                )

            if 'disable_shm' in self._args and self._args['disable_shm'] == True:
                self._options.add_arg(
                    self.options_mapping['disable_shm'],
                )
                self._arguments['arguments'].append(self.options_mapping['disable_shm'])

            if 'disable_expansions' in self._args and self._args['disable_expansions'] == True:
                self._options.add_arg(
                    self.options_mapping['disable_expansions']
                )
                self._arguments['arguments'].append(self.options_mapping['disable_expansions'])

            if 'disable_notifications' in self._args and self._args['disable_notifications'] == True:
                self._options.add_arg(
                    self.options_mapping['disable_notifications'],
                )
                self._arguments['arguments'].append(self.options_mapping['disable_notifications'])

            if 'ignore_certificate_errors' in self._args and self._args['ignore_certificate_errors'] == True:
                self._options.add_arg(
                    self.options_mapping['ignore_certificate_errors'],
                )
                self._arguments['arguments'].append(self.options_mapping['ignore_certificate_errors'])

            if 'user_data_dir' in self._args and isinstance(self._args['user_data_dir'], str):
                path = Path(self._args['user_data_dir'])
                if path.exists() and path.is_dir():
                    self._options.add_arg(
                        self.options_mapping['user_data_dir'].replace(
                            '__',
                            str(path),
                            1,
                        )
                    )
                    self._arguments['arguments'].append(
                        self.options_mapping['user_data_dir'].replace(
                            '__',
                            str(path),
                            1,
                        )
                    )

            if 'language' in self._args and isinstance(self._args['language'], str):
                self._options.add_arg(
                    self.options_mapping['lang'].replace(
                        '__',
                        self._args['language'],
                        1,
                    )
                )
                self._arguments['arguments'].append(
                    self.options_mapping['lang'].replace(
                        '__',
                        self._args['language'],
                        1,
                    )
                )

            if 'disable_webrtc' in self._args and self._args['disable_webrtc'] == True:
                self._options.add_arg(
                    self.options_mapping['disable_webrtc'],
                )
                self._arguments['arguments'].append(self.options_mapping['disable_webrtc'])

            if 'disable_web_security' in self._args and self._args['disable_web_security'] == True:
                self._options.add_arg(
                    self.options_mapping['disable_web_security'],
                )
                self._arguments['arguments'].append(self.options_mapping['disable_web_security'])

            if 'allow_running_insecure_content' in self._args and self._args['allow_running_insecure_content'] == True:
                self._options.add_arg(
                    self.options_mapping['allow_running_insecure_content'],
                )
                self._arguments['arguments'].append(self.options_mapping['allow_running_insecure_content'])


        if self._args and isinstance(self._args, Union[Sequence, set]):
            if isinstance(self._args, str):
                if ' ' in self._args:
                    args = self._args.split(' ')
                    for arg in args:
                        self._options.add_arg(
                            arg,
                        )
                        self._arguments['arguments'].append(arg)
                else:
                    self._options.add_arg(
                        self._args,
                    )
                    self._arguments['arguments'].append(self._args)
            else:
                for arg in self._args:
                    self._options.add_arg(
                        arg,
                    )
                    self._arguments['arguments'].append(arg)


        if self._exp_args and isinstance(self._exp_args, dict):
            for name, value in self._exp_args.items():
                self._options.add_exp_arg(
                    name=name,
                    value=value,
                )
            self._arguments['experimental_arguments'] = self._exp_args


    @property
    def options(self) -> Options:
        return self._options

    @property
    def get_arguments(self) -> dict:
        return self._arguments


__all__ = [
    'OptionsHandler',
]

