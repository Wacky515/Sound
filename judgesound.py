# !/usr/bin/python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        JudgeSound
# Purpose:
#
# Author:      Kilo11
#
# Created:     24/03/2016
# Copyright:   (c) SkyDog 2016
# Licence:     SDS10008
# -------------------------------------------------------------------------------

# モジュールインポート
import winsound
import time

import sys
# sysモジュール リロード
reload(sys)

# デフォルトの文字コード 出力
sys.setdefaultencoding("utf-8")


class JudgeSound:
    """ OK/NG判定音 出力 """
    def beep_ok(self):
        """ OK判定音 出力 """
        winsound.Beep(2000, 1000)
        print("OK!")
        print("")

    def beep_ng(self):
        """ NG判定音 出力 """
        for times in range(2):
            winsound.Beep(2000, 500)
            time.sleep(0.1)
        print("NG!")
        print("")


def main():
    js = JudgeSound()

    js.beep_ok()
    time.sleep(0.5)

    js.beep_ng()
    time.sleep(0.5)

if __name__ == '__main__':
    main()
