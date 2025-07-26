import subprocess
from os import PathLike
from typing import Mapping, Any

result_run = subprocess.run(
    args=["", "--version"],
    # executable=None,
    # shell=False,
    # cwd=None,
    # env=None,
    # stdin=None,
    # stdout=None,
    # stderr=None,
    capture_output=True,
    text=True,
    # encoding=None,
    # errors=None,
    # input=None,
    # check=False,
    # timeout=None,
    # bufsize=-1,
    # close_fds=False,
    # preexec_fn=None,
    # startupinfo=None,
    # creationflags=0,
    # restore_signals=True,
    # start_new_session=False,
    # # pass_fds=,
    # user=None,
    # group=None,
    # extra_groups=None,
    # umask=-1,
    # pipesize=-1,
    # universal_newlines=None,
    # process_group=None
)

# print(result.stdout)
# print(result.stderr)
# print(result.args)
# print(result.returncode)
# print(result.check_returncode())

result_popen = subprocess.Popen(
    args=["docker", "run", "hello-world"],
    bufsize=-1,
    executable=None,
    stdin=None,
    stdout=None,
    stderr=None,
    preexec_fn=None,
    close_fds=True,
    shell=False,
    cwd=None,
    env=None,
    universal_newlines=None,
    startupinfo=None,
    creationflags=0,
    restore_signals=True,
    start_new_session=False,
    # pass_fds= (),
    # *,
    text=None,
    encoding=None,
    errors=None,
    user=None,
    group=None,
    extra_groups=None,
    umask=-1,
    pipesize=-1,
    process_group=None
)
result_popen.stdout.close()

