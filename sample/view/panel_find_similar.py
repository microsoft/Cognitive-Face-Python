#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: panel_find_similar.py
Description: Find Similar Panel for Python SDK sample.
"""

import os
import uuid

import wx
import wx.lib.scrolledpanel as scrolled

import util
import model
from view import base


class FindSimilarPanel(base.MyPanel):
    """FindSimilar Panel."""
    def __init__(self, parent):
        super(FindSimilarPanel, self).__init__(parent)

        self.face_list_id = str(uuid.uuid1())
        self.face_list_name = self.face_list_id
        self.face_paths = []
        self.detected_face_paths = []
        self.faces = {}
        self.persisted_faces = {}

        self.vsizer = wx.BoxSizer(wx.VERTICAL)

        self.panel = scrolled.ScrolledPanel(self)

        self.hsizer = wx.BoxSizer()
        self.hsizer.AddStretchSpacer()

        self.hvsizer = wx.BoxSizer(wx.VERTICAL)
        self.hvsizer.SetMinSize((util.INNER_PANEL_WIDTH, -1))

        label = (
            'Find faces that are similar to a given face (the query '
            'face).\nClick "Load Candidate Faces" to select a folder '
            'containing images of the faces you want to compare to the '
            'query face.\nNext, click "Open Query Face" to select the '
            'query face image.\nScroll down to see the results '
            'displayed under the query face.\n'
        )
        self.static_text = wx.StaticText(self.panel, label=label)
        self.static_text.Wrap(util.INNER_PANEL_WIDTH)
        self.hvsizer.Add(self.static_text, 0, wx.ALL, 0)

        self.vhsizer = wx.BoxSizer()

        self.lsizer = wx.BoxSizer(wx.VERTICAL)
        self.lsizer.SetMinSize((util.MAX_IMAGE_SIZE, -1))

        flag = wx.EXPAND | wx.ALIGN_CENTER | wx.ALL
        self.btn_folder = wx.Button(self.panel, label='Load Candidate Faces')
        self.lsizer.Add(self.btn_folder, 0, flag, 5)
        self.Bind(wx.EVT_BUTTON, self.OnChooseFolder, self.btn_folder)

        flag = wx.ALIGN_CENTER | wx.ALL
        self.grid = base.MyGridStaticBitmap(self.panel, 0, 4, 0, 0)
        self.lsizer.Add(self.grid, 0, flag, 5)

        self.vhsizer.Add(self.lsizer, 1, wx.EXPAND)
        self.vhsizer.AddSpacer(90)

        self.rsizer = wx.BoxSizer(wx.VERTICAL)
        self.rsizer.SetMinSize((util.MAX_IMAGE_SIZE, -1))

        flag = wx.EXPAND | wx.ALIGN_CENTER | wx.ALL
        self.btn_file = wx.Button(self.panel, label='Open Query Face')
        self.rsizer.Add(self.btn_file, 0, flag, 5)
        self.Bind(wx.EVT_BUTTON, self.OnChooseImage, self.btn_file)

        flag = wx.ALIGN_CENTER | wx.ALL
        self.bitmap = base.MyStaticBitmap(self.panel)
        self.rsizer.Add(self.bitmap, 0, flag, 5)

        self.result = base.FindSimilarsResult(self.panel)
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

        self.btn_file.Disable()

    def OnChooseFolder(self, evt):
        """Choose Folder."""
        face_list_exists = False

        try:
            self.log.log((
                'Request: Face List {} will be used to build a person '
                'database. Checking whether the face list exists.'
            ).format(self.face_list_id))
            util.CF.face_list.get(self.face_list_id)
            face_list_exists = True
            self.log.log('Response: Face List {} exists.'.format(
                self.face_list_id))
        except util.CF.CognitiveFaceException as exp:
            if exp.code != 'FaceListNotFound':
                self.log.log('Response: {}. {}'.format(exp.code, exp.msg))
                return
            else:
                self.log.log(
                    'Response: Face List {} did not exist previously.'.format(
                        self.face_list_id))

        if face_list_exists:
            text = (
                'Requires a clean up for face list "{0}" before setting up a '
                'new face list. Click OK to proceed, face list "{0}" will be '
                'cleared.'
            ).format(self.face_list_id)
            title = 'Warning'
            style = wx.YES_NO | wx.ICON_WARNING
            result = wx.MessageBox(text, title, style)
            if result == wx.YES:
                util.CF.face_list.delete(self.face_list_id)
            else:
                return

        dlg = wx.DirDialog(self)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            del self.face_paths[:]
            for root, dirs, files in os.walk(path):
                if files:
                    self.face_paths.extend([
                        os.path.join(root, filename)
                        for filename in files
                    ])
        self.panel.SetupScrolling(scroll_x=False)

        self.log.log('Request: Preparing, detecting faces in chosen folder.')
        self.btn_folder.Disable()
        self.btn_file.Disable()
        self.persisted_faces.clear()

        del self.detected_face_paths[:]
        util.CF.face_list.create(self.face_list_id)
        for path in self.face_paths:
            try:
                res = util.CF.face_list.add_face(path, self.face_list_id)
            except util.CF.CognitiveFaceException as exp:
                self.log.log((
                    '[Error] Add "{}" to FaceList {}: Code: {}, Message: {}'
                ).format(path, self.face_list_id, exp.code, exp.msg))
                continue
            self.detected_face_paths.append(path)
            face = model.Face(res, path)
            self.persisted_faces[face.persisted_id] = face
        self.log.log(
            'Response: Success. Total {0} faces are detected.'.format(
                len(self.persisted_faces)))

        self.grid.set_paths(self.detected_face_paths)
        self.btn_folder.Enable()
        self.btn_file.Enable()

    def OnChooseImage(self, evt):
        """Choose Image."""
        dlg = wx.FileDialog(self, wildcard=util.IMAGE_WILDCARD)
        if dlg.ShowModal() != wx.ID_OK:
            return
        path = dlg.GetPath()
        self.bitmap.set_path(path)

        self.log.log('Detecting faces in {}'.format(path))
        self.faces.clear()

        res = util.CF.face.detect(path)
        for entry in res:
            face = model.Face(entry, path)
            self.faces[face.id] = face
        util.draw_bitmap_rectangle(self.bitmap, self.faces.values())

        self.log.log('Success. Detected {} face(s) in {}'.format(
            len(self.faces), path))
        res_tot = {
            'matchPerson': {},
            'matchFace': {},
        }
        for face_id in self.faces:
            self.log.log((
                'Request: Finding similar faces in Personal Match Mode for '
                'face {}'
            ).format(face_id))
            for mode in ('matchPerson', 'matchFace'):
                res_tot[mode][face_id] = []
                res = util.CF.face.find_similars(
                    face_id,
                    face_list_id=self.face_list_id,
                    mode=mode,
                )
                self.log.log((
                    'Response: Found {} similar faces for face {} in {} mode'
                ).format(len(res), face_id, mode))
                for entry in res:
                    persisted_id = entry['persistedFaceId']
                    confidence = entry['confidence']
                    res_tot[mode][face_id].append((
                        self.persisted_faces[persisted_id], confidence))
        self.result.set_data(self.faces, res_tot)
        self.panel.SetupScrolling(scroll_x=False)
