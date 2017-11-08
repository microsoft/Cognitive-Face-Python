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
            'To use the service, make sure you have a valid '
            'subscription key.\nNote that each service (Face, Emotion, '
            'Speech, etc.) has its own subscription keys.\nAnd each '
            'subscription key belongs to one specific endpoint.\nYou can use '
            'the link below to get a key.\nWhen ready, paste your key '
            'into the textbox below.'
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

        subgridsizer = wx.GridSizer(rows=2, cols=2, hgap=5, vgap=5)

        flag = wx.ALIGN_CENTER_VERTICAL | wx.ALL | wx.FIXED_MINSIZE
        label = 'Subscription Key : '
        self.subscription_key_label = wx.StaticText(self, label=label)
        subgridsizer.Add(self.subscription_key_label, flag=flag, border=5)

        flag = wx.EXPAND | wx.ALIGN_CENTER_VERTICAL | wx.ALL
        subscription_key = util.SubscriptionKey.get().decode('utf-8')
        self.subscription_key_text = wx.TextCtrl(self, size=(-1, -1))
        self.subscription_key_text.SetValue(subscription_key)
        subgridsizer.Add(self.subscription_key_text, 1, flag=flag, border=5)

        flag = wx.ALIGN_CENTER_VERTICAL | wx.ALL | wx.FIXED_MINSIZE
        label = 'Endpoint : '
        self.endpoint_label = wx.StaticText(self, label=label)
        subgridsizer.Add(self.endpoint_label, flag=flag, border=5)

        flag = wx.EXPAND | wx.ALIGN_CENTER_VERTICAL | wx.ALL
        endpoint = util.Endpoint.get().decode('utf-8')
        self.endpoint_text = wx.TextCtrl(self, size=(-1, -1))
        self.endpoint_text.SetValue(endpoint)
        subgridsizer.Add(self.endpoint_text, 1, flag=flag, border=5)

        flag = wx.EXPAND | wx.TOP | wx.BOTTOM
        self.sizer.Add(subgridsizer, flag=flag, border=5)

        subsizer = wx.BoxSizer()

        flag = wx.ALIGN_CENTER_VERTICAL | wx.ALL | wx.FIXED_MINSIZE
        self.btn_save = wx.Button(self, label='Save')
        subsizer.Add(self.btn_save, flag=flag, border=5)
        self.Bind(wx.EVT_BUTTON, self.OnSave, self.btn_save)

        flag = wx.ALIGN_CENTER_VERTICAL | wx.ALL
        self.btn_del = wx.Button(self, label='Delete')
        subsizer.Add(self.btn_del, flag=flag, border=5)
        self.Bind(wx.EVT_BUTTON, self.OnDelete, self.btn_del)

        flag = wx.EXPAND | wx.TOP | wx.BOTTOM
        self.sizer.Add(subsizer, flag=flag, border=5)

        self.SetSizer(self.sizer)

    def OnSave(self, evt):
        """Save the key and endpoint."""
        util.SubscriptionKey.set(
            self.subscription_key_text.GetValue().encode('utf-8'))
        util.Endpoint.set(
            self.endpoint_text.GetValue().encode('utf-8'))
        text = (
            'Settings successfully saved on your disk.\n'
            'You do not need to paste the key next time.'
        )
        title = 'Settings'
        style = wx.OK | wx.ICON_INFORMATION
        wx.MessageBox(text, title, style)

    def OnDelete(self, evt):
        """Delete the key and endpoint."""
        util.SubscriptionKey.delete()
        util.Endpoint.delete()
        self.subscription_key_text.Clear()
        self.endpoint_text.SetValue(util.Endpoint.get())
        text = 'Settings successfully deleted from your disk.'
        title = 'Settings'
        style = wx.OK | wx.ICON_INFORMATION
        wx.MessageBox(text, title, style)
