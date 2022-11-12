from Cython.Build import cythonize


def build(setup_kwargs):
    ext_mods = cythonize(['vecmath/vec.py'], language_level=3)

    setup_kwargs.update({
        "ext_modules": ext_mods,
    })
