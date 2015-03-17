#!/usr/bin/env python

# Copyright (c) 2015, Michael Boyle
# See LICENSE file for details: <https://github.com/moble/spherical_functions/blob/master/LICENSE>

from distutils.core import setup
from auto_version import calculate_version, build_py_copy_version


setup(name='spherical_functions',
      description='Python/numba implementation of Wigner D Matrices, spin-weighted spherical harmonics, and associated functions',
      author='Michael Boyle',
      # author_email='',
      url='https://github.com/moble/spherical_functions',
      packages=['spherical_functions',],
      package_dir={'spherical_functions': '.'},
      package_data={'spherical_functions': ['*.npy']},
      version=calculate_version(),
      cmdclass={'build_py': build_py_copy_version},)
