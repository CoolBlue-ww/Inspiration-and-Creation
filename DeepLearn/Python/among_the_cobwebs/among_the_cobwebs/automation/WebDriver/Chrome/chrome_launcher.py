#!/home/SayMyName/anaconda3/envs/Hello-World/bin/python3.12
import subprocess
import os
import sys

# 启动浏览器实例

def main():
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        print(f"脚本目录： {script_dir}")

        chrome_path = os.path.join(
            script_dir,
            "chrome-installation",
            "opt",
            "google",
            "chrome",
            "google-chrome"
        )

        user_data_dir = os.path.join(script_dir, "chrome-data")

        os.makedirs(user_data_dir, exist_ok=True)

        cmd = [
            chrome_path,
            f"--user-data-dir={user_data_dir}",
            "--no-default-browser-check",
            "--disable-extensions",
            "--disable-gpu",
            "--disable-dev-shm-usage"
        ]
        cmd.extend(sys.argv[1:])

        print(f"执行命令:", " ".join(cmd))

        process = subprocess.Popen(cmd)
        process.wait()
    except Exception as e:
        print(f"错误： {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
