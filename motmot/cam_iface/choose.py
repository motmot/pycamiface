import sys, os, warnings

def import_backend( lib_name, wrapper ):
    if wrapper != 'ctypes':
        warnings.warn('only ctypes wrapper supported')
        wrapper = 'ctypes'
    if lib_name != 'mega':
        warnings.warn('only mega backend supported')
        lib_name = 'mega'
    import motmot.cam_iface.cam_iface_ctypes as result
    return result
