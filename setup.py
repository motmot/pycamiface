import setuptools # required for namespace_packages option, below
from distutils.core import setup
import os, sys

package_data={}
ext_modules = []

build_ctypes_based_wrappers = True
include_shlibs_for_ctypes = False

if sys.platform.startswith('linux'):
    include_shlibs_for_ctypes = False

ctypes_backends = ['mega']
if build_ctypes_based_wrappers:
    if include_shlibs_for_ctypes:
        if sys.platform == 'win32':
            prefix = 'cam_iface_'
            extension = '.dll'
        elif sys.platform.startswith('linux'):
            prefix = 'libcam_iface_'
            extension = '.so'
        elif sys.platform.startswith('darwin'):
            prefix = 'libcam_iface_'
            extension = '.dylib'
        else:
            raise ValueError('unknown platform')
        for backend in ctypes_backends:
            fname = prefix+backend+extension
            if not os.path.exists(os.path.join('cam_iface',fname)):
                print '***** WARNING: Could not find file %s'%fname
            package_data.setdefault('cam_iface',[]).append(fname)

if 0:
    opj = os.path.join
    CAMIFACE_PREFIX='../cam_iface'
    include_dirs = [opj(CAMIFACE_PREFIX,'inc'),
                    opj(CAMIFACE_PREFIX,'shmwrap')]
    libpath = os.path.abspath(opj(CAMIFACE_PREFIX,'lib'))
    print 'WARNING: compiling without system install of camiface. You probably need to do this:'
    print 'export LD_LIBRARY_PATH=%s'%libpath
else:
    include_dirs = None

setup(name='motmot.cam_iface',
      description='cross-platform, cross-backend camera driver',
      long_description="""cam_iface is the core packge of several that
are involved with digital camera acquisition and analysis""",
      url='http://code.astraw.com/projects/motmot/cam_iface.html',
      version='0.5.1',
      author='Andrew Straw',
      author_email='strawman@astraw.com',
      license="BSD",
      namespace_packages = ['motmot'],
      packages = ['motmot','motmot.cam_iface'],
      ext_modules=ext_modules,
      package_data=package_data,
      )
