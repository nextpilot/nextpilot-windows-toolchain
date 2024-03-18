import os
import sys


def add_to_contex_menu():
    import winreg

    pass


def add_to_windows_terminal(action="install"):
    import json

    npwt_root = os.path.normpath(os.path.join(os.path.dirname(__file__), "../../"))

    npwt_setting = {
        "commandline": f"%windir%\\System32\\cmd.exe /K {npwt_root}\init.bat",
        "guid": "{c06ccb37-4fca-4609-b969-30aa1b3d8549}",
        "hidden": False,
        # "icon": "",
        "name": "Nextpilot Windows Toolchain",
        # "source": "Nextpilot.WindowsToolchain",
        # "startingDirectory": "",
    }

    # C:\Users\Administrator\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState
    wt_setting_file = os.path.join(
        os.environ["LOCALAPPDATA"],
        "Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json",
    )

    with open(wt_setting_file) as f:
        wt_setting = json.load(f)

    # 如果已经添加了，则先删除
    for dv in wt_setting["profiles"]["list"]:
        if dv["guid"] == npwt_setting["guid"]:
            wt_setting["profiles"]["list"].remove(dv)

    # 新增npwt的配置
    if action == "install":
        wt_setting["profiles"]["list"].insert(0, npwt_setting)
    else:
        pass

    with open(wt_setting_file, "w") as f:
        json.dump(wt_setting, f, indent=4)


if __name__ == "main":
    add_to_windows_terminal()
