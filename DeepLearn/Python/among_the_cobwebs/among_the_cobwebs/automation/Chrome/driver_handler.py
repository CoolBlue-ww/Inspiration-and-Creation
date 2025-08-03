import shutil
from tqdm import tqdm
from pathlib import Path

from requests.exceptions import RequestException

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import WebDriverException, NoSuchDriverException, SessionNotCreatedException

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


from among_the_cobwebs.automation.Chrome.service_handler import ServiceHandler
from among_the_cobwebs.automation.Chrome.options_handler import OptionsHandler

from among_the_cobwebs.automation.Chrome.error import ExecutableNotFoundError, VersionCompatibilityError, StartupError

# os.environ['SE_CACHE_DIR'] = str(self._target_rootdir)
# os.environ['WDM_LOCAL'] = '1'


class DriverHandler(object):
    def __init__(self,
                 service_handler: ServiceHandler,
                 options_handler: OptionsHandler,
                 ) -> None:
        self._service = service_handler.service
        self._options = options_handler.options
        self._chrome_driver = webdriver.Chrome(
             service=self._service,
             options=self._options,
        )

    @property
    def chrome_driver(self) -> WebDriver:
        return self._chrome_driver

