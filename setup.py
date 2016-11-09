# -*- coding: utf-8 -*-

from distutils.core import setup
import py2exe
import sys

sys.argv.append("py2exe")

option = {
        "compressed": 1,
        "optimize": 2,
        "bundle_files": 1
        }

setup(
        options={"py2exe": {"dll_excludes": ["MSVCP90.dll"]}},
        console=[{"script": "judgesound.py"}],
        # console=[{"script": "judgesound.py", "icon_resources": "icon.ico"}],
        zipfile=None
        )
