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
