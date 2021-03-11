# !/usr/bin/python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Name:        modtjudgesound.py
# Purpose:     In README.md
#
# Author:      Kilo11
#
# Created:     2016/04/01
# Last Change: 2021/03/11 13:40:41.
# Copyright:   (c) SkyDog 2016
# Licence:     SDS10005
# -----------------------------------------------------------------------------
""" OK/NG音声出力 処理 GUI """

# モジュールインポート
import sys
import importlib
import judgesound as js

# Python2 用設定
if sys.version_info.major == 2:
    # sysモジュール リロード
    importlib.reload(sys)
    # デフォルトの文字コード 出力
    sys.setdefaultencoding("utf-8")


js = js.JudgeSound()
js.beep_ok()
js.beep_ng()


def main():
    pass


if __name__ == "__main__":
    main()
