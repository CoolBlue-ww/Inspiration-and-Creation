from pathlib import Path
import os

# 指定浏览器配置相关文件的路径

class Paths(object):
    def __init__(self) ->None:
        self.current_file_path = Path(__file__)
        self.parent_directory = self.current_file_path.parent


    @property
    def chrome(self) ->str:
        return os.path.join(
            self.parent_directory,
            'chrome-installation',
            'opt',
            'google',
            'chrome',
            'google-chrome'
        )

    @property
    def chrome_cache(self) ->str:
        return os.path.join(self.parent_directory, 'chrome-cache')

    @property
    def chrome_data(self) ->str:
        return os.path.join(self.parent_directory, 'chrome-data')

    @property
    def chrome_installation(self) ->str:
        return os.path.join(self.parent_directory, 'chrome=installation')

    @property
    def chrome_deb(self) ->str:
        return os.path.join(self.parent_directory, 'chrome.deb')

    @property
    def chromedriver(self) ->str:
        return os.path.join(self.parent_directory, 'chromedriver')

    @property
    def chrome_launcher(self) ->str:
        return os.path.join(self.parent_directory, 'chrome_launcher.py')

    @property
    def run_chrome_sh(self) ->str:
        return os.path.join(self.parent_directory, 'run-chrome.sh')

    @property
    def chrome_update(self) ->str:
        return os.path.join(self.parent_directory, 'update.py')



PATHS = Paths()
CHROME = PATHS.chrome
CHROME_CACHE = PATHS.chrome_cache
CHROME_DATA = PATHS.chrome_data
CHROME_INSTALLATION = PATHS.chrome_installation
CHROME_DEB = PATHS.chrome_deb
CHROMEDRIVER = PATHS.chromedriver
CHROME_LAUNDER = PATHS.chrome_launcher
RUN_CHROME_SH = PATHS.run_chrome_sh
CHROME_UPDATE = PATHS.chrome_update


__all__ = ['CHROME', 'CHROME_CACHE', 'CHROME_DEB',
           'CHROME_DATA', 'CHROME_LAUNDER', 'CHROME_UPDATE',
           'CHROME_INSTALLATION', 'CHROMEDRIVER', 'RUN_CHROME_SH']
