from pathlib import Path
import requests
from tqdm.auto import tqdm
import zipfile
import io

class RequestData(object):
    def __init__(self,
                 platform: str,
                 version: str,
                 ) -> None:
        self._platform = platform
        self._version = version
        self._rootdir_dir = Path(__file__).parent.parent.parent.parent
        self._install_path = self._rootdir_dir.joinpath(
            'edge',
            self._version,
            self._platform,
        )
        self._zip_path = self._install_path.joinpath(
            f'edgedriver_{self._platform}'
        )
        # 检查文件保存路径是否存在
        if not self._install_path.exists():
            self._install_path.mkdir(
                parents=True,
                exist_ok=True,
            )
        if not self._zip_path.exists():
            self._zip_path.mkdir(
                parents=True,
                exist_ok=True,
            )
        self._request_url = f'https://msedgedriver.microsoft.com/{self._version}/edgedriver_{self._platform}.zip'
        self._base_url = 'https://msedgewebdriverstorage.z22.web.core.windows.net/?form=MA13LH'

    def query(self) -> list[str]:
        pass

    def install(self) -> str | None:
        # 检查兼容的驱动是否存在
        binary_path = self._zip_path.joinpath('msedgedriver.exe')
        if binary_path.exists():
            return str(binary_path)

        # 创建会话对象
        session = requests.Session()
        # 获取响应头
        resp_head = session.get(url=self._request_url, allow_redirects=True)
        # 检擦路径是否存在
        if not resp_head.ok:
            pass
        # 1. 先发 HEAD 请求拿文件大小（有的服务器没 Content-Length，需容错）
        total_size = int(resp_head.headers.get('content-length'))

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        # 2. 正式 GET 下载，用 stream=True 边下边写 BytesIO
        resp = session.get(url=self._request_url,
                           headers=headers,
                           stream=True,
                           timeout=10, )
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
            open(self._install_path.joinpath(
                f'edgedriver_{self._platform}.zip',
            ), 'wb') as f,
        ):
            print(f"Get: {self._request_url} Download completed...")
            zf.extractall(self._zip_path)
            f.write(mem_file.getvalue())

        # 获取下载完成解压之后，文件夹内部的binary文件路径
        for obj in self._zip_path.iterdir():
            if obj.name == 'msedgedriver.exe':
                binary_path = str(obj)
                return binary_path
        return None

__all__ = [
    'RequestData',
]
