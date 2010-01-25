import sys, os, warnings

ctypes_backends = ['mega']

wrappers_and_backends = {'ctypes':ctypes_backends,
                         }

if sys.platform == 'win32':
    prefix = ''
    extension = '.dll'
elif sys.platform.startswith('linux'):
    prefix = 'lib'
    extension = '.so'
elif sys.platform.startswith('darwin'):
    prefix = 'lib'
    extension = '.dylib'
else:
    raise ValueError("unknown platform '%s'"%sys.platform)

def my_import(name):
    mod = __import__(name)
    components = name.split('.')
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod

def import_backend( lib_name, wrapper ):
    valid_backends = wrappers_and_backends.get(wrapper,None)
    if valid_backends is None:
        raise ValueError("unknown wrapper '%s'"%wrapper)
    if lib_name not in valid_backends:
        new_lib_name = valid_backends[0]
        warnings.warn("Valid backends for the '%s' wrapper: %s "
                      "(You asked for '%s', switching to '%s'.)"%
                      (wrapper,str(valid_backends),lib_name,new_lib_name))
        lib_name = new_lib_name
    if wrapper == 'ctypes':
        if 'motmot.cam_iface.cam_iface_ctypes' in sys.modules:
            raise RuntimeError('ctypes backend already imported')
        orig = os.environ.get('CAM_IFACE_CTYPES_BACKEND',None)
        os.environ['CAM_IFACE_CTYPES_BACKEND'] = (prefix+'cam_iface_'+
                                                  lib_name+extension)
        import motmot.cam_iface.cam_iface_ctypes as result
        if orig is None:
            del os.environ['CAM_IFACE_CTYPES_BACKEND']
        else:
            os.environ['CAM_IFACE_CTYPES_BACKEND'] = orig
    elif wrapper == 'dummy':
        if 'cam_iface' in sys.modules:
            if 'motmot.cam_iface.cam_iface_dummy' not in sys.modules:
                raise RuntimeError('dummy backend must be first cam_iface backend')
        if lib_name != 'dummy':
            raise ValueError('unknown dummy backend requested')

        orig = os.environ.get('CAM_IFACE_DUMMY',None)
        os.environ['CAM_IFACE_DUMMY'] = '1'
        result = my_import('motmot.cam_iface.cam_iface_dummy')
        if orig is None:
            del os.environ['CAM_IFACE_DUMMY']
        else:
            os.environ['CAM_IFACE_DUMMY'] = orig
    elif wrapper == 'sharedmem':
        if 'cam_iface' in sys.modules:
            if 'motmot.cam_iface.cam_iface_sharedmem' not in sys.modules:
                raise RuntimeError('sharedmem backend must be first cam_iface backend')
        if lib_name != 'sharedmem':
            raise ValueError('unknown sharedmem backend requested')

        orig = os.environ.get('CAM_IFACE_SHAREDMEM',None)
        os.environ['CAM_IFACE_SHAREDMEM'] = '1'
        result = my_import('motmot.cam_iface.cam_iface_sharedmem')
        if orig is None:
            del os.environ['CAM_IFACE_SHAREDMEM']
        else:
            os.environ['CAM_IFACE_SHAREDMEM'] = orig
    else:
        raise ValueError('unknown wrapper %s'%wrapper)
    return result
