#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: panel_verification.py
Description: Verification Panel for Python SDK sample.
"""

import os
import uuid

import wx
import wx.lib.scrolledpanel as scrolled

import util
import model
from view import base


class VerificationPanel(base.MyPanel):
    """Verification Panel."""
    def __init__(self, parent):
        super(VerificationPanel, self).__init__(parent)

        self.face_ids = {
            'face_id': None,
            'another_face_id': None,
            'person_face_id': None,
        }
        self.person_group_id = str(uuid.uuid1())
        self.person_name = None
        self.person_id = None
        self.face_paths = []
        self.detected_face_paths = []

        self.vsizer = wx.BoxSizer(wx.VERTICAL)

        self.panel = scrolled.ScrolledPanel(self)

        self.hsizer = wx.BoxSizer()
        self.hsizer.AddStretchSpacer()

        self.hvsizer = wx.BoxSizer(wx.VERTICAL)
        self.hvsizer.SetMinSize((util.INNER_PANEL_WIDTH, -1))

        label = (
            "Demo 1: Face-to-face verification determines whether "
            "two faces belong to the same person. Choose two images "
            "with a single face each. Then click 'Verify' to get "
            "the verification result."
        )
        self.static_text = wx.StaticText(self.panel, label=label)
        self.static_text.Wrap(util.INNER_PANEL_WIDTH)
        self.hvsizer.Add(self.static_text, 0, wx.ALL, 0)

        self.vhsizer1 = wx.BoxSizer()

        self.lsizer1 = wx.BoxSizer(wx.VERTICAL)
        self.lsizer1.SetMinSize((util.MAX_IMAGE_SIZE, -1))

        flag = wx.EXPAND | wx.ALIGN_CENTER | wx.ALL
        self.btn_face2face_1 = wx.Button(self.panel, label='Choose Image')
        self.lsizer1.Add(self.btn_face2face_1, 0, flag, 5)

        flag = wx.ALIGN_CENTER | wx.ALL
        self.bitmap_face2face_1 = base.MyStaticBitmap(self.panel)
        self.lsizer1.Add(self.bitmap_face2face_1, 0, flag, 5)

        self.btn_face2face_1.Bind(
            wx.EVT_BUTTON,
            lambda evt: self.OnChooseImage(
                evt, self.bitmap_face2face_1, 'face_id'))

        self.vhsizer1.Add(self.lsizer1, 1, wx.EXPAND)

        self.msizer1 = wx.BoxSizer(wx.VERTICAL)
        self.msizer1.SetMinSize((90, -1))

        self.btn_verify_1 = wx.Button(self.panel, label='Verify')
        self.msizer1.Add(self.btn_verify_1, 0, wx.EXPAND | wx.ALL, 5)

        self.result_1 = wx.StaticText(self.panel, label='Results:')
        self.msizer1.Add(self.result_1, 0, wx.EXPAND | wx.ALL, 5)

        self.btn_verify_1.Bind(
            wx.EVT_BUTTON,
            lambda evt: self.OnVerify(evt, 'face2face', self.result_1))

        self.vhsizer1.Add(self.msizer1, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.rsizer1 = wx.BoxSizer(wx.VERTICAL)
        self.rsizer1.SetMinSize((util.MAX_IMAGE_SIZE, -1))

        flag = wx.EXPAND | wx.ALIGN_CENTER | wx.ALL
        self.btn_face2face_2 = wx.Button(self.panel, label='Choose Image')
        self.rsizer1.Add(self.btn_face2face_2, 0, flag, 5)

        flag = wx.ALIGN_CENTER | wx.ALL
        self.bitmap_face2face_2 = base.MyStaticBitmap(self.panel)
        self.rsizer1.Add(self.bitmap_face2face_2, 0, flag, 5)

        self.btn_face2face_2.Bind(
            wx.EVT_BUTTON,
            lambda evt: self.OnChooseImage(
                evt, self.bitmap_face2face_2, 'another_face_id'))

        self.vhsizer1.Add(self.rsizer1, 1, wx.EXPAND)

        self.hvsizer.Add(self.vhsizer1)

        label = (
            "Demo 2: Face-to-person verification determines whether a "
            "face belongs to a given person. Click 'Load Person' to "
            "pick a folder containing the images of one person's face. "
            "Next, click 'Choose Image' to pick a face image of the "
            "same person (or of a different person). Finally, click "
            "'Verify' to see the verification result."
        )
        self.static_text = wx.StaticText(self.panel, label=label)
        self.static_text.Wrap(util.INNER_PANEL_WIDTH)
        self.hvsizer.Add(self.static_text, 0, wx.ALL, 0)

        self.vhsizer2 = wx.BoxSizer()

        self.lsizer2 = wx.BoxSizer(wx.VERTICAL)
        self.lsizer2.SetMinSize((util.MAX_IMAGE_SIZE, -1))

        flag = wx.EXPAND | wx.ALIGN_CENTER | wx.ALL
        self.btn_face2person_1 = wx.Button(self.panel, label='Load Person')
        self.lsizer2.Add(self.btn_face2person_1, 0, flag, 5)
        self.Bind(wx.EVT_BUTTON, self.OnChooseFolder, self.btn_face2person_1)

        flag = wx.ALIGN_CENTER | wx.ALL
        self.grid = base.MyGridStaticBitmap(self.panel, 0, 4, 0, 0)
        self.lsizer2.Add(self.grid, 0, flag, 5)

        self.vhsizer2.Add(self.lsizer2, 1, wx.EXPAND)

        self.msizer2 = wx.BoxSizer(wx.VERTICAL)
        self.msizer2.SetMinSize((90, -1))

        self.btn_verify_2 = wx.Button(self.panel, label='Verify')
        self.msizer2.Add(self.btn_verify_2, 0, wx.EXPAND | wx.ALL, 5)

        self.result_2 = wx.StaticText(self.panel, label='Results:')
        self.msizer2.Add(self.result_2, 0, wx.EXPAND | wx.ALL, 5)

        self.btn_verify_2.Bind(
            wx.EVT_BUTTON,
            lambda evt: self.OnVerify(evt, 'face2person', self.result_2))

        self.vhsizer2.Add(self.msizer2, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.rsizer2 = wx.BoxSizer(wx.VERTICAL)
        self.rsizer2.SetMinSize((util.MAX_IMAGE_SIZE, -1))

        flag = wx.EXPAND | wx.ALIGN_CENTER | wx.ALL
        self.btn_face2person_2 = wx.Button(self.panel, label='Choose Image')
        self.rsizer2.Add(self.btn_face2person_2, 0, flag, 5)

        flag = wx.ALIGN_CENTER | wx.ALL
        self.bitmap_face2person = base.MyStaticBitmap(self.panel)
        self.rsizer2.Add(self.bitmap_face2person, 0, flag, 5)

        self.btn_face2person_2.Bind(
            wx.EVT_BUTTON,
            lambda evt: self.OnChooseImage(
                evt, self.bitmap_face2person, 'person_face_id'))

        self.vhsizer2.Add(self.rsizer2, 1, wx.EXPAND)

        self.hvsizer.Add(self.vhsizer2)

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

        self.btn_verify_1.Disable()
        self.btn_verify_2.Disable()

    def OnChooseImage(self, evt, bitmap, face_id):
        """Choose Image"""
        dlg = wx.FileDialog(self, wildcard=util.IMAGE_WILDCARD)
        if dlg.ShowModal() != wx.ID_OK:
            return
        path = dlg.GetPath()

        self.log.log('Request: Detecting {}'.format(path))
        res = util.CF.face.detect(path)
        faces = [model.Face(face, path) for face in res]
        self.log.log('Response: Success. Detected {} face(s) in {}'.format(
            len(res), path))

        if len(faces) > 1:
            text = (
                'Verification accepts two faces as input, please pick images'
                'with only one detectable face in it.'
            )
            title = 'Warning'
            style = wx.OK | wx.ICON_WARNING
            wx.MessageBox(text, title, style)
            return

        bitmap.set_path(path)
        util.draw_bitmap_rectangle(bitmap, faces)
        self.face_ids[face_id] = faces[0].id
        self.check_btn_verify()

    def OnChooseFolder(self, evt):
        """Choose Folder."""
        self.log.log((
            'Request: Group {0} will be used to build a person database. '
            'Checking whether the group exists.'
        ).format(self.person_group_id))
        try:
            util.CF.person_group.get(self.person_group_id)
            self.log.log('Response: Group {0} exists.'.format(
                self.person_group_id))
            text = (
                'Requires a clean up for group "{0}" before setting up a '
                'new person database. Click YES to proceed, group "{0}" '
                'will be cleared.'
            ).format(self.person_group_id)
            title = 'Warning'
            style = wx.YES_NO | wx.ICON_WARNING
            result = wx.MessageBox(text, title, style)
            if result == wx.YES:
                util.CF.person_group.delete(self.person_group_id)
                self.person_id = None
            else:
                return
        except util.CF.CognitiveFaceException as exp:
            if exp.code != 'PersonGroupNotFound':
                self.log.log('Response: {}. {}'.format(exp.code, exp.msg))
                return
            else:
                self.log.log((
                    'Response: Group {0} does not exist previously.'
                ).format(self.person_group_id))

        dlg = wx.DirDialog(self)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.person_name = os.path.basename(path)
            del self.face_paths[:]
            for root, dirs, files in os.walk(path):
                if files:
                    self.face_paths.extend([
                        os.path.join(root, filename)
                        for filename in files
                    ])
            self.log.log('Request: Creating group "{0}"'.format(
                self.person_group_id))
            util.CF.person_group.create(self.person_group_id)
            self.log.log('Response: Success. Group "{0}" created'.format(
                self.person_group_id))
            self.log.log((
                'Preparing person for verification, detecting faces in chosen '
                'folder.'))
            self.log.log('Request: Creating person "{0}"'.format(
                self.person_name))
            res = util.CF.person.create(self.person_group_id, self.person_name)
            self.person_id = res['personId']
            self.log.log((
                'Response: Success. Person "{0}" (PersonID:{1}) created'
            ).format(
                self.person_name, self.person_id
            ))
            del self.detected_face_paths[:]
            for path in self.face_paths:
                res = util.CF.person.add_face(path,
                                              self.person_group_id,
                                              self.person_id)
                if res.get('persistedFaceId'):
                    self.detected_face_paths.append(path)
            self.log.log((
                'Response: Success. Total {0} faces are detected.'
            ).format(len(self.detected_face_paths)))
            res = util.CF.person_group.train(self.person_group_id)
            self.grid.set_paths(self.detected_face_paths)
            self.panel.SetupScrolling(scroll_x=False)
            self.check_btn_verify()

    def OnVerify(self, evt, mode, result):
        """Verify the faces."""
        if mode == 'face2face':
            self.log.log('Request: Verifying face {0} and {1}'.format(
                self.face_ids['face_id'], self.face_ids['another_face_id']))
            res = util.CF.face.verify(self.face_ids['face_id'],
                                      self.face_ids['another_face_id'])
            if res['isIdentical']:
                self.log.log((
                    'Response: Success. Face {0} and {1} belong to the same '
                    'person'
                ).format(
                    self.face_ids['face_id'],
                    self.face_ids['another_face_id']
                ))
                text = (
                    'Results: \nConfidence = {0}, two faces belong to the '
                    'same person'
                ).format(res['confidence'])
            else:
                self.log.log((
                    'Response: Success. Face {0} and {1} do not belong to the '
                    'same person'
                ).format(
                    self.face_ids['face_id'],
                    self.face_ids['another_face_id']
                ))
                text = (
                    'Results: \nConfidence = {0}, two faces do not belong to '
                    'the same person'
                ).format(res['confidence'])
        else:
            util.CF.util.wait_for_training(self.person_group_id)
            self.log.log('Request: Verifying face {0} and person {1}'.format(
                self.face_ids['person_face_id'], self.person_id))
            res = util.CF.face.verify(self.face_ids['person_face_id'],
                                      person_group_id=self.person_group_id,
                                      person_id=self.person_id)
            if res['isIdentical']:
                self.log.log((
                    'Response: Success. Face {0} belongs to person {1}'
                ).format(
                    self.face_ids['person_face_id'],
                    self.person_name
                ))
                text = (
                    'Results: \n'
                    'Confidence = {0}, the face belongs to the person'
                ).format(res['confidence'])
            else:
                self.log.log((
                    'Response: Success. Face {0} does not belong to person {1}'
                ).format(
                    self.face_ids['person_face_id'],
                    self.person_name
                ))
                text = (
                    'Results: \nConfidence = {0}, the face does not belong to'
                    'the person'
                ).format(res['confidence'])
        result.SetLabelText(text)
        result.Wrap(88)

    def check_btn_verify(self):
        """Check whether the verify button is valid."""
        if self.face_ids['face_id'] and self.face_ids['another_face_id']:
            self.btn_verify_1.Enable()

        if self.person_id and self.face_ids['person_face_id']:
            self.btn_verify_2.Enable()
