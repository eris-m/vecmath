from setuptools import setup
from Cython.Build import cythonize

cython_mods = 'src/vecmath/vec.py'

if __name__ == '__main__':
    setup(
        ext_modules=cythonize(cython_mods)
    )
