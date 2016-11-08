# !/usr/bin/python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Name:        modtjudgesound.py
# Purpose:     In README.md
#
# Author:      Kilo11
#
# Created:     01/04/2016
# Copyright:   (c) SkyDog 2016
# Licence:     SDS10005
# -----------------------------------------------------------------------------

# モジュールインポート
import judgesound as js

import sys
# sysモジュール リロード
reload(sys)

# デフォルトの文字コード 出力
sys.setdefaultencoding("utf-8")

js = js.JudgeSound()
js.beep_ok()
js.beep_ng()


def main():
    pass

if __name__ == "__main__":
    main()
