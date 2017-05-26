#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: panel_detection.py
Description: Detection Panel for Python SDK sample.
"""

import wx

import util
import model
from view import base


class DetectionPanel(base.MyPanel):
    """Detection Panel."""
    def __init__(self, parent):
        super(DetectionPanel, self).__init__(parent)

        self.vsizer = wx.BoxSizer(wx.VERTICAL)

        self.hsizer = wx.BoxSizer()
        self.hsizer.AddStretchSpacer()

        self.hvsizer = wx.BoxSizer(wx.VERTICAL)
        self.hvsizer.SetMinSize((util.INNER_PANEL_WIDTH, -1))

        label = (
            "To detect faces in an image, click the 'Choose Image' "
            "button. You will see a rectangle surrounding every face "
            "that the Face API detects. You will also see a list of "
            "attributes related to the faces."
        )
        self.static_text = wx.StaticText(self, label=label)
        self.static_text.Wrap(util.INNER_PANEL_WIDTH)
        self.hvsizer.Add(self.static_text, 0, wx.ALL, 5)

        self.vhsizer = wx.BoxSizer()
        self.vhsizer.SetMinSize((util.INNER_PANEL_WIDTH, -1))

        self.lsizer = wx.BoxSizer(wx.VERTICAL)
        self.lsizer.SetMinSize((util.MAX_IMAGE_SIZE, -1))

        flag = wx.EXPAND | wx.ALIGN_CENTER | wx.ALL
        self.btn = wx.Button(self, label='Choose Image')
        self.lsizer.Add(self.btn, 0, flag, 5)
        self.Bind(wx.EVT_BUTTON, self.OnChooseImage, self.btn)

        flag = wx.ALIGN_CENTER | wx.ALL
        self.bitmap = base.MyStaticBitmap(self)
        self.lsizer.Add(self.bitmap, 0, flag, 5)

        self.vhsizer.Add(self.lsizer, 0, wx.ALIGN_LEFT)
        self.vhsizer.AddStretchSpacer()

        self.rsizer = wx.BoxSizer(wx.VERTICAL)
        self.rsizer.SetMinSize((util.MAX_IMAGE_SIZE, -1))

        style = wx.ALIGN_CENTER
        flag = wx.ALIGN_CENTER | wx.EXPAND | wx.ALL
        self.result = wx.StaticText(self, style=style)
        self.rsizer.Add(self.result, 0, flag, 5)

        flag = wx.ALIGN_LEFT | wx.EXPAND | wx.ALL
        self.face_list = base.MyFaceList(self)
        self.rsizer.Add(self.face_list, 1, flag, 5)

        self.vhsizer.Add(self.rsizer, 0, wx.EXPAND)

        self.hvsizer.Add(self.vhsizer)

        self.hsizer.Add(self.hvsizer, 0)
        self.hsizer.AddStretchSpacer()

        self.vsizer.Add(self.hsizer, 3, wx.EXPAND)

        self.log = base.MyLog(self)
        self.vsizer.Add(self.log, 1, wx.EXPAND)

        self.SetSizerAndFit(self.vsizer)

    def OnChooseImage(self, evt):
        """Choose Image."""
        dlg = wx.FileDialog(self, wildcard=util.IMAGE_WILDCARD)
        if dlg.ShowModal() != wx.ID_OK:
            return
        path = dlg.GetPath()
        self.bitmap.set_path(path)
        self.async_detect(path)

    @util.async
    def async_detect(self, path):
        """Async detection."""
        self.log.log('Request: Detecting {}'.format(path))
        self.result.SetLabelText('Detecting ...')
        self.btn.Disable()
        self.face_list.Clear()
        self.face_list.Refresh()
        self.rsizer.Layout()
        self.vhsizer.Layout()

        try:
            attributes = (
                'age,gender,headPose,smile,facialHair,glasses,emotion,hair,'
                'makeup,occlusion,accessories,blur,exposure,noise'
            )
            res = util.CF.face.detect(path, False, False, attributes)
            faces = [model.Face(face, path) for face in res]
            self.face_list.SetItems(faces)
            util.draw_bitmap_rectangle(self.bitmap, faces)

            log_text = 'Response: Success. Detected {} face(s) in {}'.format(
                len(res), path)
            self.log.log(log_text)
            text = '{} face(s) has been detected.'.format(len(res))
            self.result.SetLabelText(text)
        except util.CF.CognitiveFaceException as exp:
            self.log.log('Response: {}. {}'.format(exp.code, exp.msg))

        self.btn.Enable()
        self.rsizer.Layout()
        self.vhsizer.Layout()
