# !/usr/bin/python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Name:        judgesound.py
# Purpose:     In README.md
#
# Author:      Kilo11
#
# Created:     2016/03/24
# Last Change: 2021/03/04 10:42:19.
# Copyright:   (c) SkyDog 2016
# Licence:     SDS10004
# -----------------------------------------------------------------------------

# モジュールインポート
import os
import sys
import time

if os.name == "nt":
    import winsound

# Python3 用インポート
if sys.version_info.major == 3:
    import importlib

# Python2 用設定
if sys.version_info.major == 2:
    # sysモジュール リロード
    reload(sys)
    # デフォルトの文字コード 出力
    sys.setdefaultencoding("utf-8")


class JudgeSound:
    """ OK/NG判定音 出力 """
    def __init__(self):
        if sys.platform == "darwin":
            print("Mac machine")
        elif sys.platform == "linux2":
            print("Linux machine")
        elif os.name == "nt":
            print("Windows machine")
        print("")

    def beep_ok(self):
        """ OK判定音 出力 """
        try:
            if sys.platform == "darwin":
                os.system('say "OK"')
            elif sys.platform == "linux2":
                # print("\a")
                pass
            elif os.name == "nt":
                winsound.Beep(2000, 1000)
            print("OK!")
            print("")
        except:
            print("Sound error(OK)")
            print("")

    def beep_ng(self):
        """ NG判定音 出力 """
        try:
            if sys.platform != "darwin":
                for times in range(2):
                    if os.name == "nt":
                        winsound.Beep(2000, 500)
                    elif os.name == "posix":
                        print("\a")
                    time.sleep(0.1)
            else:
                os.system('say "NG"')
            print("NG!")
            print("")
        except:
            print("Sound error(NG)")
            print("")


def main():
    js = JudgeSound()

    js.beep_ok()
    time.sleep(0.5)

    js.beep_ng()
    time.sleep(0.5)

if __name__ == "__main__":
    main()
