#-------------------------------------------------------------------------------
# Name:        ModuleTestJudgeSound
# Purpose:
#
# Author:      Kilo11
#
# Created:     01/04/2016
# Copyright:   (c) SkyDog 2016
# Licence:     SDS10008-1
#-------------------------------------------------------------------------------
#!/usr/bin/python
# デフォルトの文字コード 変更
# -*- coding: utf-8 -*-

# モジュールインポート
import judgesound as js

import sys
# sysモジュール リロード
reload(sys)

# デフォルトの文字コード 出力
sys.setdefaultencoding("utf-8")

js = js.JudgeSound()
js.OkBeep()
js.NgBeep()

def main():
    pass

if __name__ == '__main__':
    main()
