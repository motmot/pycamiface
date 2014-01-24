# Also the example in ../README.rst -- so keep in sync
import pkg_resources
import pprint
import numpy as np
try:
    from scipy.misc import imsave
except ImportError:
    imsave = None

import motmot.cam_iface.cam_iface_ctypes as cam_iface

py_libinfo,c_libinfo = cam_iface.get_library_info()
print "pylibcamiface: loaded from %s version: %s" % py_libinfo
print "  libcamiface: loaded from %s version: %s" % c_libinfo

mode_num = 0
device_num = 0
num_buffers = 32

cam = cam_iface.Camera(device_num,num_buffers,mode_num)
cam.start_camera()

print "vendor", cam_iface.get_camera_info(device_num)

nt = cam.get_num_trigger_modes()
print "n trigger modes", nt
for i in range(nt):
    print "trigger", cam.get_trigger_mode_string(i)

for n in range(cam.get_num_camera_properties()):
    pprint.pprint( cam.get_camera_property_info(n) )

frame = np.asarray(cam.grab_next_frame_blocking())
print 'grabbed frame with shape %s'%(frame.shape,)
if frame is not None and imsave:
    imsave("test.png", frame)
