#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: face.py
Description: Face model for Python SDK Sample.
"""
import wx

import util


class Rect(object):
    """Face Rectangle."""
    def __init__(self, rect):
        super(Rect, self).__init__()
        self.set_rect(rect)

    def set_rect(self, rect):
        """docstring for set_rect"""
        self.left = int(rect['left'])
        self.top = int(rect['top'])
        self.width = int(rect['width'])
        self.height = int(rect['height'])


class Attribute(object):
    """Attributes for face."""
    def __init__(self, attr):
        super(Attribute, self).__init__()
        self.set_attr(attr)

    def set_attr(self, attr):
        """Set the attribute value."""
        self.gender = attr['gender']
        self.age = int(attr['age'])
        if not attr['hair']['hairColor']:
            if attr['hair']['invisible']:
                self.hair = 'Invisible'
            else:
                self.hair = 'Bald'
        else:
            self.hair = max(
                attr['hair']['hairColor'],
                key=lambda x: x['confidence']
            )['color']
        self.facial_hair = sum(attr['facialHair'].values()) > 0 and 'Yes' \
            or 'No'
        self.makeup = any(attr['makeup'].values())
        self.emotion = util.key_with_max_value(attr['emotion'])
        self.occlusion = any(attr['occlusion'].values())
        self.exposure = attr['exposure']['exposureLevel']
        self.head_pose = "Pitch: {}, Roll:{}, Yaw:{}".format(
            attr['headPose']['pitch'],
            attr['headPose']['roll'],
            attr['headPose']['yaw']
        )
        if not attr['accessories']:
            self.accessories = 'NoAccessories'
        else:
            self.accessories = ' '.join(
                [str(x['type']) for x in attr['accessories']]
            )


class Face(object):
    """Face Model for each face."""
    def __init__(self, res, path, size=util.MAX_THUMBNAIL_SIZE):
        super(Face, self).__init__()
        self.path = path
        img = util.rotate_image(path)
        self.bmp = img.ConvertToBitmap()
        self.name = None
        if res.get('faceId'):
            self.id = res['faceId']
        if res.get('persistedFaceId'):
            self.persisted_id = res['persistedFaceId']
        if res.get('faceRectangle'):
            self.rect = Rect(res['faceRectangle'])
            self.bmp = self.bmp.GetSubBitmap(wx.Rect(
                self.rect.left,
                self.rect.top,
                self.rect.width,
                self.rect.height,
            ))
        if res.get('faceAttributes'):
            self.attr = Attribute(res['faceAttributes'])
        self.bmp = util.scale_image(
            self.bmp.ConvertToImage(),
            size=size,
        ).ConvertToBitmap()

    def set_name(self, name):
        """Set the name for the face."""
        self.name = name
