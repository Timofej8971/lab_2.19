#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import pathlib


def tree(directory):
    time, file_path = max((f.stat().st_mtime, f) for f in directory.iterdir())
    print(datetime.fromtimestamp(time), file_path)


if __name__ == '__main__':
    tree(pathlib.Path.cwd())
    print(pathlib.Path.home())