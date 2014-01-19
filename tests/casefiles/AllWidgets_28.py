#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade "faked test version"
#

import wx
import wx.calendar

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class All_Widgets_Frame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: All_Widgets_Frame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.notebook_1 = wx.Notebook(self, wx.ID_ANY, style=wx.NB_BOTTOM)
        self.notebook_1_wxBitmapButton = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.bitmap_button_1 = wx.BitmapButton(self.notebook_1_wxBitmapButton, wx.ID_ANY, wx.Bitmap("icon.xpm", wx.BITMAP_TYPE_ANY))
        self.notebook_1_wxCalendarCtrl = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.calendar_ctrl_1 = wx.calendar.CalendarCtrl(self.notebook_1_wxCalendarCtrl, wx.ID_ANY)
        self.notebook_1_wxChoice = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.choice_empty = wx.Choice(self.notebook_1_wxChoice, wx.ID_ANY, choices=[])
        self.choice_filled = wx.Choice(self.notebook_1_wxChoice, wx.ID_ANY, choices=[_("Item 1"), _("Item 2 (pre-selected)")])
        self.notebook_1_wxComboBox = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.combo_box_empty = wx.ComboBox(self.notebook_1_wxComboBox, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        self.combo_box_filled = wx.ComboBox(self.notebook_1_wxComboBox, wx.ID_ANY, choices=[_("Item 1 (pre-selected)"), _("Item 2")], style=wx.CB_DROPDOWN)
        self.notebook_1_wxListBox = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.list_box_empty = wx.ListBox(self.notebook_1_wxListBox, wx.ID_ANY, choices=[])
        self.list_box_filled = wx.ListBox(self.notebook_1_wxListBox, wx.ID_ANY, choices=[_("Item 1"), _("Item 2 (pre-selected)")])
        self.notebook_1_wxListCtrl = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.list_ctrl_1 = wx.ListCtrl(self.notebook_1_wxListCtrl, wx.ID_ANY, style=wx.LC_REPORT | wx.SUNKEN_BORDER)
        self.notebook_1_wxRadioBox = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.radio_box_empty1 = wx.RadioBox(self.notebook_1_wxRadioBox, wx.ID_ANY, _("radio_box_empty1"), choices=[], majorDimension=0, style=wx.RA_SPECIFY_ROWS)
        self.radio_box_filled1 = wx.RadioBox(self.notebook_1_wxRadioBox, wx.ID_ANY, _("radio_box_filled1"), choices=[_("choice 1"), _("choice 2 (pre-selected)"), _("choice 3")], majorDimension=0, style=wx.RA_SPECIFY_ROWS)
        self.radio_box_empty2 = wx.RadioBox(self.notebook_1_wxRadioBox, wx.ID_ANY, _("radio_box_empty2"), choices=[], majorDimension=0, style=wx.RA_SPECIFY_COLS)
        self.radio_box_filled2 = wx.RadioBox(self.notebook_1_wxRadioBox, wx.ID_ANY, _("radio_box_filled2"), choices=[_("choice 1"), _("choice 2 (pre-selected)")], majorDimension=0, style=wx.RA_SPECIFY_COLS)
        self.notebook_1_wxRadioButton = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.radio_btn_1 = wx.RadioButton(self.notebook_1_wxRadioButton, wx.ID_ANY, _("Alice"), style=wx.RB_GROUP)
        self.text_ctrl_1 = wx.TextCtrl(self.notebook_1_wxRadioButton, wx.ID_ANY, "")
        self.radio_btn_2 = wx.RadioButton(self.notebook_1_wxRadioButton, wx.ID_ANY, _("Bob"))
        self.text_ctrl_2 = wx.TextCtrl(self.notebook_1_wxRadioButton, wx.ID_ANY, "")
        self.radio_btn_3 = wx.RadioButton(self.notebook_1_wxRadioButton, wx.ID_ANY, _("Malroy"))
        self.text_ctrl_3 = wx.TextCtrl(self.notebook_1_wxRadioButton, wx.ID_ANY, "")
        self.sizer_8_staticbox = wx.StaticBox(self.notebook_1_wxRadioButton, wx.ID_ANY, _("My RadioButton Group"))
        self.notebook_1_wxSlider = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.gauge_1 = wx.Gauge(self.notebook_1_wxSlider, wx.ID_ANY, 20)
        self.notebook_1_wxSpinButton = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.spin_button_1 = wx.SpinButton(self.notebook_1_wxSpinButton, wx.ID_ANY )
        self.notebook_1_wxSpinCtrl = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.spin_ctrl_1 = wx.SpinCtrl(self.notebook_1_wxSpinCtrl, wx.ID_ANY, "4", min=0, max=100, style=wx.SP_ARROW_KEYS | wx.TE_AUTO_URL)
        self.notebook_1_wxSplitterWindow = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1_wxStaticBitmap = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.bitmap_code_nullbitmap = wx.StaticBitmap(self.notebook_1_wxStaticBitmap, wx.ID_ANY, (wx.NullBitmap))
        self.bitmap_file = wx.StaticBitmap(self.notebook_1_wxStaticBitmap, wx.ID_ANY, wx.Bitmap("icon.xpm", wx.BITMAP_TYPE_ANY))
        self.bitmap_nofile = wx.StaticBitmap(self.notebook_1_wxStaticBitmap, wx.ID_ANY, wx.Bitmap("non-existing.bmp", wx.BITMAP_TYPE_ANY))
        self.notebook_1_wxStaticLine = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.static_line_2 = wx.StaticLine(self.notebook_1_wxStaticLine, wx.ID_ANY, style=wx.LI_VERTICAL)
        self.static_line_3 = wx.StaticLine(self.notebook_1_wxStaticLine, wx.ID_ANY, style=wx.LI_VERTICAL)
        self.static_line_4 = wx.StaticLine(self.notebook_1_wxStaticLine, wx.ID_ANY)
        self.static_line_5 = wx.StaticLine(self.notebook_1_wxStaticLine, wx.ID_ANY)
        self.notebook_1_Spacer = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.label_3 = wx.StaticText(self.notebook_1_Spacer, wx.ID_ANY, _("Two labels with a"))
        self.label_2 = wx.StaticText(self.notebook_1_Spacer, wx.ID_ANY, _("spacer between"))
        self.static_line_1 = wx.StaticLine(self, wx.ID_ANY)
        self.button_5 = wx.Button(self, wx.ID_CLOSE, "")
        self.button_1 = wx.Button(self, wx.ID_OK, "", style=wx.BU_TOP)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.startConverting, self.button_1)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: All_Widgets_Frame.__set_properties
        self.SetTitle(_("All Widgets"))
        self.bitmap_button_1.SetSize(self.bitmap_button_1.GetBestSize())
        self.bitmap_button_1.SetDefault()
        self.choice_filled.SetSelection(1)
        self.combo_box_filled.SetSelection(0)
        self.list_box_filled.SetSelection(1)
        self.radio_box_filled1.SetSelection(1)
        self.radio_box_filled2.SetSelection(1)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: All_Widgets_Frame.__do_layout
        sizer_1 = wx.FlexGridSizer(3, 1, 0, 0)
        sizer_2 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_3 = wx.FlexGridSizer(1, 3, 0, 0)
        sizer_9 = wx.BoxSizer(wx.VERTICAL)
        sizer_10 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_11 = wx.BoxSizer(wx.VERTICAL)
        sizer_14 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_16 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_15 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_8_staticbox.Lower()
        sizer_8 = wx.StaticBoxSizer(self.sizer_8_staticbox, wx.HORIZONTAL)
        grid_sizer_2 = wx.FlexGridSizer(3, 2, 0, 0)
        grid_sizer_1 = wx.GridSizer(2, 2, 0, 0)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_12 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_13 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_13.Add(self.bitmap_button_1, 1, wx.ALL | wx.EXPAND, 5)
        self.notebook_1_wxBitmapButton.SetSizer(sizer_13)
        sizer_12.Add(self.calendar_ctrl_1, 1, wx.ALL | wx.EXPAND, 5)
        self.notebook_1_wxCalendarCtrl.SetSizer(sizer_12)
        sizer_5.Add(self.choice_empty, 1, wx.ALL, 5)
        sizer_5.Add(self.choice_filled, 1, wx.ALL, 5)
        self.notebook_1_wxChoice.SetSizer(sizer_5)
        sizer_7.Add(self.combo_box_empty, 1, wx.ALL, 5)
        sizer_7.Add(self.combo_box_filled, 1, wx.ALL, 5)
        sizer_6.Add(sizer_7, 1, wx.EXPAND, 0)
        self.notebook_1_wxComboBox.SetSizer(sizer_6)
        sizer_4.Add(self.list_box_empty, 1, wx.ALL | wx.EXPAND, 5)
        sizer_4.Add(self.list_box_filled, 1, wx.ALL | wx.EXPAND, 5)
        self.notebook_1_wxListBox.SetSizer(sizer_4)
        sizer_3.Add(self.list_ctrl_1, 1, wx.ALL | wx.EXPAND, 5)
        self.notebook_1_wxListCtrl.SetSizer(sizer_3)
        grid_sizer_1.Add(self.radio_box_empty1, 1, wx.ALL | wx.EXPAND, 5)
        grid_sizer_1.Add(self.radio_box_filled1, 1, wx.ALL | wx.EXPAND, 5)
        grid_sizer_1.Add(self.radio_box_empty2, 1, wx.ALL | wx.EXPAND, 5)
        grid_sizer_1.Add(self.radio_box_filled2, 1, wx.ALL | wx.EXPAND, 5)
        self.notebook_1_wxRadioBox.SetSizer(grid_sizer_1)
        grid_sizer_2.Add(self.radio_btn_1, 1, wx.ALL | wx.EXPAND, 5)
        grid_sizer_2.Add(self.text_ctrl_1, 1, wx.ALL | wx.EXPAND, 5)
        grid_sizer_2.Add(self.radio_btn_2, 1, wx.ALL | wx.EXPAND, 5)
        grid_sizer_2.Add(self.text_ctrl_2, 1, wx.ALL | wx.EXPAND, 5)
        grid_sizer_2.Add(self.radio_btn_3, 1, wx.ALL | wx.EXPAND, 5)
        grid_sizer_2.Add(self.text_ctrl_3, 1, wx.ALL | wx.EXPAND, 5)
        sizer_8.Add(grid_sizer_2, 1, wx.EXPAND, 0)
        self.notebook_1_wxRadioButton.SetSizer(sizer_8)
        sizer_15.Add(self.gauge_1, 1, wx.ALL, 5)
        self.notebook_1_wxSlider.SetSizer(sizer_15)
        sizer_16.Add(self.spin_button_1, 1, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)
        self.notebook_1_wxSpinButton.SetSizer(sizer_16)
        sizer_14.Add(self.spin_ctrl_1, 1, wx.ALL, 5)
        self.notebook_1_wxSpinCtrl.SetSizer(sizer_14)
        sizer_11.Add(self.bitmap_code_nullbitmap, 1, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_11.Add(self.bitmap_file, 1, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_11.Add(self.bitmap_nofile, 1, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)
        self.notebook_1_wxStaticBitmap.SetSizer(sizer_11)
        sizer_10.Add(self.static_line_2, 1, wx.ALL | wx.EXPAND, 5)
        sizer_10.Add(self.static_line_3, 1, wx.ALL | wx.EXPAND, 5)
        sizer_9.Add(sizer_10, 1, wx.EXPAND, 0)
        sizer_9.Add(self.static_line_4, 1, wx.ALL | wx.EXPAND, 5)
        sizer_9.Add(self.static_line_5, 1, wx.ALL | wx.EXPAND, 5)
        self.notebook_1_wxStaticLine.SetSizer(sizer_9)
        grid_sizer_3.Add(self.label_3, 1, wx.ALL | wx.EXPAND, 5)
        grid_sizer_3.Add((60, 20), 1, wx.ALL | wx.EXPAND, 5)
        grid_sizer_3.Add(self.label_2, 1, wx.ALL | wx.EXPAND, 5)
        self.notebook_1_Spacer.SetSizer(grid_sizer_3)
        self.notebook_1.AddPage(self.notebook_1_wxBitmapButton, _("wxBitmapButton"))
        self.notebook_1.AddPage(self.notebook_1_wxCalendarCtrl, _("wxCalendarCtrl"))
        self.notebook_1.AddPage(self.notebook_1_wxChoice, _("wxChoice"))
        self.notebook_1.AddPage(self.notebook_1_wxComboBox, _("wxComboBox"))
        self.notebook_1.AddPage(self.notebook_1_wxListBox, _("wxListBox"))
        self.notebook_1.AddPage(self.notebook_1_wxListCtrl, _("wxListCtrl"))
        self.notebook_1.AddPage(self.notebook_1_wxRadioBox, _("wxRadioBox"))
        self.notebook_1.AddPage(self.notebook_1_wxRadioButton, _("wxRadioButton"))
        self.notebook_1.AddPage(self.notebook_1_wxSlider, _("wxSlider"))
        self.notebook_1.AddPage(self.notebook_1_wxSpinButton, _("wxSpinButton"))
        self.notebook_1.AddPage(self.notebook_1_wxSpinCtrl, _("wxSpinCtrl"))
        self.notebook_1.AddPage(self.notebook_1_wxSplitterWindow, _("wxSplitterWindow"))
        self.notebook_1.AddPage(self.notebook_1_wxStaticBitmap, _("wxStaticBitmap"))
        self.notebook_1.AddPage(self.notebook_1_wxStaticLine, _("wxStaticLine"))
        self.notebook_1.AddPage(self.notebook_1_Spacer, _("wxStaticText (with Spacer)"))
        sizer_1.Add(self.notebook_1, 1, wx.EXPAND, 0)
        sizer_1.Add(self.static_line_1, 0, wx.ALL | wx.EXPAND, 5)
        sizer_2.Add(self.button_5, 0, wx.ALL | wx.ALIGN_RIGHT, 5)
        sizer_2.Add(self.button_1, 0, wx.ALL | wx.ALIGN_RIGHT, 5)
        sizer_1.Add(sizer_2, 0, wx.ALIGN_RIGHT, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        sizer_1.SetSizeHints(self)
        sizer_1.AddGrowableRow(0)
        sizer_1.AddGrowableCol(0)
        self.Layout()
        self.Centre()
        # end wxGlade

    def startConverting(self, event):  # wxGlade: All_Widgets_Frame.<event_handler>
        print "Event handler 'startConverting' not implemented!"
        event.Skip()

# end of class All_Widgets_Frame
if __name__ == "__main__":
    gettext.install("ComplexExampleApp") # replace with the appropriate catalog name

    ComplexExampleApp = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    All_Widgets = All_Widgets_Frame(None, wx.ID_ANY, "")
    ComplexExampleApp.SetTopWindow(All_Widgets)
    All_Widgets.Show()
    ComplexExampleApp.MainLoop()
