"""\
Code generator functions for spacers

@copyright: 2002-2007 Alberto Griggio
@copyright: 2014 Carsten Grohmann
@license: MIT (see license.txt) - THIS PROGRAM COMES WITH NO WARRANTY
"""

import common
import wcodegen


class PythonSpacerGenerator(wcodegen.PythonWidgetCodeWriter):

    # spacers are generally handled by a hack:
    # The the implementations of add_sizeritem() contains more details.
    # The code generation code is already implemented in base class.
    pass

# end of class PythonSpacerGenerator


class CppSpacerGenerator(wcodegen.CppWidgetCodeWriter):

    # spacers are generally handled by a hack:
    # The the implementations of add_sizeritem() contains more details.
    # The code generation code is already implemented in base class.
    pass

# end of class CppSpacerGenerator


def initialize():
    klass = 'spacer'
    common.class_names['EditSpacer'] = klass
    common.register('python', klass, PythonSpacerGenerator(klass))
    common.register('C++', klass, CppSpacerGenerator(klass))
