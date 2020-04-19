# -*- coding: UTF-8 -*-
#
# generated by wxGlade
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
from Gnumed.wxpython.gmListWidgets import cReportListCtrl
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetTitle("frame")
        
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        
        self.button_2 = wx.Button(self, wx.ID_ANY, "button_2")
        sizer_1.Add(self.button_2, 0, 0, 0)
        
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        
        self.Layout()
        # end wxGlade

# end of class MyFrame

class MyDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyDialog.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetTitle("dialog")
        
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.button_1 = wx.Button(self, wx.ID_ANY, "button_1")
        sizer_2.Add(self.button_1, 0, 0, 0)
        
        self.SetSizer(sizer_2)
        sizer_2.Fit(self)
        
        self.Layout()
        # end wxGlade

# end of class MyDialog

class wxgMeasurementsByDayPnl(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: wxgMeasurementsByDayPnl.__init__
        kwds["style"] = kwds.get("style", 0) | wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        
        __szr_main = wx.BoxSizer(wx.HORIZONTAL)
        
        self._LCTRL_days = cReportListCtrl(self, wx.ID_ANY, style=wx.BORDER_NONE | wx.LC_REPORT)
        self._LCTRL_days.SetMinSize((100, 100))
        __szr_main.Add(self._LCTRL_days, 1, wx.EXPAND | wx.RIGHT, 5)
        
        self._LCTRL_results = cReportListCtrl(self, wx.ID_ANY, style=wx.BORDER_NONE | wx.LC_REPORT)
        self._LCTRL_results.SetMinSize((100, 100))
        __szr_main.Add(self._LCTRL_results, 1, wx.EXPAND | wx.RIGHT, 5)
        
        __szr_details = wx.BoxSizer(wx.VERTICAL)
        __szr_main.Add(__szr_details, 1, wx.EXPAND, 0)
        
        self._TCTRL_measurements = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_AUTO_URL | wx.TE_MULTILINE | wx.TE_READONLY)
        self._TCTRL_measurements.SetMinSize((255, 102))
        self._TCTRL_measurements.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_BACKGROUND))
        __szr_details.Add(self._TCTRL_measurements, 1, wx.EXPAND, 0)
        
        __szr_show_docs = wx.BoxSizer(wx.HORIZONTAL)
        __szr_details.Add(__szr_show_docs, 0, wx.EXPAND, 0)
        
        self._LBL_no_of_docs = wx.StaticText(self, wx.ID_ANY, "")
        self._LBL_no_of_docs.SetMinSize((100, 100))
        __szr_show_docs.Add(self._LBL_no_of_docs, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 3)
        
        self._BTN_show_docs = wx.Button(self, wx.ID_ANY, "Show X documents")
        self._BTN_show_docs.SetMinSize((100, 100))
        self._BTN_show_docs.SetToolTip(wx.ToolTip("Show lab related documents for the episode of the selected measurement."))
        self._BTN_show_docs.Enable(False)
        __szr_show_docs.Add(self._BTN_show_docs, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        
        __szr_show_docs.Add((20, 20), 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
        
        self.SetSizer(__szr_main)
        __szr_main.Fit(self)
        
        self.Layout()

        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self._on_day_selected, self._LCTRL_days)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self._on_result_selected, self._LCTRL_results)
        self.Bind(wx.EVT_BUTTON, self._on_show_docs_button_pressed, self._BTN_show_docs)
        # end wxGlade

    def _on_day_selected(self, event):  # wxGlade: wxgMeasurementsByDayPnl.<event_handler>
        print("Event handler '_on_day_selected' not implemented!")
        event.Skip()

    def _on_result_selected(self, event):  # wxGlade: wxgMeasurementsByDayPnl.<event_handler>
        print("Event handler '_on_result_selected' not implemented!")
        event.Skip()

    def _on_show_docs_button_pressed(self, event):  # wxGlade: wxgMeasurementsByDayPnl.<event_handler>
        print("Event handler '_on_show_docs_button_pressed' not implemented!")
        event.Skip()

# end of class wxgMeasurementsByDayPnl

class wxgMeasurementsByDayPnl(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: wxgMeasurementsByDayPnl.__init__
        kwds["style"] = kwds.get("style", 0) | wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        
        __szr_main = wx.BoxSizer(wx.HORIZONTAL)
        
        self._LCTRL_days = cReportListCtrl(self, wx.ID_ANY, style=wx.BORDER_NONE | wx.LC_REPORT)
        self._LCTRL_days.SetMinSize((100, 100))
        __szr_main.Add(self._LCTRL_days, 1, wx.EXPAND | wx.RIGHT, 5)
        
        self._LCTRL_days_copy = cReportListCtrl(self, wx.ID_ANY, style=wx.BORDER_NONE | wx.LC_REPORT)
        self._LCTRL_days_copy.SetMinSize((100, 100))
        __szr_main.Add(self._LCTRL_days_copy, 1, wx.EXPAND | wx.RIGHT, 5)
        
        self.SetSizer(__szr_main)
        __szr_main.Fit(self)
        
        self.Layout()

        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self._on_day_selected, self._LCTRL_days)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self._on_day_selected, self._LCTRL_days_copy)
        # end wxGlade

    def _on_day_selected(self, event):  # wxGlade: wxgMeasurementsByDayPnl.<event_handler>
        print("Event handler '_on_day_selected' not implemented!")
        event.Skip()

# end of class wxgMeasurementsByDayPnl

class wxgMeasurementsByDayPnl(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: wxgMeasurementsByDayPnl.__init__
        kwds["style"] = kwds.get("style", 0) | wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        
        __szr_main = wx.BoxSizer(wx.HORIZONTAL)
        
        self.text_ctrl_1 = wx.TextCtrl(self, wx.ID_ANY, "")
        __szr_main.Add(self.text_ctrl_1, 0, 0, 0)
        
        self.text_ctrl_2 = wx.TextCtrl(self, wx.ID_ANY, "")
        __szr_main.Add(self.text_ctrl_2, 0, 0, 0)
        
        self.SetSizer(__szr_main)
        __szr_main.Fit(self)
        
        self.Layout()
        # end wxGlade

# end of class wxgMeasurementsByDayPnl

class MyFrame1(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame1.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetTitle("frame_1")
        
        __szr_main = wx.BoxSizer(wx.HORIZONTAL)
        
        self._LCTRL_days = cReportListCtrl(self, wx.ID_ANY, style=wx.BORDER_NONE | wx.LC_REPORT)
        self._LCTRL_days.SetMinSize((100, 100))
        __szr_main.Add(self._LCTRL_days, 1, wx.EXPAND | wx.RIGHT, 5)
        
        self._LCTRL_results = cReportListCtrl(self, wx.ID_ANY, style=wx.BORDER_NONE | wx.LC_REPORT)
        self._LCTRL_results.SetMinSize((100, 100))
        __szr_main.Add(self._LCTRL_results, 1, wx.EXPAND | wx.RIGHT, 5)
        
        __szr_details = wx.BoxSizer(wx.VERTICAL)
        __szr_main.Add(__szr_details, 1, wx.EXPAND, 0)
        
        self._TCTRL_measurements = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_AUTO_URL | wx.TE_MULTILINE | wx.TE_READONLY)
        self._TCTRL_measurements.SetMinSize((255, 102))
        self._TCTRL_measurements.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_BACKGROUND))
        __szr_details.Add(self._TCTRL_measurements, 1, wx.EXPAND, 0)
        
        __szr_show_docs = wx.BoxSizer(wx.HORIZONTAL)
        __szr_details.Add(__szr_show_docs, 0, wx.EXPAND, 0)
        
        self._LBL_no_of_docs = wx.StaticText(self, wx.ID_ANY, "")
        self._LBL_no_of_docs.SetMinSize((100, 100))
        __szr_show_docs.Add(self._LBL_no_of_docs, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 3)
        
        self._BTN_show_docs = wx.Button(self, wx.ID_ANY, "Show X documents")
        self._BTN_show_docs.SetMinSize((100, 100))
        self._BTN_show_docs.SetToolTip(wx.ToolTip("Show lab related documents for the episode of the selected measurement."))
        self._BTN_show_docs.Enable(False)
        __szr_show_docs.Add(self._BTN_show_docs, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        
        __szr_show_docs.Add((20, 20), 1, wx.EXPAND, 0)
        
        self.SetSizer(__szr_main)
        __szr_main.Fit(self)
        
        self.Layout()

        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self._on_day_selected, self._LCTRL_days)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self._on_result_selected, self._LCTRL_results)
        self.Bind(wx.EVT_BUTTON, self._on_show_docs_button_pressed, self._BTN_show_docs)
        # end wxGlade

    def _on_day_selected(self, event):  # wxGlade: MyFrame1.<event_handler>
        print("Event handler '_on_day_selected' not implemented!")
        event.Skip()

    def _on_result_selected(self, event):  # wxGlade: MyFrame1.<event_handler>
        print("Event handler '_on_result_selected' not implemented!")
        event.Skip()

    def _on_show_docs_button_pressed(self, event):  # wxGlade: MyFrame1.<event_handler>
        print("Event handler '_on_show_docs_button_pressed' not implemented!")
        event.Skip()

# end of class MyFrame1
