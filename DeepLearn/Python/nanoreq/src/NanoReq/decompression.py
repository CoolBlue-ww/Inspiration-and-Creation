import gzip
import zlib
import brotli
import zstandard
import asyncio
from client import data
from analysisResponse import aa, bb


def connect_chunk(body: bytes) -> bytes:
    if b'\r\n0\r\n\r\n' in body:
        chunks = []
        while True:
            rn = body.find(b'\r\n')
            chunk_size = int(body[:rn], 16)
            chunk_start = rn + 2
            chunk_end = chunk_start + chunk_size
            chunk = body[chunk_start:chunk_end:1]
            if chunk_size == len(chunk):
                chunks.append(chunk)
                body = body[chunk_end + 2::1]
            else:
                pass
            if chunk_size == 0:
                break
        chunks = b''.join(chunks)
        return chunks
    else:
        print('获取的响应数据不完整！')


# def square_response



def decompress_chunks(chunks: bytes, response_headers: dict) -> bytes:
    content_encoding = response_headers.get('Content-Encoding')
    if content_encoding == 'gzip':
        return gzip.decompress(chunks)
    elif content_encoding == 'deflate':
        return zlib.decompress(chunks, -zlib.MAX_WBITS)
    elif content_encoding == 'br':
        return brotli.decompress(chunks)
    elif content_encoding == 'zstd':
        ZstdDecompressor = zstandard.ZstdDecompressor()
        return ZstdDecompressor.decompress(chunks)


cc = connect_chunk(bb)
print(cc)

