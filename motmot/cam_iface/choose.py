"""There is no reason to use this module. It exists for backward compatibility."""
import sys, os, warnings

wrappers_and_backends = {'ctypes':['mega']} # for backwards compatibility

def import_backend( lib_name, wrapper ):
    """import a cam_iface backend

    There is no reason to use this function. It exists for backward compatibility."""
    if wrapper != 'ctypes':
        warnings.warn('only ctypes wrapper supported')
        wrapper = 'ctypes'
    if lib_name != 'mega':
        warnings.warn('only mega backend supported')
        lib_name = 'mega'
    import motmot.cam_iface.cam_iface_ctypes as result
    return result
