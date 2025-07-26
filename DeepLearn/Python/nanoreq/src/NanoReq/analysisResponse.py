
from client import data
def Analysis_Response(response: bytes) -> tuple:
    segment = response.find(b'\r\n\r\n')
    response_headers = response[:segment]
    response_body = response[(segment + 4):]
    response_headers_lines = response_headers.split(b'\r\n')
    lines_dict = {}
    for line in response_headers_lines:
        if b'HTTP' in line:
            lines_dict[b'Status-Line'] = line
        else:
            key, value = line.split(b':', 1)
            lines_dict[key] = value
    response_headers_lines_dict = {}
    for key, value in lines_dict.items():
        response_headers_lines_dict[key.decode('ascii')] = value.decode(encoding='ascii', errors='replace')
    return response_headers_lines_dict, response_body

aa, bb = Analysis_Response(data)
