#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: main.py
Description: main script for Python SDK sample.
"""

from view import MyApp


if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()
