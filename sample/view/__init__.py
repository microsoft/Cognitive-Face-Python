#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: __init__.py
Description: View components for Python SDK sample.
"""

import wx
import wx.lib.agw.labelbook as LB

from wx.lib.agw.fmresources import INB_FIT_LABELTEXT
from wx.lib.agw.fmresources import INB_LEFT
from wx.lib.agw.fmresources import INB_NO_RESIZE

from view.panel_detection import DetectionPanel
from view.panel_subscription import SubscriptionPanel
from view.panel_find_similar import FindSimilarPanel
from view.panel_group import GroupPanel
from view.panel_identification import IdentificationPanel
from view.panel_verification import VerificationPanel

TITLE = u"Microsoft Cognitive Services Face Samples"


class MyLabelBook(LB.LabelBook):
    """LabelBook part in Main Frame."""
    def __init__(self, parent):
        agw_style = INB_LEFT | INB_FIT_LABELTEXT | INB_NO_RESIZE
        super(MyLabelBook, self).__init__(parent, agwStyle=agw_style)

        subscription_panel = SubscriptionPanel(self)
        subscription_text = u"Subscription Key Management"
        self.AddPage(subscription_panel, subscription_text, True)

        self.AddPage(wx.Panel(self), u"Select a scenario:")
        self.EnableTab(1, False)

        self.AddPage(DetectionPanel(self), u" - Face Detection")
        self.AddPage(FindSimilarPanel(self), u" - Face Find Similar")
        self.AddPage(GroupPanel(self), u" - Face Grouping")
        self.AddPage(IdentificationPanel(self), u" - Face Identification")
        self.AddPage(VerificationPanel(self), u" - Face Verification")


class MyTitle(wx.Panel):
    """Title part in Main Frame."""
    def __init__(self, parent):
        super(MyTitle, self).__init__(parent)
        self.SetBackgroundColour('#00b294')
        self.SetMinSize((-1, 80))

        sizer = wx.BoxSizer()
        sizer.AddStretchSpacer()

        family = wx.FONTFAMILY_DEFAULT
        style = wx.FONTSTYLE_NORMAL
        weight = wx.FONTWEIGHT_NORMAL
        font = wx.Font(20, family, style, weight)
        self.text = wx.StaticText(self, label=TITLE, style=wx.ALIGN_CENTER)
        self.text.SetFont(font)
        sizer.Add(self.text, flag=wx.ALIGN_CENTER_VERTICAL)

        sizer.AddStretchSpacer()
        self.SetSizer(sizer)


class MyFrame(wx.Frame):
    """Main Frame."""
    def __init__(self, parent):
        super(MyFrame, self).__init__(parent, title=TITLE, size=(1280, 768))

        icon_path = 'Assets/Microsoft-logo_rgb_c-gray.png'
        self.SetIcon(wx.Icon(icon_path))

        sizer = wx.BoxSizer(wx.VERTICAL)

        self.title = MyTitle(self)
        sizer.Add(self.title, flag=wx.EXPAND)

        self.book = MyLabelBook(self)
        sizer.Add(self.book, 1, flag=wx.EXPAND)

        status_text = (
            'Microsoft will receive the images you upload and may use them to '
            'improve Face API and related services. By submitting an image, '
            'you confirm you have consent from everyone in it.'
        )
        self.status = wx.StatusBar(self)
        self.status.SetStatusText(status_text)
        sizer.Add(self.status, flag=wx.EXPAND)

        self.SetSizer(sizer)
        self.Layout()


class MyApp(wx.App):
    """The whole app."""
    def OnInit(self):
        """Show main frame."""
        frame = MyFrame(None)
        frame.Show()
        return True
