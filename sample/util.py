#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: util.py
Description: util module for Python SDK sample.
"""

from threading import Thread
import os.path

import wx

try:
    import cognitive_face as CF
except ImportError:
    import sys
    ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, ROOT_DIR)
    import cognitive_face as CF


IMAGE_WILDCARD = 'Image files (*.jpg, *.png)|*.jpg; *.png'
INNER_PANEL_WIDTH = 710
MAX_IMAGE_SIZE = 300
MAX_THUMBNAIL_SIZE = 75
STYLE = wx.SIMPLE_BORDER
SUBSCRIPTION_KEY_FILENAME = 'Subscription.txt'

LOG_FACE_LIST_REQUEST = (
    'Request: Face List {} will be used for build person database. '
    'Checking whether group exists.'
)
LOG_FACE_LIST_NOT_EXIST = 'Response: Face List {} does not exist before.'
LOG_FACE_LIST_EXIST = 'Response: Face List {} exists.'


class SubscriptionKey(object):
    """Subscription Key."""

    @classmethod
    def get(cls):
        """Get the subscription key."""
        if not hasattr(cls, 'key'):
            cls.key = ''
        if not cls.key:
            if os.path.isfile(SUBSCRIPTION_KEY_FILENAME):
                with file(SUBSCRIPTION_KEY_FILENAME) as fin:
                    cls.key = fin.read().strip()
            else:
                cls.key = ''
        CF.Key.set(cls.key)
        return cls.key

    @classmethod
    def set(cls, key):
        """Set the subscription key."""
        cls.key = key
        with file(SUBSCRIPTION_KEY_FILENAME, 'w') as fout:
            print >>fout, key
        CF.Key.set(cls.key)

    @classmethod
    def delete(cls):
        """Delete the subscription key."""
        cls.key = ''
        if os.path.isfile(SUBSCRIPTION_KEY_FILENAME):
            os.remove(SUBSCRIPTION_KEY_FILENAME)
        CF.Key.set(cls.key)


def scale_bitmap(bitmap, size=MAX_IMAGE_SIZE):
    """Scale the image."""
    img = bitmap.ConvertToImage()
    width = img.GetWidth()
    height = img.GetHeight()
    if width > height:
        new_width = size
        new_height = size * height / width
    else:
        new_height = size
        new_width = size * width / height
    img = img.Scale(new_width, new_height)
    return wx.BitmapFromImage(img)


def draw_bitmap_rectangle(bitmap, faces):
    """Draw rectangle on bitmap."""
    dc = wx.MemoryDC(bitmap.bmp)
    dc.SetPen(wx.BLUE_PEN)
    dc.SetBrush(wx.TRANSPARENT_BRUSH)
    dc.SetTextBackground('black')
    dc.SetTextForeground('white')
    dc.SetBackgroundMode(wx.SOLID)
    dc.SetFont(wx.Font(8,
                       wx.FONTFAMILY_DEFAULT,
                       wx.FONTSTYLE_NORMAL,
                       wx.FONTWEIGHT_BOLD))
    for face in faces:
        dc.DrawRectangle(
            face.left * bitmap.scale,
            face.top * bitmap.scale,
            face.width * bitmap.scale,
            face.height * bitmap.scale,
        )
        if face.name:
            text_width, text_height = dc.GetTextExtent(face.name)
            dc.DrawText(face.name,
                        face.left * bitmap.scale,
                        face.top * bitmap.scale - text_height)
    dc.SelectObject(wx.NullBitmap)
    bitmap.bitmap.SetBitmap(bitmap.bmp)


def async(func):
    """Async wrapper."""
    def wrapper(*args, **kwargs):
        """docstring for wrapper"""
        thr = Thread(target=func, args=args, kwargs=kwargs)
        thr.start()
    return wrapper
