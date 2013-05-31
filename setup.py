try:
    from setuptools import setup, Extension
    uses_setuptools = True
except ImportError:
    from distutils.core import setup, Extension
    uses_setuptools = False


phpunserialize = Extension(
    "pakker.php._unserialize",
    sources=["pakker/php/_unserialize.c"])


if uses_setuptools:
    extra_kwargs = {
        "install_requires": ["singledispatch"]
    }
else:
    extra_kwargs = {}


setup(
    name="pakker",
    packages=["pakker", "pakker.php", "pakker.tests"],
    version="0.1",
    ext_modules=[phpunserialize],
    **extra_kwargs)
