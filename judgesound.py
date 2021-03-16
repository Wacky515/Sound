# !/usr/bin/python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Name:        judgesound.py
# Purpose:     In README.md
#
# Author:      Kilo11
#
# Created:     2016/03/24
# Last Change: 2021/03/16 17:19:43.
# Copyright:   (c) SkyDog 2016
# Licence:     SDS10004
# -----------------------------------------------------------------------------
""" OK/NG音声出力 処理 """

# モジュールインポート
import os
import sys
import time
import importlib

if os.name == "nt":
    import winsound

# Python2 用設定
if sys.version_info.major == 2:
    # sysモジュール リロード
    importlib.reload(sys)
    # デフォルトの文字コード 出力
    sys.setdefaultencoding("utf-8")


class JudgeSound:
    """ OK/NG判定音 出力 """

    def __init__(self):
        if sys.platform == "Darwin":
            print(">> Mac machine")
        elif sys.platform == "linux2":
            print(">> Linux machine")
        elif os.name == "nt":
            print(">> Windows machine")

    def beep_ok(self):
        """ OK判定音 出力 """
        try:
            if sys.platform == "Darwin":
                print(">> OK [Mac]")
                # os.system('>> say "OK"')
            elif sys.platform == "linux2":
                print(">> OK [Linux]")
                # print("\a")
            elif os.name == "nt":
                print(">> OK [Windows]")
                winsound.Beep(2000, 1000)
        except OSError:
            print(">> SOUND ERROR[OK SOUND]")
        finally:
            time.sleep(0.1)

    def beep_ng(self):
        """ NG判定音 出力 """
        try:
            if sys.platform == "Darwin":
                print(">> NG [Mac]")
                # os.system('>> say "NG"')
            elif sys.platform == "linux2":
                print(">> NG [Linux]")
                # print("\a")
            if os.name == "nt":
                print(">> NG [Windows]")
                winsound.Beep(2000, 500)
        except OSError:
            print(">> SOUND ERROR[OK SOUND]")
        finally:
            time.sleep(0.1)


def main():
    js = JudgeSound()

    js.beep_ok()
    time.sleep(0.5)

    js.beep_ng()
    time.sleep(0.5)


if __name__ == "__main__":
    main()
