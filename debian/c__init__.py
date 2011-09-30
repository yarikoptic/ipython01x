#!/usr/bin/python
#emacs: -*- mode: python-mode; py-indent-offset: 4; tab-width: 4; indent-tabs-mode: nil -*- 
#ex: set sts=4 ts=4 sw=4 noet:
"""IPython01X -- ugly hack to load custom-installed IPython module

Its job is to augment sys.path and PYTHONPATH so that having imported
IPython01X, upon 'import IPython' you would be working with a local
copy of IPython (as opposed to possibly system-wide available,
distribution-supported ipython)

This way it provides capability to package and use provided GIT
snapshot of IPython on the systems with system-wide available
older/stable version of IPython

"""
#-----------------\____________________________________/------------------

__author__ = 'Yaroslav Halchenko'
__copyright__ = 'Copyright (c) 2011 Yaroslav Halchenko'
__license__ = 'BSD-3'

import os, sys;

print "Beware: you are importing a development version of IPython -- no whining"

# directory which contains this __init__
_i01path = os.path.dirname(__file__)

# for processes sharing this Python session
_i01path in sys.path or sys.path.insert(1, _i01path);

# for newly spawn processes we need to agument PYTHONPATH
_PYTHONPATH = [_i01path]
if os.getenv('PYTHONPATH', None):
    _PYTHONPATH.append(os.getenv('PYTHONPATH'))
os.putenv('PYTHONPATH', ':'.join(_PYTHONPATH))
