*************************************************
:mod:`cam_iface` -- Python wrapper of libcamiface
*************************************************

.. module:: cam_iface
  :synopsis: Python wrapper of libcamiface
.. index::
  module: cam_iface
  single: cam_iface

This is a ctypes wrapper of :ref:`libcamiface`. It requires
libcamiface 0.5.9 or higher.

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

  # Also the example in ../README.rst -- so keep in sync
  import pkg_resources
  import motmot.cam_iface.cam_iface_ctypes as cam_iface
  import numpy as np

  mode_num = 0
  device_num = 0
  num_buffers = 32

  cam = cam_iface.Camera(device_num,num_buffers,mode_num)
  cam.start_camera()
  frame = np.asarray(cam.grab_next_frame_blocking())
  print 'grabbed frame with shape %s'%(frame.shape,)

.. Remember to keep the above example in sync with demo/very_simple.py
