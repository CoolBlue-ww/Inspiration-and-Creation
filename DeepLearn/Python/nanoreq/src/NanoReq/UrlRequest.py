from UrlParse import *
import io
import os
from datetime import datetime


class KeyTypeError(Exception):
    def __init__(self, message="Key not is string or list or tuple."):
        self.message = message
        super().__init__(message)
        return


class InputErrorLog(object):
    __slots__ = ()

    @classmethod
    def input_error_log(cls, Error_log):
        current_dirname = os.getcwd()
        file_path = os.path.join(current_dirname, "runs", "log.txt")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "a", encoding="utf-8") as file:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%m:%S")
            file.write(current_time + " " + "||" + " " + str(Error_log) + "\n")
        return


def start(obj: dict, key: str or tuple or list or set or None) -> str or dict:
    if isinstance(key, str):
        return obj.get(key)
    if isinstance(key, tuple) or isinstance(key, list) or isinstance(key, set):
        arg_dict = {}
        for k in key:
            if k in obj.keys():
                arg_dict[k] = obj.get(k)
            else:
                InputErrorLog().input_error_log("Key not in dict")
        return arg_dict
    if key is None:
        return
    try:
        if type(key) not in [str, tuple, list] and key is not None:
            raise KeyTypeError()
    except KeyTypeError as e:
        InputErrorLog().input_error_log(e)
        print("Error Log input runs/log.text")


key = {"a", "b", "c"}
result = start({"a": 1, "b": 2, "c": 3}, key=key)
print(result)

