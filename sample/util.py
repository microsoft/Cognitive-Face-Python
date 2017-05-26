#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: util.py
Description: util module for Python SDK sample.
"""

from threading import Thread
import operator
import os.path

from PIL import Image
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
ENDPOINT_FILENAME = 'Endpoint.txt'
ORIENTATION_TAG = 274

LOG_FACE_LIST_REQUEST = (
    'Request: Face List {} will be used for build person database. '
    'Checking whether group exists.'
)
LOG_FACE_LIST_NOT_EXIST = 'Response: Face List {} does not exist before.'
LOG_FACE_LIST_EXIST = 'Response: Face List {} exists.'
LABEL_FACE = (
    '{}, {} years old\n'
    'Hair: {}, Facial Hair: {}\n'
    'Makeup: {}, Emotion: {}\n'
    'Occluded: {}, Exposure: {}\n'
    '{}\n{}\n'
)


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


class Endpoint(object):
    """Endpoint."""

    @classmethod
    def get(cls):
        """Get the endpoint."""
        if not hasattr(cls, 'endpoint'):
            cls.endpoint = ''
        if not cls.endpoint:
            if os.path.isfile(ENDPOINT_FILENAME):
                with file(ENDPOINT_FILENAME) as fin:
                    cls.endpoint = fin.read().strip()
            else:
                cls.endpoint = CF.BaseUrl.get()
        CF.BaseUrl.set(cls.endpoint)
        return cls.endpoint

    @classmethod
    def set(cls, endpoint):
        """Set the endpoint."""
        cls.endpoint = endpoint
        with file(ENDPOINT_FILENAME, 'w') as fout:
            print >>fout, endpoint
        CF.BaseUrl.set(cls.endpoint)

    @classmethod
    def delete(cls):
        """Delete the endpoint."""
        cls.endpoint = ''
        if os.path.isfile(ENDPOINT_FILENAME):
            os.remove(ENDPOINT_FILENAME)
        CF.BaseUrl.set(CF.util.DEFAULT_BASE_URL)


def scale_image(img, size=MAX_IMAGE_SIZE):
    """Scale the wx.Image."""
    width = img.GetWidth()
    height = img.GetHeight()
    if width > height:
        new_width = size
        new_height = size * height / width
    else:
        new_height = size
        new_width = size * width / height
    img = img.Scale(new_width, new_height)
    return img


def rotate_image(path):
    """Rotate the image from path and return wx.Image."""
    img = Image.open(path)
    try:
        exif = img._getexif()
        if exif[ORIENTATION_TAG] == 3:
            img = img.rotate(180, expand=True)
        elif exif[ORIENTATION_TAG] == 6:
            img = img.rotate(270, expand=True)
        elif exif[ORIENTATION_TAG] == 8:
            img = img.rotate(90, expand=True)
    except:
        pass
    return pil_image_to_wx_image(img)


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
            face.rect.left * bitmap.scale,
            face.rect.top * bitmap.scale,
            face.rect.width * bitmap.scale,
            face.rect.height * bitmap.scale,
        )
        if face.name:
            text_width, text_height = dc.GetTextExtent(face.name)
            dc.DrawText(face.name,
                        face.rect.left * bitmap.scale,
                        face.rect.top * bitmap.scale - text_height)
    dc.SelectObject(wx.NullBitmap)
    bitmap.bitmap.SetBitmap(bitmap.bmp)


def pil_image_to_wx_image(pil_image):
    """Convert from PIL image to wx image."""
    wx_image = wx.EmptyImage(pil_image.width, pil_image.height)
    wx_image.SetData(pil_image.convert("RGB").tobytes())
    return wx_image


def key_with_max_value(item):
    """Get the key with maximum value in a dict."""
    return max(item.iteritems(), key=operator.itemgetter(1))[0]


def async(func):
    """Async wrapper."""
    def wrapper(*args, **kwargs):
        """docstring for wrapper"""
        thr = Thread(target=func, args=args, kwargs=kwargs)
        thr.start()
    return wrapper
