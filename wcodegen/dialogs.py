"""\
Dialogs to ask users during widget initialisation triggered by an graphical
user interaction.

@copyright: 2014-2016 Carsten Grohmann
@copyright: 2019-2020 Dietmar Schwertberger
@license: MIT (see LICENSE.txt) - THIS PROGRAM COMES WITH NO WARRANTY
"""

import wx
import compat

class WidgetStyleSelectionDialog(wx.Dialog):
    "User dialog to select a style during widget creation"
    def __init__(self, dlg_title, box_label, choices, options=None, defaults=None):
        """Initialise the dialog and draw the content

        dlg_title: Dialog title
        box_label: Label of the draw around the listed choices
        choices: Choices to select one (string list)
        options: see uses of the dialog"""
        pos = wx.GetMousePosition()
        wx.Dialog.__init__(self, None, -1, dlg_title, pos)

        szr = wx.BoxSizer(wx.VERTICAL)

        self.box = wx.RadioBox( self, wx.ID_ANY, box_label, wx.DefaultPosition, wx.DefaultSize,choices.split('|'),
                                1, style=wx.RA_SPECIFY_COLS )
        self.box.SetSelection(0)
        self.Bind(wx.EVT_RADIOBOX, self.on_choice)
        szr.Add(self.box, 5, wx.ALL | wx.EXPAND, 10)

        if options:
            self._check_option_dependencies(options)
            self.option_controls = []
            self.option_values = []
            for o, option in enumerate(self.options):
                # calculate border flags
                #flags = wx.LEFT | wx.RIGHT
                #if not self.dependencies[o]:   flags |= wx.TOP
                #if not self.dependencies[o+1]: flags |= wx.BOTTOM
                flags = wx.ALL
                # create and add the option controls
                if option[0]=="Checkbox":
                    ctrl = wx.CheckBox(self, -1, option[1])
                    value = defaults and defaults[o]
                    ctrl.SetValue(value)
                    szr.Add(ctrl, 0, flags, 8)
                    ctrl.Bind(wx.EVT_CHECKBOX, self.callback)
                elif option[0]=="Spin":
                    label, range_ = option[1:]
                    hsizer = wx.BoxSizer(wx.HORIZONTAL)
                    hsizer.Add(wx.StaticText(self, -1, label), 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 4)
                    mi_, ma_ = range_
                    value = defaults and defaults[o] or 1
                    ctrl = wx.SpinCtrl(self, -1, str(value), min=mi_, max=ma_, initial=value)
                    hsizer.Add(ctrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 4)
                    self.dependencies[o]
                    szr.Add(hsizer, 0, flags|wx.EXPAND, 4)
                    ctrl.Bind(wx.EVT_SPINCTRL, self.callback)
                self.option_controls.append(ctrl)
                self.option_values.append( value )
            self.active = [True]*len(self.options)
            self._activate(1)

            line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
            szr.Add(line, 0, wx.EXPAND|wx.TOP|wx.LEFT, 5)

        # buttons
        btnbox = wx.StdDialogButtonSizer()
        btnOK = wx.Button(self, wx.ID_OK)
        btnOK.SetDefault()
        btnCANCEL = wx.Button(self, wx.ID_CANCEL)
        btnbox.AddButton(btnOK)
        btnbox.AddButton(btnCANCEL)
        btnbox.Realize()
        szr.Add(btnbox, 0, wx.ALL|wx.ALIGN_CENTER, 8)

        self.SetAutoLayout(True)
        self.SetSizer(szr)
        szr.Fit(self)

    def on_choice(self, event):
        # this can be overridden
        event.Skip()

    def _check_option_dependencies(self, options):
        # if an option string starts with ">", it depends on the previous option
        self.dependencies = [False]*len(options)
        self.options = []
        for o, option in enumerate(options):
            if isinstance(option, compat.basestring):
                # string -> checkbox
                if option.startswith(">"):
                    self.dependencies[o] = True
                    option = option[1:]
                self.options.append( ("Checkbox", option) )
            elif len(option)==2:
                # (string, range) -> spin control
                label = option[0]
                if label.startswith(">"):
                    self.dependencies[o] = True
                    label = label[1:]
                self.options.append( ("Spin", label, option[1]) )
        self.dependencies.append(None)  # dummy

    def _activate(self, i):
        # de-/activate controls based on the preceding options
        for i in range(i, len(self.options)):
            if self.dependencies[i] and not self.active[i-1] or not self.option_values[i-1]:
                activate = False
            else:
                activate = True
            if activate!=self.active[i]:
                self.option_controls[i].Enable(activate)
                self.active[i] = activate

    def callback(self, event):
        # update values and enable / disable dependent options
        ctrl = event.GetEventObject()
        i = self.option_controls.index(ctrl)
        self.option_values[i] = ctrl.GetValue()
        self._activate(i+1)

    def get_selection(self):
        "Return the selected choice."
        return self.box.GetStringSelection()

    def get_options(self):
        return self.option_values
