#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: face.py
Description: Face model for Python SDK Sample.
"""

import wx

import util


class Face(object):
    """Face Model for each face."""
    def __init__(self, res, path, size=util.MAX_THUMBNAIL_SIZE):
        super(Face, self).__init__()
        self.path = path
        self.bmp = wx.Bitmap(path)
        self.name = None
        if res.get('faceId'):
            self.id = res['faceId']
        if res.get('persistedFaceId'):
            self.persisted_id = res['persistedFaceId']
        if res.get('faceRectangle'):
            rect = res['faceRectangle']
            self.left = int(rect['left'])
            self.top = int(rect['top'])
            self.width = int(rect['width'])
            self.height = int(rect['height'])
            self.bmp = self.bmp.GetSubBitmap(wx.Rect(
                self.left, self.top, self.width, self.height))
        if res.get('faceAttributes'):
            attr = res['faceAttributes']
            self.age = int(attr['age'])
            self.gender = attr['gender']
            self.smile = float(attr['smile']) > 0 and 'Smile' or 'Not Smile'
            self.glasses = attr['glasses']
        self.bmp = util.scale_bitmap(self.bmp, size)

    def set_name(self, name):
        """Set the name for the face."""
        self.name = name
