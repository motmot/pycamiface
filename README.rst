*************************************************
:mod:`cam_iface` -- Python wrapper of libcamiface
*************************************************

.. module:: cam_iface
  :synopsis: Python wrapper of libcamiface
.. index::
  module: cam_iface
  single: cam_iface

This is a ctypes wrapper of :ref:`libcamiface`.

Installation
============

The usual::

  python setup.py install

License
=======

pycamiface is licensed under the BSD license. See the LICENSE.txt file
for the full description.

Example usage
=============

A very simple example of usage is in the file
``demo/very_simple.py``. This file contains the following::

  import pkg_resources
  import motmot.cam_iface.choose as cam_iface_choose
  import numpy as np

  # Choose the mega ctypes backend
  cam_iface = cam_iface_choose.import_backend( 'mega', 'ctypes' )

  mode_num = 0
  device_num = 0
  num_buffers = 32

  cam = cam_iface.Camera(device_num,num_buffers,mode_num)
  cam.start_camera()
  frame = np.asarray(cam.grab_next_frame_blocking())
  print 'grabbed frame with shape %s'%(frame.shape,)

.. Remember to keep the above example in sync with demo/very_simple.py
