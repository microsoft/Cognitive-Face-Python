#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: panel_group.py
Description: Group Panel for Python SDK sample.
"""

import os

import wx
import wx.lib.scrolledpanel as scrolled

import util
import model
from view import base


class GroupPanel(base.MyPanel):
    """Group Panel."""
    def __init__(self, parent):
        super(GroupPanel, self).__init__(parent)

        self.face_paths = []
        self.faces = {}

        self.vsizer = wx.BoxSizer(wx.VERTICAL)

        self.panel = scrolled.ScrolledPanel(self)

        self.hsizer = wx.BoxSizer()
        self.hsizer.AddStretchSpacer()

        self.hvsizer = wx.BoxSizer(wx.VERTICAL)
        self.hvsizer.SetMinSize((util.INNER_PANEL_WIDTH, -1))

        label = (
            'Click the button below to select a folder containing face '
            'images.\nThe images will be grouped based on similarity.\n'
            'You will see the different groups under the '
            '"Grouping Results" label.'
        )
        self.static_text = wx.StaticText(self.panel, label=label)
        self.static_text.Wrap(util.INNER_PANEL_WIDTH)
        self.hvsizer.Add(self.static_text, 0, wx.ALL, 0)

        self.vhsizer = wx.BoxSizer()

        self.lsizer = wx.BoxSizer(wx.VERTICAL)
        self.lsizer.SetMinSize((util.MAX_IMAGE_SIZE, -1))

        flag = wx.EXPAND | wx.ALIGN_CENTER | wx.ALL
        self.btn = wx.Button(self.panel, label='Group')
        self.lsizer.Add(self.btn, 0, flag, 5)
        self.Bind(wx.EVT_BUTTON, self.OnChooseFolder, self.btn)

        self.grid = base.MyGridStaticBitmap(self.panel, 0, 4, 0, 0)
        self.lsizer.Add(self.grid, 0, wx.ALL, 5)

        self.vhsizer.Add(self.lsizer, 1, wx.EXPAND)
        self.vhsizer.AddSpacer(90)

        self.rsizer = wx.BoxSizer(wx.VERTICAL)
        self.rsizer.SetMinSize((util.MAX_IMAGE_SIZE, -1))

        flag = wx.ALIGN_CENTER | wx.EXPAND | wx.ALL
        self.result_text = wx.StaticText(self.panel, label='Grouping Results:')
        self.rsizer.Add(self.result_text, 0, flag, 5)

        self.result = base.GroupResult(self.panel)
        self.rsizer.Add(self.result, 0, wx.EXPAND)

        self.vhsizer.Add(self.rsizer, 1, wx.EXPAND)

        self.hvsizer.Add(self.vhsizer)

        self.hsizer.Add(self.hvsizer)
        self.hsizer.AddStretchSpacer()
        self.hsizer.Layout()

        self.panel.SetSizer(self.hsizer)
        self.panel.Layout()
        self.panel.SetupScrolling(scroll_x=False)

        self.vsizer.Add(self.panel, 3, wx.EXPAND)

        self.log = base.MyLog(self)
        self.vsizer.Add(self.log, 1, wx.EXPAND)

        self.SetSizerAndFit(self.vsizer)

    def OnChooseFolder(self, evt):
        """Choose Folder."""
        dlg = wx.DirDialog(self)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            del self.face_paths[:]
            self.faces.clear()
            for root, dirs, files in os.walk(path):
                if files:
                    self.face_paths.extend([
                        os.path.join(root, filename)
                        for filename in files
                    ])

            self.btn.Disable()

            self.log.log(
                'Request: Preparing faces for grouping, detecting faces in '
                'chosen folder.'
            )
            self.grid.set_paths(self.face_paths)
            for path in self.face_paths:
                try:
                    res = util.CF.face.detect(path)
                except util.CF.CognitiveFaceException:
                    continue
                for entry in res:
                    face = model.Face(entry, path)
                    self.faces[face.id] = face
            self.grid.set_faces(self.faces.values())
            self.log.log(
                'Response: Success. Total {0} faces are detected.'.format(
                    len(self.faces)))

            self.log.log('Request: Grouping {0} faces.'.format(
                len(self.faces)))
            res = util.CF.face.group(self.faces.keys())
            self.result.set_data(self.faces, res)
            len_groups = len(res['groups'])
            if res.get('messyGroup'):
                len_groups += 1
            self.log.log(
                'Response: Success. {0} faces grouped into {1} groups'.format(
                    len(self.faces), len_groups))

            self.btn.Enable()
