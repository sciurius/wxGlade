"""\
Code generator functions for wxDirPickerCtrl objects
"""

import common
import wcodegen


class LispDirPickerCtrlGenerator(wcodegen.LispWidgetCodeWriter):
    tmpl = '(setf %(name)s (%(klass)s_Create %(parent)s %(id)s -1 -1 -1 -1 %(style)s))\n'


def initialize():
    klass = 'wxDirPickerCtrl'
    common.class_names['EditDirPickerCtrl'] = klass
    common.register('lisp', klass, LispDirPickerCtrlGenerator(klass))
