# !/usr/bin/python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Name:        judgesound.py
# Purpose:     In README.md
#
# Author:      Kilo11
#
# Created:     24/03/2016
# Copyright:   (c) SkyDog 2016
# Licence:     SDS10004
# -----------------------------------------------------------------------------

# モジュールインポート
import os
import sys
import time

if os.name == "nt":
    import winsound

# Python3用
import importlib

# sysモジュール リロード
if sys.version_info.major == 2:
    reload(sys)
# デフォルトの文字コード 出力
    sys.setdefaultencoding("utf-8")


class JudgeSound:
    """ OK/NG判定音 出力 """
    def __init__(self):
        if sys.platform == "linux2":
            print("Linux machine")
        elif sys.platform == "darwin":
            print("Mac machine")
        elif os.name == "nt":
            print("Windows machine")
        print("")

    def beep_ok(self):
        """ OK判定音 出力 """
        try:
            if os.name == "nt":
                winsound.Beep(2000, 1000)
            elif sys.platform == "darwin":
                os.system('say "OK"')
            elif sys.platform == "linux2":
                # print("\a")
                pass
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
            elif sys.platform == "darwin":
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
