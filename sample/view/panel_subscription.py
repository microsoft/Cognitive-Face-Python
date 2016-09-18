#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: view.py
Description: Subscription Panel for Python SDK sample.
"""

import wx
import wx.lib.agw.hyperlink as HL

import util
from view.base import MyPanel


class SubscriptionPanel(MyPanel):
    """Subscription Panel."""
    def __init__(self, parent):
        super(SubscriptionPanel, self).__init__(parent)

        self.sizer = wx.BoxSizer(wx.VERTICAL)

        label = (
            'To use the service, you need to ensure that you have right '
            'subscription key.\nPlease note that each service (Face, Emotion, '
            'Speech, etc) has its own subscription key.\nIf you do not have '
            'key yet, please use the link to get a key first, then paste the '
            'key into the textbox below.'
        )
        style = wx.ALIGN_LEFT | wx.ST_ELLIPSIZE_END
        self.static_text = wx.StaticText(self, label=label, style=style)
        self.sizer.Add(self.static_text, flag=wx.EXPAND | wx.ALL, border=5)

        label = 'Get Key'
        url = 'https://www.microsoft.com/cognitive-services/en-us/sign-up'
        colour_window = wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW)
        flag = wx.ALIGN_LEFT | wx.ALL
        self.link = HL.HyperLinkCtrl(self, label=label, URL=url)
        self.link.SetBackgroundColour(colour_window)
        self.sizer.Add(self.link, flag=flag, border=5)

        subsizer = wx.BoxSizer()

        flag = wx.ALIGN_CENTER_VERTICAL | wx.ALL
        self.label = wx.StaticText(self, label='Subscription Key : ')
        subsizer.Add(self.label, flag=flag, border=5)

        flag = wx.EXPAND | wx.ALIGN_CENTER_VERTICAL | wx.ALL
        self.text = wx.TextCtrl(self, size=(-1, -1))
        self.text.SetValue(util.SubscriptionKey.get().decode('utf-8'))
        subsizer.Add(self.text, 1, flag=flag, border=5)

        flag = wx.ALIGN_CENTER_VERTICAL | wx.ALL
        self.btn_save = wx.Button(self, label='Save Key')
        subsizer.Add(self.btn_save, flag=flag, border=5)
        self.Bind(wx.EVT_BUTTON, self.OnSaveKey, self.btn_save)

        flag = wx.ALIGN_CENTER_VERTICAL | wx.ALL
        self.btn_del = wx.Button(self, label='Delete Key')
        subsizer.Add(self.btn_del, flag=flag, border=5)
        self.Bind(wx.EVT_BUTTON, self.OnDeleteKey, self.btn_del)

        flag = wx.EXPAND | wx.TOP | wx.BOTTOM
        self.sizer.Add(subsizer, flag=flag, border=5)

        self.SetSizer(self.sizer)

    def OnSaveKey(self, evt):
        """Save the key."""
        util.SubscriptionKey.set(self.text.GetValue().encode('utf-8'))
        text = (
            'Subscription key is saved in your disk.\n'
            'You do not need to paste the key next time.'
        )
        title = 'Subscription Key'
        style = wx.OK | wx.ICON_INFORMATION
        wx.MessageBox(text, title, style)

    def OnDeleteKey(self, evt):
        """Delete the key."""
        self.text.Clear()
        util.SubscriptionKey.delete()
        text = 'Subscription key is deleted from your disk.'
        title = 'Subscription Key'
        style = wx.OK | wx.ICON_INFORMATION
        wx.MessageBox(text, title, style)
