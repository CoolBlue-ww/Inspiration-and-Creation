import ijson
import zipfile
from pathlib import Path
import requests
import io
from tqdm.auto import tqdm


class ParseJson(object):
    def __init__(self,
                 platform: str,
                 version: str,
                 ) -> None:
        self._platform = platform
        self._version = version
        self._parent_dir = Path(__file__).parent
        self._cache_json_path = self._parent_dir.joinpath(
            'chromedriver_info.json',
        )

    def parse_json(self) -> str:
        install_links = {}
        possible_versions = []
        finally_possible_versions = []
        with open(self._cache_json_path, 'r', encoding='utf-8') as f:
            for meta_info in ijson.items(f, 'versions.item'):
                if meta_info['version'] == self._version:
                    install_links = meta_info['downloads']['chromedriver']
                    break
                if self._version.rsplit(sep='.', maxsplit=1)[0] in meta_info['version']:
                    possible_versions.append(meta_info['version'])
                if self._version.split(sep='.', maxsplit=1)[0] in meta_info['version']:
                    finally_possible_versions.append(meta_info['version'])
        url = ''
        for install_link in install_links:
            if install_link['platform'] == self._platform:
                url = install_link['url']
        if not url and possible_versions:
            print(possible_versions)
            close_version = max(possible_versions, key=lambda v: int(v.split('.')[-1]))
            with open(self._cache_json_path, 'r', encoding='utf-8') as f:
                for meta_info in ijson.items(f, 'versions.item'):
                    if meta_info['version'] == close_version:
                        install_links = meta_info['downloads']['chromedriver']
                        break
            for install_link in install_links:
                if install_link['platform'] == self._platform:
                    url = install_link['url']
            return url
        if not url and not possible_versions and finally_possible_versions:
            close_version = max(finally_possible_versions, key=lambda v: tuple(map(int, v.split('.')[-2::])))
            with open(self._cache_json_path, 'r', encoding='utf-8') as f:
                for meta_info in ijson.items(f, 'versions.item'):
                    if meta_info['version'] == close_version:
                        install_links = meta_info['downloads']['chromedriver']
                        break
            for install_link in install_links:
                if install_link['platform'] == self._platform:
                    url = install_link['url']
            return url
        return url

    def install(self) -> str | None:
        url = self.parse_json()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        root_dir = Path(__file__).parent.parent.parent
        install_path = root_dir.joinpath(
            'chrome',
            self._version,
            self._platform,
        )
        # 检查路径是否存在，不存在则创建。保证内存中的二字节原始数据顺利存入文件。
        if not install_path.exists():
            install_path.mkdir(parents=True, exist_ok=True)
        # 如果存在直接直接返回路径，避免重复下载
        else:
            binary_path = str(install_path.joinpath(
                f'chromedriver-{self._platform}',
                'chromedriver.exe',
            ))
            return binary_path

        # 创建Session会话对象
        session = requests.Session()

        # 1. 先发 HEAD 请求拿文件大小（有的服务器没 Content-Length，需容错）
        resp_head = session.head(url, allow_redirects=True)
        total_size = int(resp_head.headers.get('content-length', 0))

        # 2. 正式 GET 下载，用 stream=True 边下边写 BytesIO
        resp = session.get(url=url,
                           headers=headers,
                           stream=True,
                           timeout=10,)
        resp.raise_for_status()

        # 3. BytesIO 充当内存文件
        mem_file = io.BytesIO()

        # 4. tqdm 包装迭代器，实时刷新
        with tqdm(total=total_size, unit='B', unit_scale=True,
                  desc='Downloading') as bar:
            for chunk in resp.iter_content(chunk_size=1024 * 64):  # 64 KB 一块
                if chunk:
                    mem_file.write(chunk)
                    bar.update(len(chunk))

        # 5. 下载完成，把指针拉回开头
        mem_file.seek(0)

        # 6. 直接在内存解压,并且同时保存压缩包原文件
        with (
            zipfile.ZipFile(mem_file) as zf,
            open(install_path.joinpath(
                f'chromedriver-{self._platform}.zip',
            ), 'wb') as f,
        ):
            print(f"Get: {url} Download completed...")
            zf.extractall(install_path)
            f.write(mem_file.getvalue())

        # 获取下载完成解压之后，文件夹内部的binary文件路径
        for obj in install_path.iterdir():
            if obj.is_dir():
                binary_path = str(obj.joinpath(
                    'chromedriver.exe',
                )
            )
                return binary_path
        return None

__all__ = [
    'ParseJson',
]
