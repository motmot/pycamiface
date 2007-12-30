pycamiface - a Python wrapper of [wiki:cam_iface].

= installation =

{{{
python setup.py install
}}}

= Backend notes =

There are currently 2 ways that Python can access the backends:
through ctypes and through Pyrex-based wrappers. ctypes is the future
and the Pyrex wrappers are legacy. Please use ctypes for future
development.

= License =

pycamiface is licensed under the BSD license. See the LICENSE.txt file
for the full description.
