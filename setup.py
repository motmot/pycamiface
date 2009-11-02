from setuptools import setup, find_packages
from setuptools.dist import Distribution
import os, sys

import setupext, setup_autogen

package_data={}
ext_modules = []

build_ctypes_based_wrappers = True
include_shlibs_for_ctypes = False

if sys.platform.startswith('linux'):
    include_shlibs_for_ctypes = False

if sys.platform == 'win32':
    build_pyrex_based_wrappers = False
else:
    build_pyrex_based_wrappers = False
    #build_pyrex_based_wrappers = True

ctypes_backends = ['mega','unity']
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
    print 'export UNITY_BACKEND_DIR=%s'%libpath
else:
    include_dirs = None
#ext_modules.append( setupext.get_shm_extension(include_dirs=include_dirs) )

pyrex_backends = []
if build_pyrex_based_wrappers:
    #ext_modules.append( setupext.get_blank_extension() )
    if sys.platform == 'win32':
        #ext_modules.append( get_cmu1394_extension() )
        #ext_modules.append( get_bcam_extension() )
        pass # none compile easily out of the box
    elif sys.platform.startswith('linux'):
        #ext_modules.append( setupext.get_dc1394_extension() ); pyrex_backends.append('dc1394')
        try:
            ext_modules.append( setupext.get_camwire_extension() )
            pyrex_backends.append('camwire')
        except Exception,err:
            print 'WARNING: Not building camwire pyrex backend (error "%s")'%str(err)

setup_autogen.generate_choose_module(pyrex_backends, ctypes_backends)

setup(name='motmot.cam_iface',
      description='cross-platform, cross-backend camera driver',
      long_description="""cam_iface is the core packge of several that
are involved with digital camera acquisition and analysis""",
      url='http://code.astraw.com/projects/motmot/cam_iface.html',
      version='0.4.7',
      author='Andrew Straw',
      author_email='strawman@astraw.com',
      license="BSD",
      namespace_packages = ['motmot'],
      packages = find_packages(),#['cam_iface','cam_iface_choose'],
      ext_modules=ext_modules,
      zip_safe=True,
      package_data=package_data,
      )
