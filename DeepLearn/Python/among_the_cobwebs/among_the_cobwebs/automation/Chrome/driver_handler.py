import shutil
import os
import warnings
from pathlib import Path
import logging
import json
import re
import sys
import platform
import time
from typing import Any, KeysView
from among_the_cobwebs.automation.Chrome.error import ExecutableFileError
from among_the_cobwebs.automation.Chrome.error import CompatibleError
from webdriver_manager.core.manager import DriverCacheManager
from webdriver_manager.chrome import ChromeDriverManager

class OsArchitectureParser(object):
    __slots__ = [
        '_os_name',
        '_architecture',
    ]

    def __init__(self) ->None:
        self._os_name: str | None = platform.system()
        self._architecture: str | None = platform.machine()

    @property
    def get_os_architecture(self) -> str | None:
        os_architecture = (self._os_name + '_' + self._architecture).lower()
        return os_architecture


class JsonInfoParser(object):
    __slots__ = [
        '_json_path',
        '_base_rootdir',
        '_target_rootdir',
        '_encoding',
        '_re_rule',
        '_os_architecture',
    ]

    def __init__(self,
                 json_path: str | Path | None = None,
                 base_rootdir: str | Path | None = None,
                 target_rootdir: str | Path | None = None,
                 encoding: str | None = None,
                 re_rule: str | None = None,
                 ) ->None:
        self._json_path = json_path
        self._base_rootdir = base_rootdir
        self._target_rootdir = target_rootdir
        self._encoding = encoding
        self._re_rule = re_rule
        self._os_architecture = OsArchitectureParser()

    @staticmethod
    def convert_path_object(path: str | Path | None = None) -> Path | None:
        if path is None:
            return None

        if isinstance(path, Path):
            return path

        if isinstance(path, str):
            if len(path) > 0:
                return Path(path)

            if len(path) == 0:
                raise ValueError('The path cannot be empty.')
        return None

    @staticmethod
    def convert_executable_path(
            driver_name: str,
            target_rootdir: Path | None = None,
    ) -> str | None:
        target_executable_path = str(target_rootdir.joinpath(driver_name))
        return target_executable_path

    @staticmethod
    def create_driver_info(
            os_arch,
            driver_name,
            driver_version,
            compatible_version,
            target_rootdir,
    ) -> dict:
        driver_info = {
            driver_name: {
                'os_architecture': os_arch,
                'driver_version': driver_version,
                'compatible_version': compatible_version,
                'executable_path': JsonInfoParser.convert_executable_path(
                    driver_name=driver_name,
                    target_rootdir=target_rootdir,
                ),
            }
        }
        return driver_info


    @property
    def parse_json_info(self) -> tuple | None:
        path_object = self.convert_path_object(self._json_path)
        base_rootdir = self.convert_path_object(self._base_rootdir)
        target_rootdir = self.convert_path_object(self._target_rootdir)
        if path_object is None:
            return None

        if path_object:

            if path_object.exists():

                if path_object.suffix == '.json':

                    with open(file=path_object, mode='r', encoding=self._encoding) as json_file:
                        json_data = json.load(json_file)
                        key = list(json_data.keys())[0]
                        binary_path = self.convert_path_object(json_data[key]['binary_path'])
                        re_rule = re.compile(self._re_rule)
                        match_object = re_rule.match(key)
                        os_architecture = self._os_architecture.get_os_architecture

                        if match_object:
                            os_arch = match_object.group(1)
                            driver_name = match_object.group(2)
                            driver_version = match_object.group(3)
                            compatible_version = match_object.group(5)

                            if os_architecture:
                                driver_info = self.create_driver_info(
                                    os_arch=os_architecture,
                                    driver_name=driver_name,
                                    driver_version=driver_version,
                                    compatible_version=compatible_version,
                                    target_rootdir=target_rootdir,
                                )

                                return driver_name, driver_info

                            else:
                                driver_info = self.create_driver_info(
                                    os_arch=os_arch,
                                    driver_name=driver_name,
                                    driver_version=driver_version,
                                    compatible_version=compatible_version,
                                    target_rootdir=target_rootdir,
                                )
                                return driver_name, driver_info

                        else:
                            raise ValueError('The content format is incorrect.')

                else:
                    raise TypeError('Received unexpected types of files.')

        else:
            raise FileNotFoundError('Cannot find this file.')

        return None


class InstallConfig(object):
    def __init__(self) -> None:
        self._enabled_install: bool = False
        self._target_rootdir: Path | None = Path('ssdds')
        self._default_target_rootdir: Path = Path(
            Path(__file__).parent,
            'executable_files',
        )
        self._encoding: str | None = 'utf-8'
        self._re_rule: str | None = r'([a-zA-Z]+?[0-9]+?)_([a-zA-Z]+)_([0-9.]+?)_([a-zA-Z]+?)_([0-9.]+?)$'

    def load_json(self, json_path) -> dict:
        with open(file=json_path, mode='r', encoding=self._encoding) as json_file:
            json_data = json.load(json_file)
        return json_data

    def dump_json(self, json_path, json_data: dict) -> None:
        with open(file=json_path, mode='w', encoding=self._encoding) as json_file:
            json.dump(
                json_data,
                json_file,
                ensure_ascii=False,
                indent=4,
            )
        return None

    def ggsg(self,
             rootdir: Path | str | None,
             json_path: Path | None,
             ) -> Path | None:
        base_json_path = Path(
            json_path,
            'drivers.json'
        )
        driver_name, driver_info = JsonInfoParser(
            json_path=base_json_path,
            base_rootdir=rootdir,
            target_rootdir=json_path,
        ).parse_json_info
        base_json_path.unlink(missing_ok=True)
        json_path = json_path.joinpath('drivers_info.json')
        self.dump_json(
            json_path,
            driver_info,
        )
        executable_path = driver_info[driver_name]['executable_path']
        return executable_path



    def selenium_manager_install(self) -> None:
        os.environ['SE_CACHE_DIR'] = str(self._target_rootdir)
        return None

    def webdriver_manager_install(self) -> str | None:

        if self._enabled_install and not self._target_rootdir and not self._default_target_rootdir:
            Path(self._default_target_rootdir).mkdir(parents=True, exist_ok=True)

        json_path_default_target = self._default_target_rootdir.joinpath('drivers_info.json')
        json_path_target = self._target_rootdir.joinpath('drivers_info.json')

        if json_path_target.exists() or json_path_default_target.exists():
            json_data = self.load_json(json_path_target or json_path_default_target)
            if 'chromedriver' in json_data:
                executable_path = Path(json_data['chromedriver']['executable_path'])
                if executable_path.exists() and executable_path.is_file():
                    return str(executable_path)

            else:
                json_path = json_path_target if json_path_target.exists() else json_path_default_target
                parent_dir = json_path.parent
                os.environ['WDM_LOCAL'] = '1'
                base_executable_path = ChromeDriverManager().install()
                rootdir = Path(DriverCacheManager()._root_dir)
                base_json_path = rootdir.joinpath('drivers.json')
                driver_name, driver_info = JsonInfoParser(
                    json_path=base_json_path,
                    base_rootdir=rootdir,
                    target_rootdir=self._target_rootdir if self._target_rootdir.exists() else self._default_target_rootdir,
                )
                shutil.move(
                    base_executable_path,
                    parent_dir
                )
                shutil.rmtree(
                    rootdir,
                )
                json_data[driver_name] = driver_info
                executable_path = json_data[driver_name]['executable_path']
                self.dump_json(
                    json_path,
                    json_data,
                )
                return executable_path

        else:
            os.environ['WDM_LOCAL'] = '1'
            rootdir = Path(DriverCacheManager()._root_dir)
            base_executable_path = ChromeDriverManager().install()
            target_rootdir = self._target_rootdir if self._target_rootdir.exists() else self._default_target_rootdir
            parent_dir = target_rootdir.parent
            driver_name, driver_info = JsonInfoParser(
                json_path=rootdir.joinpath('drivers.json'),
                base_rootdir=rootdir,
                target_rootdir=target_rootdir,
            )
            shutil.move(
                base_executable_path,
                parent_dir,
            )
            shutil.rmtree(
                rootdir,
            )
            self.dump_json(
                json_path=parent_dir.joinpath(
                    'drivers_info.json'
                ),
                json_data={
                    driver_name: driver_info
                }
            )
            executable_path = driver_info[driver_name]['executable_path']
            return executable_path


    @property
    def enabled_install(self) -> bool:
        return self._enabled_install

    @property
    def target_rootdir(self) -> str | None:
        return self._target_rootdir

    @enabled_install.setter
    def enabled_install(self, value: bool) -> None:
        self._enabled_install = value

    @target_rootdir.setter
    def target_rootdir(self, value: str | None) -> None:
        if   self._enabled_install:
            if not Path(value).exists():
                Path(value).mkdir(parents=True, exist_ok=True)
            self._target_rootdir = Path(value)
        else:
            self._target_rootdir = None


a = InstallConfig()
a.enabled_install = True
a.webdriver_manager_install()


class DriverHandler(object):
    def __init__(self,
                 executable_path: str | None = None,
                 enabled_install: bool = False,
                 target_rootdir: str | None = None,
                 ) -> None:
        self._executable_path = executable_path
        self._install_config = InstallConfig()
        self._install_config.enabled_install = enabled_install
        self._install_config.target_rootdir = target_rootdir

